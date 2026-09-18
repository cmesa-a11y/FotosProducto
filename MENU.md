# Menú de lobstermini.com — cómo montarlo

## Reparto: qué vive dónde

| Pieza | Dónde se configura | Estado |
|---|---|---|
| Menú de escritorio | **Admin de Shopify** → Contenido → Menús | Lo creas tú (instrucciones abajo) |
| Diseño del mega menú | **Tema** → cabecera → bloques `megamenu` | ✅ ya configurado |
| Menú móvil | **Tema** → `halo-navigation-mobile` | ✅ ya reconstruido |

El menú de escritorio es dato de la tienda, no del tema, así que no viaja en el zip.
El mega menú y el menú móvil sí, y esos ya están hechos.

## Lo que había

**Escritorio:** los 7 bloques de mega menú estaban **vacíos**, restos de la demo de Ella.
Sin configurar, cada ítem del menú caía en un desplegable simple.

**Móvil:** Ella no usa el menú de Shopify cuando `mobile_menu = 'custom'`, que es tu caso
(`wrapper-header.liquid:23-24`). El menú móvil se construye en el tema, y estaba lleno con
la estructura antigua de Lobster Mini:

```
Ver Todo · Nueva Colección Aire Libre 🌿 · Nuevos Basicos Mixers 🍦 ·
Prendas superiores · Prendas Inferiores · Sets y Conjuntos · Vestidos ·
Adultos [off] · Hasta 50% OFF🔥 · Manifiesto [off]
```

Ni una mención a bordados, zapatos, esenciales ni a ninguna de las seis marcas.
Escritorio sin configurar y móvil desactualizado: **dos navegaciones distintas**.

## La estructura propuesta: 5 pestañas

Las mismas cuatro palabras que usan las fichas de categoría del home, más marcas.
Que el menú y el home digan lo mismo es lo que hace que se aprenda.

```
BORDADOS      ROPA      ZAPATOS      ESENCIALES      MARCAS
```

## Cómo crearlo en el admin

Contenido → Menús → **Menú principal** (handle `main-menu`, que es el que lee el tema).

El mega menú usa **tres niveles**: nivel 1 = pestaña, nivel 2 = encabezado de columna,
nivel 3 = enlaces de esa columna (`halo-megamenu.liquid:33-55`). Shopify permite
exactamente esos tres.

### 1 · BORDADOS → `/collections/personalizados`
```
  Qué puedes bordar
     Baberos            ⚠ crear colección
     Muselinas          ⚠ crear colección
     Toallas            ⚠ crear colección
  Antes de pedir
     Cómo funciona      ⚠ crear página
     Tipografías e hilos ⚠ crear página (hoy es un enlace a Google Drive)
     Tiempos de entrega ⚠ crear página
```

### 2 · ROPA → `/collections/ropa` ⚠
```
  Prendas
     Prendas superiores → /collections/tops       ✅
     Prendas inferiores → /collections/bottoms    ✅
     Vestidos           → /collections/vestidos   ✅
     Buzos              → /collections/buzos      ✅
     Camisetas          → /collections/camisetas  ✅
  Conjuntos
     Sets y conjuntos   → /collections/sets       ✅
     Mixers             → /collections/mixers     ✅
  Colecciones
     Aire Libre         → /collections/aire-libre ✅
```

### 3 · ZAPATOS → `/collections/zapatos` ⚠
Desplegable simple, sin mega menú: hoy solo hay una marca de calzado.
```
     Igor               → /collections/igor-shoes ✅
```

### 4 · ESENCIALES → `/collections/esenciales` ⚠
```
  Para la comida
     Baberos            ⚠
  Para dormir
     Cobijas · Muselinas ⚠
  Para el baño
     Toallas            ⚠
  Para cargar
     Fulares Kargo      ⚠ → /collections/fulares-kargo
```

### 5 · MARCAS → página de marcas (`templates/page.template-brands.json` ya existe)
```
  Nuestra marca
     Lobster Mini       → /collections/lobster-mini ✅
  Marcas aliadas
     Kings & Rebels     → /collections/kings-rebels ✅
     Igor               → /collections/igor-shoes   ✅
     Pombo & Lola       ⚠ → /collections/pombo-lola
     Fulares Kargo      ⚠ → /collections/fulares-kargo
     Piesh Kids         ⚠ → /collections/piesh-kids
```

✅ colección verificada en tu configuración · ⚠ hay que crearla o confirmar el handle

## Lo que ya quedó hecho en el tema

### Mega menú
Eliminados los 7 bloques vacíos de la demo. Configurados 4, que se enganchan **por el
texto del ítem**, comparado con `| downcase | handle`
(`halo-navigation-list.liquid:28` y `:43`) — o sea que mayúsculas y tildes dan igual:

| Bloque | `item` | Columnas |
|---|---|---|
| megamenu_style_1 | Bordados | 3 |
| megamenu_style_1 | Ropa | 4 |
| megamenu_style_1 | Esenciales | 4 |
| megamenu_style_1 | Marcas | 2 |

Si nombras las pestañas distinto, el mega menú no engancha y el ítem cae en un
desplegable normal. No se rompe nada, pero pierdes el diseño.

Zapatos a propósito no lleva mega menú.

### Menú móvil
```
Bordados        → /collections/personalizados   [etiqueta: Personalizado]
Ropa            → /collections/ropa             ⚠
Zapatos         → /collections/zapatos          ⚠
Esenciales      → /collections/esenciales       ⚠
Marcas          → /collections
Aire Libre 🌿    → /collections/aire-libre        ✅
Mixers 🍦        → /collections/mixers            ✅
Ver todo        → /collections/shop-all          ✅
```

Colores y estilo heredados de tu configuración actual.

Cada ítem del móvil tiene además un campo **Menú** (`menu`, tipo `link_list`): cuando
crees los submenús en el admin, se los asignas ahí y el cajón móvil pasa a ser anidado
en vez de plano. Lo dejé vacío porque esos submenús todavía no existen.

## Lo que quité del móvil, y por qué

- **"Hasta 50% OFF🔥"** apuntaba a `shop-all`, no a una colección de rebajas. Prometía un
  descuento y llevaba al catálogo entero. Vuelve a ponerlo cuando tengas una colección
  de rebajas de verdad.
- **"Adultos"** y **"Manifiesto"** estaban desactivados. Manifiesto
  (`/pages/about-us-lobster-mini`) es buen contenido de marca: yo lo pondría en el pie,
  no en el menú.
- **"Nueva Colección"** y **"Nuevos Basicos"** como prefijos: envejecen mal. Quedaron
  "Aire Libre" y "Mixers".

## Consejo de fondo

Falta un eje que en ropa infantil funciona muy bien y hoy no tienes en ninguna parte:
**la edad o la talla**. "0-6 meses", "6-12 meses", "1-2 años"… Si alguna vez creas esas
colecciones, ese es el sexto ítem del menú — y probablemente el que más se use.
