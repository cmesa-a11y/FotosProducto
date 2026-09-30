#!/usr/bin/env python3
"""
Validador del tema. Comprueba tres cosas que las herramientas normales no ven:

1. JSON válido en templates/, sections/ y config/
2. Etiquetas Liquid balanceadas
3. Argumentos de {% render %} bien formados

El punto 3 existe por un fallo real: Ella trae
    {% render 'pagination-listing', ..., show_infinite_scrolling: x,pagination
                                     anchor: '', ... %}
con un token suelto ('pagination') que no es 'clave: valor'. Shopify lo repara
solo al abrir el archivo en el editor, pero si ese código viaja dentro de un
{% comment %} y alguien lo descomenta, vuelve a estar vivo y roto.

Uso:  python3 validar-tema.py
"""
import json, glob, re, sys, os

BLOQUE = {'if','unless','case','for','tablerow','capture','form','paginate',
          'schema','javascript','stylesheet','style','comment','raw','block'}
COMENTARIO = re.compile(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', re.S)
TAG = re.compile(r"\{%-?\s*(?:render|include)\s+('[^']+'|\"[^\"]+\")\s*(,.*?)?-?%\}", re.S)
ARG = re.compile(r"^[A-Za-z_][\w.]*\s*:")

def trocear(args):
    piezas, buf, prof, q = [], '', 0, None
    for ch in args:
        if q:
            buf += ch
            if ch == q: q = None
            continue
        if ch in '"\'': q = ch; buf += ch; continue
        if ch in '[({': prof += 1
        elif ch in '])}': prof -= 1
        if ch == ',' and prof == 0: piezas.append(buf); buf = ''
        else: buf += ch
    piezas.append(buf)
    return piezas

def main():
    errores = 0

    for p in glob.glob('templates/*.json') + glob.glob('sections/*.json') + glob.glob('config/*.json'):
        try: json.load(open(p, encoding='utf-8'))
        except Exception as e: print(f"  JSON inválido  {p}: {e}"); errores += 1

    for p in glob.glob('sections/*.liquid'):
        m = re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema', open(p, encoding='utf-8', errors='replace').read(), re.S)
        if m:
            try: json.loads(m.group(1))
            except Exception as e: print(f"  schema inválido  {p}: {e}"); errores += 1

    for p in sorted(glob.glob('**/*.liquid', recursive=True)):
        src = open(p, encoding='utf-8', errors='replace').read()
        pila = []
        for m in re.finditer(r'\{%-?\s*(\w+)', src):
            t = m.group(1)
            if t in BLOQUE: pila.append((t, src.count('\n', 0, m.start()) + 1))
            elif t.startswith('end'):
                if pila and pila[-1][0] == t[3:]: pila.pop()
                else: print(f"  {p}: '{t}' sin apertura"); errores += 1
        for t, l in pila: print(f"  {p}:{l}: '{t}' sin cerrar"); errores += 1

        # los comentarios no se ejecutan: se excluyen para no dar falsos positivos
        limpio = COMENTARIO.sub(lambda m: '\n' * m.group(0).count('\n'), src)
        for m in TAG.finditer(limpio):
            args = (m.group(2) or '').strip().lstrip(',')
            if not args: continue
            linea = limpio.count('\n', 0, m.start()) + 1
            for pieza in trocear(args):
                t = pieza.strip()
                if not t or t.startswith(('with ', 'for ', 'as ')): continue
                if not ARG.match(t):
                    print(f"  {p}:{linea}: argumento sin 'clave:' en render -> {t[:60]!r}")
                    errores += 1

    print(f"\n{'TODO OK' if not errores else f'{errores} problema(s)'}")
    return 1 if errores else 0

if __name__ == '__main__':
    sys.exit(main())
