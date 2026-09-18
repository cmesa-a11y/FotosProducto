# Colecciones: estructura, taxonomía y prompts para Sidekick

## El orden importa

```
1. Definir la taxonomía   ← decidir los valores de una vez
2. Etiquetar los productos ← el trabajo de verdad
3. Crear las colecciones   ← automático, se llenan solas
```

Si creas las colecciones antes de etiquetar, salen **vacías** y parece que algo falló.
Y Sidekick no puede etiquetar por ti: no sabe si un babero es regalo de baby shower o si
un body es talla 6-12 meses. Esa decisión es tuya, producto por producto.

## Taxonomía: dos campos y un prefijo

| Qué | Dónde va | Por qué |
|---|---|---|
| **Marca** | Campo **Proveedor** | Shopify ya tiene ese campo y filtra por él de forma nativa. No lo metas en etiquetas. |
| **Todo lo transversal** | **Etiquetas**, con prefijo | El prefijo mantiene la lista ordenada y evita que dentro de un año tengas 200 etiquetas sueltas |

### Proveedores (6 valores, escritos siempre igual)
```
Lobster Mini · Kings & Rebels · Igor · Pombo & Lola · Piesh Kids · Fulares Kargo
```

### Etiquetas (17 valores)
```
cat:ropa          cat:zapatos        cat:esenciales
edad:0-6m         edad:6-12m         edad:1-2a        edad:3a-mas
ocasion:baby-shower   ocasion:cumpleanos   ocasion:bautizo
regalo            bordado
tipo:babero       tipo:muselina      tipo:toalla      tipo:cobija
```

Un mismo producto lleva varias a la vez. Un babero bordado de Lobster Mini:
`cat:esenciales`, `tipo:babero`, `bordado`, `regalo`, `ocasion:baby-shower`,
`edad:0-6m` — y Proveedor `Lobster Mini`. Con eso aparece solo en seis colecciones.

## Las 18 colecciones

⚠️ = **el handle tiene que ser exacto**, el tema ya lo enlaza. Si Shopify genera otro,
el enlace queda roto.

| Título | Handle | Condición |
|---|---|---|
| Regalos | `regalos` ⚠️ | Etiqueta = `regalo` |
| Baby shower | `baby-shower` | Etiqueta = `ocasion:baby-shower` |
| Cumpleaños | `cumpleanos` | Etiqueta = `ocasion:cumpleanos` |
| Bautizo | `bautizo` | Etiqueta = `ocasion:bautizo` |
| 0-6 meses | `0-6-meses` | Etiqueta = `edad:0-6m` |
| 6-12 meses | `6-12-meses` | Etiqueta = `edad:6-12m` |
| 1-2 años | `1-2-anos` | Etiqueta = `edad:1-2a` |
| 3 años en adelante | `3-anos-en-adelante` | Etiqueta = `edad:3a-mas` |
| Ropa | `ropa` ⚠️ | Etiqueta = `cat:ropa` |
| Zapatos | `zapatos` ⚠️ | Etiqueta = `cat:zapatos` |
| Esenciales | `esenciales` ⚠️ | Etiqueta = `cat:esenciales` |
| Pombo & Lola | `pombo-lola` ⚠️ | Proveedor = `Pombo & Lola` |
| Piesh Kids | `piesh-kids` ⚠️ | Proveedor = `Piesh Kids` |
| Fulares Kargo | `fulares-kargo` ⚠️ | Proveedor = `Fulares Kargo` |
| Baberos | `baberos` | Etiqueta = `tipo:babero` |
| Muselinas | `muselinas` | Etiqueta = `tipo:muselina` |
| Toallas | `toallas` | Etiqueta = `tipo:toalla` |
| Cobijas | `cobijas` | Etiqueta = `tipo:cobija` |

**Todas automáticas**, condición única, "coincide con todas".

Ya existen y no hay que tocarlas: `personalizados`, `lobster-mini`, `kings-rebels`,
`igor-shoes`, `tops`, `bottoms`, `vestidos`, `buzos`, `camisetas`, `sets`, `mixers`,
`aire-libre`, `accesorios`, `shop-all`.

## Paso 2 · Etiquetar (hazlo antes)

**Exporta → edita → importa.** Productos → Exportar → CSV. En la hoja solo tocas la
columna `Tags` (separadas por coma) y `Vendor`. Vuelves a importar marcando
*"Sobrescribir productos existentes"*.

