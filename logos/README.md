# Logos para la cinta de marcas (`brand-slider`)

## Qué hace el script

`procesar-logos.py` convierte un logo a **PNG gris con fondo transparente**, centrado en
un lienzo **cuadrado** de 500×500, ocupando el 76% para que todos respiren igual.

El alfa se calcula desde la luminancia del original, no con un recorte por umbral, así que
**el antialiasing se conserva**: los bordes quedan suaves y no dentados.

```bash
python3 procesar-logos.py logo1.jpg logo2.png
python3 procesar-logos.py --gris "#8B7E6A" *.jpg
```

## Limitación

Supone **logo oscuro sobre fondo claro**. Un logo blanco sobre negro saldría invertido, y
uno a color perdería la forma si tiene zonas claras que deban ser opacas. Esos hay que
tratarlos aparte.

## Ajustes

| Constante | Valor | Qué controla |
|---|---|---|
| `LIENZO` | 500 | Lado del cuadrado en px |
| `OCUPACION` | 0.76 | Cuánto del lienzo ocupa el logo |
| `GRIS` | `#8B8B8B` | Color final |
| `UMBRAL` | 245 | Por encima de esta luminancia es fondo |

## Por qué cuadrado

La sección `brand-slider` tiene `brand_image_ratio` en `square`. Si los logos llegan con
proporciones distintas, la fila se descuadra. Con todos en el mismo lienzo cuadrado y el
mismo aire, la cinta se ve pareja.

## Pendiente: equilibrar ópticamente

Un logo ancho escalado al 76% del ancho se ve **más pequeño** que uno cuadrado escalado al
76% en ambos lados, aunque midan lo mismo. Con los seis logos juntos se ajusta el factor
de cada uno para que pesen igual a la vista. Eso solo se puede afinar viéndolos en fila.
