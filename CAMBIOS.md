# Revisión del tema Ella 6.5.5 — lobstermini.com

Origen: `theme_export__hello-mellow-25-myshopify-com-theme-export-lobstermini-com-ella-6-5-5-theme__17SEP2026-0454pm.zip`

El commit anterior sube el export sin tocar. Este aplica las correcciones.

---

## ⚠️ Antes de publicar: este export NO es el tema de Lobster Mini

Se exportó desde `hello-mellow-25.myshopify.com`. Las referencias `shopify://shop_images/...`
se resuelven **por nombre de archivo en la tienda destino**, así que al publicarlo en
lobstermini.com se pierde todo lo que no exista allí con ese nombre:

| Qué | Estado en este export |
|---|---|
| Logo cabecera | `logo_hello_mellow_sin_fondo.png` (Hello Mellow, no Lobster Mini) |
| Logo móvil y logo del segundo header | vacíos (antes `logo_web.png`) |
| Portadas de categoría 01–08 | ausentes |
| Banners SALE, banners mixers, fotos lobster*WEB | ausentes |
| Guía de tallas del producto (`size_chart_image`) | ausente |
| App embeds (Klaviyo, SmartSEO, Judge.me, Sale & Discount, Notify Me, Easy Product Addons) | **ninguno**: `settings_data.current.blocks` no existe |
| Badges de reseñas Judge.me en la ficha de producto | reemplazados por bloques de Infinite Options |
| Kiwi Size Chart, Instafeed | ausentes |

**Publicar esto tal cual apaga reseñas, emails, SEO y badges de descuento.** Súbelo como
tema no publicado, revisa logos e imágenes en el editor y reactiva los app embeds
(Configuración de la tienda → Apps) antes de publicar.

---

## P0 — Bugs que rompen páginas

### 1. Las colecciones dependían al 100% de la app USF
`snippets/collection-*.liquid` (6 archivos)

USF (Ultimate Search & Filter) había **comentado el grid nativo de productos** y lo
sustituyó por `<div id="usf_container">` con `visibility:hidden`. El servidor no
enviaba ni un producto: si el JS de la app no arrancaba, la colección quedaba en blanco.

Ahora el grid original se restaura como rama `{% else %}`:

```liquid
{%- liquid
  assign usf_active = false
  if shop.metafields.usf.settings != blank
    assign usf_active = true
  endif
-%}
{%- if usf_active -%}   ...versión USF...
{%- else -%}            ...grid nativo de Ella...
{%- endif -%}
```

### 2. `snippets/usf.liquid` podía tumbar todo el bloque de scripts
`settings: {{ shop.metafields.usf.settings }}` sin `| json` ni validación. Con el
metafield vacío se imprimía `settings: }` → **SyntaxError** que mataba el `<script>`
entero (`_usfTheme`, `_usfCollectionId`, `_usfLocale`…) y la app nunca inicializaba.
Además el `theme.id` estaba quemado (`166236455225`), así que **al duplicar el tema
USF dejaba de aplicar**. Ahora se valida el metafield y el id es `{{ theme.id }}`.

### 3. `<div>` sin cerrar que ocultaba la página de colección completa
`sections/main-collection-product-grid-no-usf.liquid`

Rapid Search abría `<div class="rps-foc-container">` (con `display:none !important`)
vía `{% render 'rapid-search-foc-wrapper-condition' %}`, pero `{% render %}` **aísla el
scope**: la variable `focIsEnabled` nunca llegaba a la sección, así que el `</div>` de
cierre jamás se emitía. El navegador cerraba el div al final del `<body>` → toda la
colección quedaba oculta. La condición ahora se evalúa dentro de la sección.

### 4. `snippets/rapid-search-settings.liquid`
- `rpsMetafields` no existía en ese snippet (mismo problema de scope) → el bloque nunca
  se ejecutaba y `window.RapidSearchSettings` nunca se definía.
