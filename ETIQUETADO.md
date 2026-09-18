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

## 3 · Cómo aplicarlo: el CSV

Con más de 30 productos, el editor masivo de Shopify se hace lento y propenso a errores.
El camino bueno:

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

## 4 · Te lo puedo hacer yo

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

## 5 · Después, las colecciones

Una vez etiquetado, sigue `COLECCIONES.md`: las 18 colecciones con su condición exacta y
los prompts para Sidekick. Se llenarán solas en cuanto las crees.
