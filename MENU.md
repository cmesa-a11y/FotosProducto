# Menú de lobstermini.com

**Posicionamiento:** multimarca de niños + **especialista en regalos para bebés**.

El menú anterior era una plantilla de Lobster Mini en solitario: "Prendas superiores",
"Nuevos Basicos Mixers", "Hasta 50% OFF". Ni una marca aliada, y **ningún eje de regalo**,
que es justo la posición que quieres ocupar.

## Reparto: qué vive dónde

| Pieza | Dónde | Estado |
|---|---|---|
| Menú de escritorio | Admin → Contenido → Menús | Lo creas tú, abajo está la estructura |
| Diseño del mega menú | Tema → cabecera | ✅ configurado |
| Menú móvil | Tema → `halo-navigation-mobile` | ✅ reconstruido |

En Ella, con `mobile_menu = 'custom'` el móvil **no usa el menú de Shopify**
(`wrapper-header.liquid:23-24`): se construye en el tema. Por eso el móvil ya funciona y
el de escritorio depende de que lo crees.

## Las seis pestañas

```
REGALOS    BORDADOS    ROPA    ZAPATOS    ESENCIALES    MARCAS
```

**Regalos va primero** porque es la palabra que usa tu cliente cuando busca, no la que
usas tú para describirte. Quien llega de un baby shower no busca "canastilla": busca un
regalo. **Bordados va segundo** porque es tu diferencial y tu margen, y porque es lo que
convierte un regalo cualquiera en uno que se guarda.

El mega menú usa **tres niveles** (`halo-megamenu.liquid:33-55`): nivel 1 = pestaña,
nivel 2 = encabezado de columna, nivel 3 = enlaces. Shopify permite exactamente esos tres.

### 1 · REGALOS → `/collections/regalos` ⚠
La pestaña que da sentido a la posición. Es la única que organiza por **momento de
compra** en vez de por producto.
```
  Por ocasión
     Nacimiento                ⚠
     Baby shower               ⚠
     Primer cumpleaños         ⚠
     Bautizo                   ⚠
  Por precio
     Hasta $80.000             ⚠
     Hasta $150.000            ⚠
     Más de $150.000           ⚠
  Listos para regalar
     Canastillas y sets  → /collections/sets            ✅
     Regalo personalizado → /collections/personalizados ✅
```

### 2 · BORDADOS → `/collections/personalizados` ✅
```
  Qué puedes bordar
     Baberos · Muselinas · Toallas · Cobijas    ⚠
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
  Colecciones
     Aire Libre         → /collections/aire-libre ✅
```

### 4 · ZAPATOS → `/collections/zapatos` ⚠
Desplegable simple, sin mega menú: hoy solo hay una marca de calzado.
```
     Igor → /collections/igor-shoes  ✅
```

### 5 · ESENCIALES → `/collections/esenciales` ⚠
```
  Para la comida   → Baberos                              ⚠
  Para dormir      → Cobijas · Muselinas                  ⚠
  Para el baño     → Toallas                              ⚠
  Para cargar      → Fulares Kargo → /collections/fulares-kargo ⚠
```

### 6 · MARCAS → página de marcas (`page.template-brands.json` ya existe)
Ordenadas por desempeño, no alfabéticamente.
```
  Nuestra marca
     Lobster Mini    → /collections/lobster-mini  ✅
  Marcas aliadas
     Kings & Rebels  → /collections/kings-rebels  ✅
     Pombo & Lola    → /collections/pombo-lola    ⚠
     Igor            → /collections/igor-shoes    ✅
     Fulares Kargo   → /collections/fulares-kargo ⚠
     Piesh Kids      → /collections/piesh-kids    ⚠
```

✅ colección verificada · ⚠ hay que crearla o confirmar el handle

## Ya configurado en el tema

### Mega menú
Enganchan **por el texto de la pestaña**, comparado con `| downcase | handle`
(`halo-navigation-list.liquid:28` y `:43`): mayúsculas y tildes dan igual.

| `item` | Columnas |
|---|---|
| Regalos | 3 |
| Bordados | 2 |
| Ropa | 4 |
| Esenciales | 4 |
| Marcas | 2 |

Si nombras una pestaña distinto, no engancha y cae en desplegable simple. No se rompe
nada; pierdes el diseño.

### Menú móvil
Espejo exacto del de escritorio:
```
Regalos [Para regalar] · Bordados [Personalizado] · Ropa · Zapatos ·
Esenciales · Marcas · Ver todo
```

Quité **Aire Libre 🌿** y **Mixers 🍦** del menú móvil. Son sub-líneas de Lobster Mini, y
tenerlas en la navegación principal de una tienda multimarca es justo la herencia de la
que estás saliendo. Viven dentro de Ropa, donde las dejé.

Cada ítem del móvil tiene un campo **Menú** (`menu`, tipo `link_list`): cuando crees los
submenús en el admin se los asignas ahí y el cajón pasa de plano a anidado.

## Colecciones que faltan, por orden de urgencia

1. **`regalos`** y sus hijas por ocasión. Sin esto la posición de "especialista en regalos"
   no existe en la tienda, solo en tu cabeza.
2. **`ropa`**, **`zapatos`**, **`esenciales`** — las tres pestañas de catálogo.
3. **`pombo-lola`**, **`fulares-kargo`**, **`piesh-kids`** — las tres marcas nuevas.
4. Las colecciones de bordado (baberos, muselinas, toallas, cobijas).

Las de **precio** se montan solas con colecciones automáticas por rango; las de
**ocasión** necesitan etiquetas en los productos.

## Dos cosas que quedan abiertas

**Las fichas del home dicen Ropa · Zapatos · Bordados · Esenciales.** Si Regalos es la
primera pestaña del menú, debería estar también ahí. Son cuatro fichas y ahora hay cinco
candidatas: mi voto es cambiar Zapatos (una sola marca) por Regalos.

**Falta el eje de edad o talla.** "0-6 meses", "6-12 meses", "1-2 años". En regalo para
bebé es casi la primera pregunta: quien regala no sabe la talla, sabe la edad. Hoy no
existe en ninguna parte de la tienda.