- `{% assign settings = ... %}` **sobrescribía el objeto global `settings`** del tema.
- `shop.metafields.rapid-search` (guion en notación de punto) no resuelve.

### 5. `layout/theme.liquid`
- **Dos `<link rel="canonical">`** con valores distintos → Google ignora la etiqueta.
- El widget de Addi estaba **duplicado** (mismo bundle dos veces, slugs `lobstermini`
  y `lobstermini-ecommerce`) y el segundo vivía **fuera de `</body>`**. Queda una sola
  carga, con `defer`, dentro del body y con ambos selectores.
- `<meta name="theme-color" content="">` vacío.

### 6. Contenido demo de Ella en el pie, en todas las páginas
`sections/footer-group.json` tenía un `slide-show` con un único slide **sin imagen** y
titular **"Cosmopolis"**, con 50 px de margen arriba y abajo. Eliminado.

### 7. Condición de contenedor invertida
`snippets/collection-*.liquid` (12 archivos, 18 ocurrencias)

El `<div class="container">` se abría con `sidebar_type != 'horizontal'` y se cerraba
con `sidebar_type == 'horizontal'`. Con `settings.layout == '4'` quedaba un div sin
cerrar o un `</div>` huérfano. Las dos condiciones ahora coinciden.

---

## P1 — Rendimiento (Core Web Vitals)

### 8. 3 scripts bloqueantes en el `<head>`
`snippets/global-script.liquid`

`{{ 'vendor.js' | asset_url | script_tag }}` genera `<script src>` **sin defer ni
async**. `vendor.js` son 156 KB (jQuery 3.6 + slick) bloqueando el parseo del HTML en
**todas** las páginas. Es el mayor lastre de FCP/LCP del tema.

Los tres (`vendor.js`, `global.js`, `lazysizes.min.js`) ahora cargan con `defer`
(que conserva el orden de ejecución). Para no romper el JS inline que usaba jQuery en
tiempo de parseo se añadió un helper y se envolvieron **16 bloques** en 13 archivos:

```js
window.themeReady = function (fn) { /* corre en DOMContentLoaded, con jQuery ya cargado */ };
```

`lazysizes` se configura antes y se inicializa en su `onload`.

### 9. La imagen LCP se cargaba en `lazy`
- `sections/image-banner.liquid`: las 14 imágenes salían con `loading="lazy"`, incluida
  la primera de la página. Ahora las dos primeras secciones usan `eager` +
  `fetchpriority="high"`. (Ojo: Liquid evalúa condiciones de derecha a izquierda, por
  eso el `if` va anidado y no como `a != blank and a <= 2`.)
- `sections/slide-show.liquid`: el primer slide ya iba eager pero sin prioridad;
  añadido `fetchpriority="high"`. En todo el tema había **cero** `fetchpriority`.

### 10. `layout_rtl.css` (88 KB, render-blocking) en tiendas no RTL
Se cargaba con solo tener la opción activada, sin mirar el idioma. Ahora usa la misma
condición que el `<body>`: idioma realmente RTL.

### 11. Preconnect a terceros
Añadidos `preconnect` + `dns-prefetch` a `clarity.ms` y `s3.amazonaws.com` (Addi).

### 12. Home más ligera
`templates/index.json`: el primer `product-tab-block` cargaba **20 productos**; sumado a
los otros 4 bloques eran ~52 fichas de producto en el home. Bajado a 8.

---

## P2 — SEO y robustez

### 13. JSON-LD sin escapar (`snippets/schema.liquid`)
Títulos de colección, producto, artículo, autor y descripciones se inyectaban entre
comillas sin escapar: una comilla en el texto rompía el bloque y Google descartaba los
rich results. Todos pasan ahora por `| json`. Además `"gtin12/13/14"` se emitían **sin
comillas**: un código de barras con cero a la izquierda genera JSON inválido.

