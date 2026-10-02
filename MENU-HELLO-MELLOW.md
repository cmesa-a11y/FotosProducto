# Menú de Hello Mellow

Menú principal de `hello-mellow-25.myshopify.com` (Admin → Contenido → Menús → Menú principal).
Acordado en sesión; sustituye a la propuesta de `MENU.md`, que era para Lobster Mini.

## Las cinco pestañas

```
NOVEDADES    REGALOS    PERSONALIZADOS    ESENCIALES    MARCAS
```

Tres niveles: pestaña → encabezado de columna → enlaces.

### 1 · NOVEDADES → `/collections/all?sort_by=created-descending`
Sin submenú. Lista todo el catálogo con lo más reciente primero, así se mantiene sola
sin tener que etiquetar ni mover productos a mano.

### 2 · REGALOS → `/collections/regalos`
```
  Por ocasión
     Baby shower   → /collections/baby-shower
     Cumpleaños    → /collections/cumpleanos
     Bautizo       → /collections/bautizo
  Por edad
     0-6 meses     → /collections/0-6-meses
     6-12 meses    → /collections/6-12-meses
     1-2 años      → /collections/1-2-anos
     3 años o más  → /collections/3-anos-en-adelante
```

### 3 · PERSONALIZADOS → `/collections/personalizados`
```
  Qué bordamos     → /collections/personalizados
  Cómo funciona    → página (por crear)
```

### 4 · ESENCIALES → `/collections/esenciales`
```
  Para comer       → /collections/baberos
  Para dormir      → /collections/cobijas · /collections/muselinas
  Para el baño     → /collections/toallas
  Para cargar      → /collections/fulares-kargo
```

### 5 · MARCAS
```
  Lobster Mini           → /collections/lobster-mini
  Kings & Rebels         → /collections/kings-rebels
  Igor                   → /collections/igor-shoes
  Pombo & Lola           → /collections/pombo-y-lola
  Fulares Kargo          → /collections/fulares-kargo
  Un libro para siempre  → por confirmar
  Piesh Kids             → por confirmar
```

## Pendiente de comprobar en la tienda

Los handles marcados arriba se confirman contra las colecciones reales antes de crear el
menú. Las que no existan se crean (automáticas por etiqueta, ver `COLECCIONES.md`) o se
quitan del menú.

## Estado (2 oct 2026): menú creado en la tienda

El menú principal (`main-menu`) se reemplazó con las cinco pestañas. Diferencias con lo de
arriba, según lo que había en la tienda:

- **Por edad**: no existen `3-anos-en-adelante` y `6-12-meses` está vacía. Quedó
  `0-12 meses` (handle `0-6-meses`, 90 productos), `1-2 años`, `3-6 años` y `6-10 años`.
- **Personalizados**: falta "Cómo funciona"; la página no existe todavía.
- **Esenciales**: solo Para comer (Baberos) y Para cargar (Fulares Kargo). No hay colecciones
  de cobijas, muselinas ni toallas, y ningún producto lleva `tipo:cobija`, `tipo:muselina`
  ni `tipo:toalla`.
- **Marcas**: la pestaña enlaza a `/collections/marcas-especiales`. Se incluyó Un libro para
  siempre (la colección existe). Falta Piesh Kids: hay 18 productos con ese proveedor, pero
  no tiene colección.
- Se quitó el ítem anterior "Bebé 0-18 Meses".
