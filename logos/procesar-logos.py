#!/usr/bin/env python3
"""
Convierte logos a PNG gris con fondo transparente, sobre lienzo cuadrado uniforme.
Pensado para la sección brand-slider de Ella (brand_image_ratio: square).

Uso:  python3 procesar-logos.py entrada/*.jpg
      python3 procesar-logos.py --gris "#8B7E6A" entrada/*.png

Supone logo OSCURO sobre fondo CLARO. Un logo blanco sobre negro sale invertido:
para esos, pásame el original y lo trato aparte.
"""
import sys, os
from PIL import Image

LIENZO   = 500     # px del lado del cuadrado
OCUPACION= 0.76    # cuánto del lienzo ocupa el logo (deja aire alrededor)
GRIS     = "#8B8B8B"
UMBRAL   = 245     # por encima de esto se considera fondo y se vuelve transparente

def procesar(ruta, gris=GRIS, salida_dir="salida"):
    hexa = gris.lstrip('#')
    r, g, b = (int(hexa[i:i+2], 16) for i in (0, 2, 4))

    im = Image.open(ruta).convert("RGB")
    ancho, alto = im.size
    px = im.load()

    # alfa a partir de la luminancia: el antialiasing del original se conserva
    capa = Image.new("RGBA", im.size, (r, g, b, 0))
    cpx = capa.load()
    for y in range(alto):
        for x in range(ancho):
            pr, pg, pb = px[x, y]
            lum = 0.299*pr + 0.587*pg + 0.114*pb
            if lum >= UMBRAL:
                continue                          # fondo -> transparente
            alfa = int(round(255 * (1 - lum/UMBRAL)))
            cpx[x, y] = (r, g, b, alfa)

    caja = capa.getbbox()                          # recorta al contenido real
    if caja:
        capa = capa.crop(caja)

    # escala para ocupar OCUPACION del lienzo, manteniendo proporción
    objetivo = int(LIENZO * OCUPACION)
    cw, ch = capa.size
    escala = min(objetivo / cw, objetivo / ch)
    capa = capa.resize((max(1, round(cw*escala)), max(1, round(ch*escala))), Image.LANCZOS)

    lienzo = Image.new("RGBA", (LIENZO, LIENZO), (0, 0, 0, 0))
    lienzo.paste(capa, ((LIENZO - capa.size[0])//2, (LIENZO - capa.size[1])//2), capa)

    os.makedirs(salida_dir, exist_ok=True)
    nombre = os.path.splitext(os.path.basename(ruta))[0] + ".png"
    destino = os.path.join(salida_dir, nombre)
    lienzo.save(destino, "PNG", optimize=True)
    return destino, caja, lienzo.size

if __name__ == "__main__":
    args = sys.argv[1:]
    gris = GRIS
    if args and args[0] == "--gris":
        gris = args[1]; args = args[2:]
    for ruta in args:
        d, caja, tam = procesar(ruta, gris)
        print(f"  {os.path.basename(ruta)} -> {d}   recorte={caja}  final={tam}")