### 14. Open Graph (`snippets/meta-tags.liquid`)
`og:image` salía con esquema `http:` (validadores de Facebook/WhatsApp lo degradan) y
usaba el filtro `img_url`, deprecado. Añadidos `og:image:alt` y `twitter:image`, que
faltaba pese a declarar `summary_large_image`.

### 15. Valores inyectados crudos en JS (`snippets/global-script.liquid`)
`money_format`, `mobile_menu`, `currencySymbol`, `notify_form_*`, `countdown_text`,
`dynamic_browser_title_content` y 5 settings booleanos se imprimían sin `| json`
(algunos dentro de template literals, donde un backtick o `${` rompe el script).
Cinco de ellos **no existen en `settings_data.json`** y sólo funcionan porque
`settings_schema.json` tiene default; el día que se toque el schema, el `<head>`
entero deja de ejecutarse. Todos blindados con `| json`.

### 16. Cookie sin `SameSite`
`document.cookie = \`currentCollection=...\`` sin `SameSite` ni `Secure` (aviso en la
consola de Chrome). Además `template contains 'collection'` también capturaba la página
`list-collections`; ahora usa `request.page_type`.

### 17. Referencias rotas
Creados `snippets/icon-mail-1.liquid` y `snippets/multilang.liquid` (ambos se invocaban
con `{% render %}` sin existir → *"Liquid error: Could not find asset"* impreso en la
página) y los assets `loading.svg` y `green-marker.svg` (404).

### 18. `sections/main-collection-product-grid.liquid`
`window._usf_show_compare = ... ,` terminaba en **coma** en vez de punto y coma, y el
objeto `_usfGlobalSettings` repetía las claves `show_compare` y `product_compare_type`.

### 19. `target="_blank"` sin `rel` (`templates/index.json`)
El botón "Ver guía de tipografías e hilos" del bloque *¿Cómo funciona el bordado?*
abría una pestaña nueva sin `rel="noopener noreferrer"` (tabnabbing). Corregido.

---

## Pendiente — decisiones tuyas, no las toqué

1. **Enlace a Google Drive en producción.** Esa misma guía apunta a
   `drive.google.com/file/d/.../preview`. Depende de permisos de Drive, no se puede
   medir y rompe la marca. Súbelo como archivo de Shopify (Contenido → Archivos).
2. **Emojis como iconos** en los bloques de Liquid personalizado (`♾️ 🌿 🇨🇴`). La bandera
   `🇨🇴` **no se renderiza en Windows** (sale "CO"). Conviene SVG.
3. **Los bloques custom-liquid usan `max-width:480px`**: en escritorio el contenido queda
   encajonado en una columna estrecha y centrada.
4. **Doble descarga de imagen en el slideshow.** `slide-pc` y `slide-mobile` renderizan
   dos `<img>` y los alternan por CSS; el navegador descarga ambas. La solución correcta
   es `<picture>` con `<source media>`, pero implica reescribir la sección.
5. **113 archivos siguen usando `img_url`**, deprecado por Shopify en favor de
   `image_url`. Migración mecánica pero grande.
6. **SEO de colecciones.** Con USF activo el HTML de las colecciones no lleva productos
   ni paginación server-side: Google ve páginas de categoría vacías. Vale la pena
   revisar si USF debe reemplazar el grid o sólo filtrar sobre él.
7. **`<script defer>` inline** en `sections/header-basic.liquid:148`: `defer` no hace
   nada en scripts sin `src`.

---

## Verificación ejecutada

- 838 archivos empaquetados, JSON de `templates/`, `sections/`, `config/` y `locales/` válidos.
- Etiquetas Liquid balanceadas en los 480 `.liquid`.
- Los 124 `{% schema %}` parsean como JSON.
- 0 snippets o assets referenciados que falten (salvo uno dentro de `{% comment %}`).
- 0 usos de jQuery en nivel superior de scripts inline (verificado con un parser que
  ignora strings y comentarios).
