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
| Kit Bienvenida Bebé (+ color y talla de zapatos) | Manta Bosque + Gamuza (Night Blue, Arena, Café, Chocolate, Negro, Gris Claro) + Babero Drapeau Azul + Midi Box Gray | Manta Animal Print + Gamuza (Palo Rosa, Cranberry, Arena, Gris Claro) + Babero Drapeau Rosa + Midi Box Milk Tea | 225.000 | 252.900 |
| Kit Siesta y Baño | Cobija + Toalla microfibra Mar | Cobija + Toalla microfibra Jardín Mágico | 169.000 | 188.000 |
| Kit Manta de Muselina + Babero | Manta + Babero doble faz Bosque | Manta + Babero doble faz Animal Print | 116.000 | 129.000 |
| Kit Babero + Zapatos Kings & Rebels (Babero / Color zapatos / Talla) | Babero a elegir: Volantes Blanco, Salmón, Floral; Orgánico Terracota, Mostaza, Vino tinto | + Gamuza Classic en 8 colores (3M/6M) | 85.000 | 94.000 |

Fotos: `kits/*.jpg` (una por versión, enlazada a su variante), generadas con `generar_fotos_kits.py`.

Los kits con zapatos tienen opciones Para / Color zapatos / Talla zapatos (20 variantes). Cada color tiene su propia foto, enlazada a la variante (`kits-color-zapatos.json`).

Kit Babero + Kings & Rebels: 96 variantes (6 baberos × 8 colores × 2 tallas), con foto por combinación de babero y color (`kits/babero-kings/`). No tiene opción Niño/Niña porque Shopify permite máximo 3 opciones.

Bordado: los 4 kits tienen la etiqueta `personalizable`, así que muestran el formulario de bordado (snippet `hm-personalizacion`) y el cobro de $20.000 se agrega solo (`hm-bordado-sync`). Se borda una pieza por kit: manta (Bienvenida, Manta + Babero), cobija (Siesta y Baño) o babero (Babero + Kings & Rebels).

Elegir pieza a bordar (tema-31): el metacampo de producto `custom.bordado_piezas` (lista de texto) muestra el paso "¿Qué quieres bordar?". Una opción que empieza por "Ambas" cobra 2 bordados. Configurado en Kit Siesta y Baño (cobija / toalla / ambas) y Kit Manta + Babero (manta / babero / ambas).
