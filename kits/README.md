# Kits de regalo (bundles con variantes Niño / Niña)

Actualizados el 10 nov 2026. Cada kit es un producto con la opción **Para: Niño / Niña**.
Cada variante tiene sus propios componentes (bundle "variant fixed", creado con
`productVariantRelationshipBulkUpdate`). Shopify descuenta el inventario de cada componente
y calcula solo el stock del kit. Todos están en la colección **Regalos listos**, con el tipo
`Kit de Regalo` y la etiqueta `kit-regalo`. Solo se venden en la tienda online, porque el canal
Facebook & Instagram no admite este tipo de kit.

> Ojo: si se cambian los componentes con la API, Shopify vuelve a poner como precio la suma de
> los componentes. Después hay que volver a fijar el precio combo.

| Kit | Niño | Niña | Precio | Antes |
|---|---|---|---|---|
| Kit Bienvenida Bebé (+ talla 3M/6M) | Manta Bosque + Gamuza Night Blue + Babero Drapeau Azul + Midi Box Gray | Manta Animal Print + Gamuza Palo Rosa + Babero Drapeau Rosa + Midi Box Milk Tea | 225.000 | 252.900 |
| Kit Siesta y Baño | Cobija + Toalla microfibra Mar | Cobija + Toalla microfibra Jardín Mágico | 169.000 | 188.000 |
| Kit Manta de Muselina + Babero | Manta + Babero doble faz Bosque | Manta + Babero doble faz Animal Print | 116.000 | 129.000 |
| Kit Muselina con Encaje + Babero HM (+ color muselina) | Muselina + Babero orgánico Azul | Muselina + Babero volantes Salmón | 135.000 | 150.000 |

Fotos: `kits/*.jpg` (una por versión, enlazada a su variante), generadas con `generar_fotos_kits.py`.