- Los 77 `.js` de `assets/` pasan `node --check`.

Nada de esto sustituye una prueba en tienda: súbelo como tema **no publicado** y revisa
home, colección, ficha de producto, carrito y buscador antes de publicar.

---

# Segunda tanda — estructura del home

## Corrección a lo dicho antes

El hero **no** carga slick por ser un slideshow de un solo slide. `sections/slide-show.liquid`
guarda tanto el `data-loader-script` como el `data-init-slideshow` tras
`{% if section.blocks.size > 1 %}`. No hay nada que optimizar ahí y no se tocó.

## Código

### `sections/product-tab-block.liquid` — enlace "Ver todo"
La sección no tenía forma de enlazar a la colección completa: los cuatro grids del home
mostraban 8 productos y dejaban al usuario sin salida. Añadidos tres ajustes
(`view_all`, `link_view_all`, `view_all_align`) con el mismo marcado y las mismas clases
que ya usa `product-block.liquid`; los estilos `.view_all` viven en `base.css`, así que
no hace falta CSS nuevo. Aplicado a las dos cabeceras de la sección (con y sin banner).

## Estructura del home (`templates/index.json`)

```
 1  slide-show          → personalizados          (antes → shop-all)
 ·  Explora por Categorias        [DESACTIVADA, recuperada]
 ·  (4 categorías más)            [DESACTIVADA, recuperada]
 2  Productos Personalizables   1170  50/50   [Ver todo]
 3  ¿Cómo funciona el bordado?
 4  banner              → lobster-mini
 5  apps
 6  Lo Último en Lobster Mini   1170  50/50   [Ver todo]
 7  apps
 8  banner              → kings-rebels          (antes sin enlace)
 9  Kings & Rebels              1170  50/50   [Ver todo]
10  banner              → igor-shoes
11  Calzado Respetuoso          1170  50/50   [Ver todo]
12  Sin género · Circular · Colombia            [ACTIVADO]
```

### Eliminado (no renderizaba nada)
| Sección | Motivo |
|---|---|
| `slide_show_hGjUTB` | demo de Ella "Cosmopolis", sin imagen, desactivada |
| `slide_show_zMA7N4` | idem |
| `custom_image_banner_78M4gC` | demo "Lorem De Dorus", bloques vacíos, desactivada |
| `product_tab_block_MjcxVg` | titulada "Adultos" pero **sin ningún bloque**: no puede mostrar productos |
| `slide_show_c6TYCE` | activa, pero su único slide estaba apagado → `section.blocks.size == 0` |

Si "Adultos" era una sección planificada, se vuelve a crear en el editor en un clic.

### Recuperado
Los dos `spotlight-block` de navegación por categoría que se perdieron en el rediseño,
tomados de tu export anterior con sus 8 categorías y sus imágenes intactas:
mixers, camisetas, buzos, vestidos, bottoms, sets, accesorios y shop-all.
**Se dejaron DESACTIVADOS**: recuperarlos es dato, activarlos es una decisión de
merchandising que es tuya. Van justo debajo del hero; se encienden con un clic.

### Retícula y ritmo
Los cuatro grids de producto usaban cuatro anchos distintos (`1170`, `fullwidth`,
`container`, `1770`) y márgenes dispares. Todos a `1170` y a 50/40/30 px
(escritorio/tablet/móvil). Los banners quedan a `fullwidth` con margen 0: el aire
lo ponen los grids vecinos, así que el espaciado entre secciones es constante.

Lo que **no** unifiqué: el primer grid sigue en `scroll` a 3 por fila mientras los otros
van en `grid` a 5. Es tu producto diferenciador y las fichas más grandes le dan peso;
si lo prefieres homogéneo, son dos ajustes en el editor.

### Enlaces y textos
- Banner de Kings & Rebels: enlace añadido (era un clic muerto).
- Hero: `shop-all` → `personalizados`. **Revísalo** — es una decisión de negocio y quizá
  tengas datos que digan otra cosa; se revierte en el editor en diez segundos.