Es mucho más rápido que el editor masivo si tienes más de 30 productos, y te deja un
respaldo del estado anterior.

## Paso 3 · Prompts para Sidekick

Sidekick trabaja mejor **de pocas en pocas** que con una lista de 18. Pégale un bloque,
verifica, y sigue con el siguiente.

> **Antes de empezar:** Sidekick a veces crea la colección como *manual* aunque le pidas
> automática, y a veces cambia el handle. Revisa las dos cosas en cada tanda. Si te falla
> más de dos veces, hazlas a mano: son 18 colecciones, unos 20 minutos, y tienes control
> total.

### Tanda 1 — categorías del menú
```
Crea 4 colecciones automáticas en español. Cada una con una sola condición:
el producto debe coincidir con "todas" las condiciones.

1. Título "Regalos", condición: la etiqueta del producto es igual a "regalo"
2. Título "Ropa", condición: la etiqueta del producto es igual a "cat:ropa"
3. Título "Zapatos", condición: la etiqueta del producto es igual a "cat:zapatos"
4. Título "Esenciales", condición: la etiqueta del producto es igual a "cat:esenciales"

Importante: los handles deben quedar exactamente regalos, ropa, zapatos y esenciales.
```

### Tanda 2 — edad
```
Crea 4 colecciones automáticas, cada una con una sola condición sobre la etiqueta:

1. "0-6 meses"          → etiqueta igual a "edad:0-6m"
2. "6-12 meses"         → etiqueta igual a "edad:6-12m"
3. "1-2 años"           → etiqueta igual a "edad:1-2a"
4. "3 años en adelante" → etiqueta igual a "edad:3a-mas"

Confirma que los handles quedaron 0-6-meses, 6-12-meses, 1-2-anos
y 3-anos-en-adelante.
```

### Tanda 3 — ocasión
```
Crea 3 colecciones automáticas, una condición cada una sobre la etiqueta:

1. "Baby shower" → etiqueta igual a "ocasion:baby-shower"
2. "Cumpleaños"  → etiqueta igual a "ocasion:cumpleanos"
3. "Bautizo"     → etiqueta igual a "ocasion:bautizo"
```

### Tanda 4 — marcas
```
Crea 3 colecciones automáticas cuya condición sea el PROVEEDOR del producto,
no la etiqueta:

1. "Pombo & Lola"  → proveedor igual a "Pombo & Lola"
2. "Piesh Kids"    → proveedor igual a "Piesh Kids"
3. "Fulares Kargo" → proveedor igual a "Fulares Kargo"

Los handles deben quedar pombo-lola, piesh-kids y fulares-kargo.
```

### Tanda 5 — tipos de esenciales
```
Crea 4 colecciones automáticas, una condición cada una sobre la etiqueta:

1. "Baberos"   → etiqueta igual a "tipo:babero"
2. "Muselinas" → etiqueta igual a "tipo:muselina"
3. "Toallas"   → etiqueta igual a "tipo:toalla"
4. "Cobijas"   → etiqueta igual a "tipo:cobija"
```

### Para pedirle que etiquete (con criterio tuyo)
Sidekick sí puede etiquetar en bloque si tú pones el criterio:
```
Añade la etiqueta "cat:zapatos" a todos los productos cuyo proveedor sea
Kings & Rebels, Igor o Piesh Kids.
```
```
Añade la etiqueta "bordado" y "regalo" a todos los productos de la colección
personalizados.
```

## Paso 4 · Verificar los 7 handles obligatorios

Abre cada una y mira la URL. Tiene que ser exactamente:

```
/collections/regalos      /collections/ropa        /collections/zapatos
/collections/esenciales   /collections/pombo-lola  /collections/piesh-kids
/collections/fulares-kargo
```

Si alguno salió distinto (`regalos-1`, `ropa-2`…), suele ser porque ya existe una
colección con ese handle, aunque esté archivada. Edítalo a mano en la colección.

Estos siete son los que el tema enlaza desde el home, el menú móvil y los mega menús. Los
demás solo los usa el menú de escritorio, que creas tú y puedes apuntar a donde quieras.

## Nota suelta

En la barra inferior móvil quedó un enlace a `shopify://collections/vitamina-local`
(`halo-toolbar-mobile`). Está desactivado, así que no se ve, pero es otro resto de la
etapa anterior por si te aparece.
