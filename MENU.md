# Menú de lobstermini.com

**Posicionamiento:** multimarca de niños + **especialista en regalos para bebés**.

El menú anterior era una plantilla de Lobster Mini en solitario — "Prendas superiores",
"Nuevos Basicos Mixers", "Hasta 50% OFF" — sin ninguna marca aliada, sin eje de regalo y
sin eje de edad. Los dos ejes que más necesita esta tienda.

## Reparto: qué vive dónde

| Pieza | Dónde | Estado |
|---|---|---|
| Menú de escritorio | Admin → Contenido → Menús | Lo creas tú, estructura abajo |
| Diseño del mega menú | Tema → cabecera | ✅ configurado |
| Menú móvil | Tema → `halo-navigation-mobile` | ✅ reconstruido |

Con `mobile_menu = 'custom'` Ella **no usa el menú de Shopify en móvil**
(`wrapper-header.liquid:23-24`): lo construye desde el tema. Por eso el móvil ya funciona
y el de escritorio depende de que lo crees.

## Las seis pestañas

```
REGALOS    BORDADOS    ROPA    ZAPATOS    ESENCIALES    MARCAS
```

**Regalos primero** porque es la palabra que usa tu cliente al buscar, no la que usas tú
para describirte: quien sale de un baby shower no busca "canastilla", busca un regalo.
**Bordados segundo** porque es tu margen y lo que convierte un regalo cualquiera en uno
que se guarda.

Tres niveles (`halo-megamenu.liquid:33-55`): nivel 1 = pestaña, nivel 2 = encabezado de
columna, nivel 3 = enlaces. Shopify permite exactamente esos tres.

### 1 · REGALOS → `/collections/regalos` ⚠
La única pestaña que organiza por **momento de compra** en vez de por producto.
```
  Por ocasión
     Baby shower               ⚠
     Cumpleaños                ⚠
     Bautizo                   ⚠
  Por edad
     0-6 meses                 ⚠
     6-12 meses                ⚠
     1-2 años                  ⚠
     3 años en adelante        ⚠
  Listos para regalar
     Canastillas y sets   → /collections/sets            ✅
     Regalo personalizado → /collections/personalizados  ✅
```

### 2 · BORDADOS → `/collections/personalizados` ✅
```
  Qué puedes bordar
     Baberos · Muselinas · Toallas · Cobijas   ⚠
  Antes de pedir
     Cómo funciona · Tipografías e hilos · Tiempos de entrega   ⚠ páginas
```

### 3 · ROPA → `/collections/ropa` ⚠
```
  Prendas
     Prendas superiores → /collections/tops      ✅
     Prendas inferiores → /collections/bottoms   ✅
     Vestidos           → /collections/vestidos  ✅
     Buzos              → /collections/buzos     ✅
     Camisetas          → /collections/camisetas ✅
  Conjuntos
     Sets y conjuntos   → /collections/sets      ✅
     Mixers             → /collections/mixers    ✅
  Por edad
     0-6 meses · 6-12 meses · 1-2 años · 3 años en adelante   ⚠
  Colecciones
     Aire Libre         → /collections/aire-libre ✅
```

### 4 · ZAPATOS → `/collections/zapatos` ⚠
Tres marcas fuertes, agrupadas.
```
  Marcas
     Kings & Rebels → /collections/kings-rebels ✅
     Igor           → /collections/igor-shoes   ✅
     Piesh Kids     → /collections/piesh-kids   ⚠
  Por edad
     0-6 meses · 6-12 meses · 1-2 años · 3 años en adelante   ⚠
  Primeros pasos
     Pre-andantes · Andantes    ⚠ (opcional, muy usado en calzado infantil)
```

### 5 · ESENCIALES → `/collections/esenciales` ⚠
```
  Para la comida   → Baberos                                     ⚠
  Para dormir      → Cobijas · Muselinas                         ⚠
  Para el baño     → Toallas                                     ⚠
  Para cargar      → Fulares Kargo → /collections/fulares-kargo  ⚠
```

### 6 · MARCAS → página de marcas (`page.template-brands.json` ya existe)
Por desempeño, no alfabéticamente.
```
  Nuestra marca
     Lobster Mini    → /collections/lobster-mini  ✅
  Marcas aliadas
     Kings & Rebels  → /collections/kings-rebels  ✅
     Pombo & Lola    → /collections/pombo-lola    ⚠
     Igor            → /collections/igor-shoes    ✅
     Piesh Kids      → /collections/piesh-kids    ⚠
     Fulares Kargo   → /collections/fulares-kargo ⚠
```

✅ verificada · ⚠ hay que crearla o confirmar el handle

## Por qué la edad no es una pestaña

Con Edad serían siete pestañas, demasiadas para una barra horizontal. Y la edad por sí
sola no es un destino de compra: nadie busca "6-12 meses", busca *ropa* o *un regalo*
para esa edad. Por eso va como **columna dentro de Regalos, Ropa y Zapatos**, que es
donde se usa.

Si aun así la quieres como pestaña propia, dímelo: la candidata a salir sería Esenciales,
que se puede absorber dentro de Regalos.

## Ya configurado en el tema

### Mega menú
Enganchan **por el texto de la pestaña**, comparado con `| downcase | handle`
(`halo-navigation-list.liquid:28` y `:43`): mayúsculas y tildes dan igual.

| `item` | Columnas |
|---|---|
| Regalos | 3 |
| Bordados | 2 |
| Ropa | 4 |
| Zapatos | 3 |
| Esenciales | 4 |
| Marcas | 2 |

Si nombras una pestaña distinto no engancha y cae en desplegable simple: no se rompe
nada, pierdes el diseño.

### Menú móvil
Espejo del de escritorio:
```
Regalos [Para regalar] · Bordados [Personalizado] · Ropa · Zapatos ·
Esenciales · Marcas · Ver todo
```

Quité **Aire Libre 🌿** y **Mixers 🍦**: son sub-líneas de Lobster Mini, y tenerlas en la
navegación principal de una tienda multimarca es la herencia de la que estás saliendo.
Siguen dentro de Ropa.

Cada ítem del móvil tiene un campo **Menú** (`menu`, tipo `link_list`): cuando crees los
submenús en el admin se los asignas ahí y el cajón pasa de plano a anidado.

## Colecciones que faltan, por urgencia

1. **`regalos`** + las 3 de ocasión (baby shower, cumpleaños, bautizo). Sin esto la
   posición de especialista en regalos no existe en la tienda.
2. **Las 4 de edad**: `0-6-meses`, `6-12-meses`, `1-2-anos`, `3-anos-en-adelante`.
   Se montan como colecciones **automáticas** por etiqueta, así que basta con etiquetar
   los productos una vez.
3. **`ropa`**, **`zapatos`**, **`esenciales`** — las pestañas de catálogo.
4. **`pombo-lola`**, **`piesh-kids`**, **`fulares-kargo`** — las marcas nuevas.
5. Las de bordado: baberos, muselinas, toallas, cobijas.

Las de ocasión también pueden ser automáticas por etiqueta. Un mismo producto puede estar
en varias: un babero bordado puede ser `baby-shower` + `0-6-meses` + `bordados` a la vez.