- `'Lo Último en  Lobster  Mini'` → espacios dobles corregidos.
- `'Trending Now'` → `'Kings & Rebels'`, que es lo que hay debajo y coincide con su banner.
  Vaciada la pestaña redundante "Todo de Kings & Rebels".

### Bloques de Liquid personalizado
- **¿Cómo funciona el bordado?**: estaba encajonado a 480 px, así que en escritorio los
  tres pasos salían en una columna estrecha y centrada. Reescrito con CSS con ámbito
  propio (`.lm-pasos`): apilado en móvil, **tres columnas a partir de 750 px**.
  Se conserva `rel="noopener noreferrer"` en el enlace de la guía.
- **Sin género · Circular · Colombia**: **activado** y movido al final, antes del pie.
  Los emojis se sustituyeron por SVG en línea — la bandera 🇨🇴 no se renderiza en Windows
  (sale el texto "CO") y el resto cambia de forma según el sistema operativo.

## Lo que sigue sin hacer, y por qué

1. **Prueba social.** Es lo que más convertiría en una tienda de bordado personalizado, y
   no lo añado porque tendría que inventarme el contenido. El tema ya trae
   `customer-review-block`, `instagram-grid` y `lookbook-with-collection` sin usar, y las
   dos secciones `apps` vacías del home son justo donde vivían Judge.me e Instafeed.
   En cuanto reactives esos app embeds, las secciones ya están colocadas.
2. **Activar la navegación por categoría.** Recuperada pero desactivada; decide tú si
   encaja con el home multimarca.
3. **Enlace a Google Drive** en la guía de tipografías: sigue apuntando a Drive.
   Súbelo a Contenido → Archivos.

---

# Tercera tanda — categorías del home

## Sección nueva: `spotlight_categorias`

Cuatro categorías en **una sola** sección `spotlight-block`, colocada después de
"¿Cómo funciona el bordado?" y antes del banner de Lobster Mini: el recorrido pasa de
"esto es lo nuestro" a "y este es todo el catálogo", y de ahí a las marcas.

| Ficha | Subtítulo | Destino |
|---|---|---|
| **Ropa** | Camisetas · Buzos · Vestidos · Bottoms | `/collections/ropa` ⚠️ |
| **Zapatos** | — | `/collections/zapatos` ⚠️ |
| **Bordados** | Personalízalo con el nombre | `shopify://collections/personalizados` ✅ |
| **Esenciales** | Baberos · Muselinas · Cobijas · Toallas | `/collections/esenciales` ⚠️ |

✅ verificado: ese handle ya se usa en tu home.
⚠️ **asumido**: no pude comprobar que existan. Si no existen, créalas o corrige el
destino en el editor.

Ajustes: ancho `1170`, márgenes 50/40/30, 4 columnas en escritorio y 2 en móvil,
título "Explora por categorías" y enlace "Ver todas las categorías" → `/collections`.

### Faltan las imágenes
Los cuatro bloques van **sin imagen a propósito**. La sección pinta en su lugar un
marcador que dice `370 x 440px`, que es la medida que espera. Sube las cuatro
**con la misma proporción**: `spotlight-block.liquid:31` calcula el alto de cada ficha
con `1 / aspect_ratio` de cada imagen por separado, así que una más cuadrada que las
otras desalinea la fila entera.

**No publiques el tema antes de subirlas** o el home mostrará cuatro recuadros grises.

Las imágenes conviene que vayan **sin el nombre escrito dentro**: el nombre lo pone el
tema desde el ajuste `title`, así puedes renombrar una categoría sin volver a Photoshop,
Google lee texto ancla de verdad y el enlace tiene nombre accesible. Recuerda que antes
los ocho bloques tenían `title` vacío y, por el `| default: shop.name` de la línea 31,
los ocho enlaces se llamaban "Lobster Mini".

