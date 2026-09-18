# Etiquetado de productos — el paso previo a las colecciones

Las 18 colecciones son automáticas: se llenan solas **si los productos están etiquetados**.
Crear las colecciones toma 20 minutos; etiquetar es el trabajo real. Este documento es la
regla para hacerlo sin pensar producto por producto.

## 1 · El campo Proveedor (antes que nada)

Cada producto debe tener su marca en **Proveedor**, escrita siempre igual:

```
Lobster Mini · Kings & Rebels · Igor · Pombo & Lola · Piesh Kids · Fulares Kargo
```

Con esto las 3 colecciones de marca nuevas se llenan solas, sin una sola etiqueta.
Cuidado con las variantes de escritura: `Igor` y `IGOR` son proveedores distintos para
Shopify.

## 2 · La matriz

### Categoría — una y solo una por producto

| Si el producto es… | Etiqueta |
|---|---|
| Calzado — **todo** lo de Kings & Rebels, Igor y Piesh Kids | `cat:zapatos` |
| Prenda de vestir — camisetas, buzos, vestidos, bottoms, sets, mixers | `cat:ropa` |
| Babero, muselina, cobija, toalla, fular | `cat:esenciales` |

Regla rápida: **la marca ya te dice la categoría en 3 de las 6**. Kings, Igor y Piesh son
`cat:zapatos` sin excepción.

### Tipo — solo para esenciales

| Producto | Etiqueta |
|---|---|
| Babero | `tipo:babero` |
| Muselina | `tipo:muselina` |
| Toalla | `tipo:toalla` |
| Cobija | `tipo:cobija` |
| Fular | `tipo:fular` |

### Bordado

`bordado` → todo lo que hoy está en la colección `personalizados`.

### Edad — según la talla

⚠️ **Esta tabla hay que confirmarla con tu tabla de tallas real.** Lo que hay en el tema
(`1T,2T,3T…`, `X,XS,L,M`) son valores de demo de Ella, no tuyos.

| Talla | Etiqueta |
|---|---|
| RN, 0-3M, 3-6M | `edad:0-6m` |
| 6-9M, 9-12M, 12M | `edad:6-12m` |
| 12-18M, 18-24M, 1T, 2T | `edad:1-2a` |
| 3T, 4T, 5T, 6T, 8T, 10T | `edad:3a-mas` |

Un producto que existe en varias tallas lleva **varias etiquetas de edad**. Un body que va
de 3M a 18M lleva `edad:0-6m`, `edad:6-12m` y `edad:1-2a`. Es correcto y es lo que hace
que aparezca en las tres colecciones.

### Regalo y ocasión — aquí decides tú

Estas dos no salen de una regla automática: son curaduría, y ahí está tu criterio de
tienda especializada en regalos.

**Punto de partida sugerido para `regalo`:**
- Todo lo bordado (un nombre bordado es, por definición, un regalo)
- Todo `cat:esenciales`
- Los sets y conjuntos

**Ocasión** — no fuerces las tres en todo:

| Etiqueta | Qué poner ahí |
|---|---|
| `ocasion:baby-shower` | 0-12 meses, bordables, cosas que la mamá aún no tiene |
| `ocasion:cumpleanos` | 1 año en adelante, juguetes, ropa "de estrenar" |
| `ocasion:bautizo` | blancos, ceremoniales, cobijas y mantas finas |

Un producto puede llevar varias. Uno puede no llevar ninguna.

## 3 · La forma más rápida: filtrar y etiquetar en bloque

No etiquetes producto por producto. El patrón que lo resuelve casi todo es:

```
Productos → aplicar un filtro → seleccionar todo → "..." → Añadir etiquetas
```

**Detalle que cambia todo:** al seleccionar con un filtro activo, Shopify ofrece
*"Seleccionar los N productos que coinciden con este filtro"*. Si no pulsas eso, solo
marcas los 50 de la pantalla. Es el error que hace que la gente crea que hay que ir uno
por uno.

### Las acciones, en orden