### Ortografía
Quedó **"Esenciales"**, con S. "Escenciales" es un error de escritura frecuente y esto
se ve en la tienda.

### Sobre "Bordados"
Es la única de las cuatro que no es un tipo de producto sino un tratamiento: cruza a las
otras tres. Un babero bordado va a salir en dos fichas. No está mal —es lo mismo que una
categoría "Sale"— pero que la imagen y el subtítulo dejen claro que es *"personalízalo"*
y no *"otro tipo de producto"*.

## Otros cambios
- Eliminadas las dos secciones de 8 categorías que había recuperado, ya que pediste 4.
  Su configuración completa (8 categorías, enlaces e imágenes) queda guardada en
  `referencia/categorias-8-anteriores.json` para no volver a perderla.
- Eliminado un último bloque de demo de Ella: `large_img_9pcdLE` ("Metropólis"),
  desactivado y sin imagen, dentro de `image_banner_3nRmLM`.
  El home ya no contiene ni un solo resto de texto de plantilla.

---

# Cuarta tanda — tres marcas nuevas

Tres parejas **banner + grid**, clonadas del par de Lobster Mini
(`image_banner_3nRmLM` + `product_tab_block_yaJbK4`). Verificado que cada clon es
idéntico al original salvo en el nombre, la colección y el enlace: mismo ancho 1170,
mismos márgenes 50/40/30, mismo layout, mismo `product_block_limit: 8`, mismo estilo de
pestañas y mismo "Ver todo".

Van después del par de Igor y antes del bloque de valores:

```
13  banner Pombo & Lola     → /collections/pombo-lola      [SIN IMAGEN]
14  Pombo & Lola            → pombo-lola          [Ver todo]
15  banner Fulares Kargo    → /collections/fulares-kargo   [SIN IMAGEN]
16  Fulares Kargo           → fulares-kargo       [Ver todo]
17  banner Piesh Kids       → /collections/piesh-kids      [SIN IMAGEN]
18  Piesh Kids              → piesh-kids          [Ver todo]
```

## Lo que falta

**Handles asumidos.** `pombo-lola`, `fulares-kargo` y `piesh-kids` siguen la forma en que
Shopify convierte un nombre en handle (el `&` desaparece). No pude comprobar que existan:
si no coinciden, corrígelos en el editor o al crear las colecciones.

**Banners sin imagen.** Los seis huecos (escritorio y móvil de cada marca) van vacíos a
propósito; la sección pinta un marcador con la medida esperada. Mismas medidas que usan
los banners actuales de Kings & Rebels e Igor:

| | Medida |
|---|---|
| Escritorio | **1880 × 720 px** |
| Móvil | **638 × 780 px** |

**No publiques antes de subirlas** o saldrán tres bandas grises seguidas.

## Advertencia: el home se está alargando

Con esto quedan **19 secciones activas, 7 grids y 56 fichas de producto**. Cada ficha de
Ella carga swatches, quick view, wishlist, badges y comparador, así que 56 es mucho peso
y mucho scroll: seis marcas seguidas con la misma estructura banner→grid se vuelven
monótonas antes de llegar al pie.

Dos formas de aliviarlo sin quitar ninguna marca:

1. **Bajar el límite por grid.** De 8 a 4 en las marcas de terceros deja el home en 32
   fichas. Es un ajuste por sección en el editor.
2. **Aprovechar las pestañas.** `product-tab-block` está pensado para varias pestañas en
   una sola sección — de ahí su nombre — y hoy las siete la usan con una sola. Las tres
   marcas nuevas podrían ser tres pestañas de una misma sección "Nuestras marcas":
   un solo bloque en lugar de seis secciones, y el usuario compara marcas sin hacer
   scroll. Se monta sin tocar código, añadiendo bloques `ProductTabs`.

Lo dejé como pediste, con las tres parejas completas. Si prefieres cualquiera de las dos
alternativas, es un cambio pequeño.