| # | Filtro | Etiqueta a añadir |
|---|---|---|
| 1 | Proveedor = Kings & Rebels | `cat:zapatos` |
| 2 | Proveedor = Igor | `cat:zapatos` |
| 3 | Proveedor = Piesh Kids | `cat:zapatos` |
| 4 | Proveedor = Fulares Kargo | `cat:esenciales` · `tipo:fular` |
| 5 | Colección = personalizados | `bordado` · `regalo` |
| 6 | Colección = tops | `cat:ropa` |
| 7 | Colección = bottoms | `cat:ropa` |
| 8 | Colección = vestidos | `cat:ropa` |
| 9 | Colección = buzos | `cat:ropa` |
| 10 | Colección = camisetas | `cat:ropa` |
| 11 | Colección = sets | `cat:ropa` · `regalo` |
| 12 | Colección = mixers | `cat:ropa` |
| 13 | Buscar "babero" | `cat:esenciales` · `tipo:babero` · `regalo` |
| 14 | Buscar "muselina" | `cat:esenciales` · `tipo:muselina` · `regalo` |
| 15 | Buscar "toalla" | `cat:esenciales` · `tipo:toalla` |
| 16 | Buscar "cobija" | `cat:esenciales` · `tipo:cobija` |

Dieciséis acciones. Unos diez minutos, y con eso queda etiquetado el grueso del catálogo
sin escribir una etiqueta más de una vez.

Puedes añadir **varias etiquetas en la misma acción**: en el cuadro de "Añadir etiquetas"
las separas por coma.

### Lo que este método NO resuelve

**Las etiquetas de edad.** Dependen de la talla, que vive en las *variantes*, y el listado
de productos del admin no permite filtrar por valor de opción. Para esto sí hace falta el
CSV — o pasármelo a mí.

**`regalo` y las de ocasión.** Son curaduría. Pero sigue usando el mismo patrón: busca o
filtra, selecciona el grupo que quieras, y añade la etiqueta en bloque.

## 4 · Que los productos nuevos se etiqueten solos

Instala **Shopify Flow** (app gratuita de Shopify). Creas una regla una vez:

```
Cuando se crea un producto
  → Si el proveedor es Kings & Rebels, Igor o Piesh Kids
      → Añadir etiqueta "cat:zapatos"
```

Y a partir de ahí no vuelves a tocar el tema. Sin esto, cada producto que subas hay que
etiquetarlo a mano o se queda fuera de todas las colecciones — que es exactamente cómo
las tiendas acaban con el catálogo a medio clasificar.

Vale la pena montar una regla por cada etiqueta que sea deducible: las de proveedor y las
de tipo por nombre del producto.

## 5 · El CSV, para lo que falta

Para las etiquetas de edad, y para cualquier corrección masa que el filtro no alcance:

```
Productos → Exportar → CSV (todos los productos)
   ↓
Abrir en Excel o Google Sheets
   ↓
Tocar SOLO dos columnas:  Vendor  y  Tags
   ↓
Productos → Importar → marcar "Sobrescribir productos existentes"
```

En `Tags` las etiquetas van **separadas por coma** en una sola celda:

```
cat:esenciales,tipo:babero,bordado,regalo,ocasion:baby-shower,edad:0-6m
```

Guarda el CSV original antes de tocarlo: es tu respaldo si algo sale mal.

## 6 · Te lo puedo hacer yo

**Exporta el CSV y pásamelo por aquí.** Te lo devuelvo con las columnas `Vendor` y `Tags`
ya rellenas según esta matriz, listo para reimportar.

Lo que aplicaría solo, sin preguntarte:
- `cat:zapatos` por proveedor (Kings, Igor, Piesh)
- `cat:ropa` y `cat:esenciales` por tipo de producto y nombre
- `tipo:*` por nombre del producto
- `bordado` a lo que esté en `personalizados`
- `edad:*` a partir de las tallas, una vez me confirmes la tabla

Lo que te devolvería **marcado para que revises**, porque es criterio tuyo y no mío:
- `regalo`
- las tres de `ocasion:`

## 7 · Después, las colecciones

Una vez etiquetado, sigue `COLECCIONES.md`: las 18 colecciones con su condición exacta y
los prompts para Sidekick. Se llenarán solas en cuanto las crees.
