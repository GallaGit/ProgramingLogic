"""CLI Typer: estima precio a partir de CSV de comparables + datos de la vivienda."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Optional

import typer

from calculadora_precio import __version__
from calculadora_precio.calculo import estimar_precio
from calculadora_precio.comparables import leer_comparables_csv
from calculadora_precio.configuracion import cargar_config
from calculadora_precio.modelos import Estado, Orientacion, Vivienda

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Estimación orientativa de precio por comparables (no es tasación).",
)


def _fmt_eur(v: float) -> str:
    # 195517 → 195.517 €
    return f"{v:,.0f} €".replace(",", "X").replace(".", ",").replace("X", ".")


@app.command("version")
def version_cmd() -> None:
    """Muestra la versión del paquete."""
    typer.echo(__version__)


@app.command("estimar")
def estimar(
    csv: Path = typer.Option(..., "--csv", help="CSV de comparables"),
    direccion: str = typer.Option(..., help="Dirección de la vivienda"),
    barrio: str = typer.Option(..., help="Barrio (define la zona)"),
    m2_construidos: float = typer.Option(..., help="m² construidos"),
    m2_utiles: float = typer.Option(..., help="m² útiles"),
    habitaciones: int = typer.Option(..., help="Habitaciones"),
    banos: int = typer.Option(..., help="Baños"),
    planta: int = typer.Option(..., help="Planta (0 = bajo)"),
    ascensor: bool = typer.Option(..., help="¿Tiene ascensor?"),
    estado: Estado = typer.Option(..., help="a_reformar | buen_estado | reformado"),
    orientacion: Orientacion = typer.Option(..., help="exterior | interior"),
    terraza: bool = typer.Option(False, help="¿Tiene terraza?"),
    m2_terraza: Optional[float] = typer.Option(None, help="m² de terraza"),
    garaje: bool = typer.Option(False, help="¿Tiene garaje?"),
    trastero: bool = typer.Option(False, help="¿Tiene trastero?"),
    config: Optional[Path] = typer.Option(
        None, "--config", help="TOML de coeficientes (por defecto el ejemplo)"
    ),
    json_out: Optional[Path] = typer.Option(
        None, "--json", help="Guardar resultado completo en JSON"
    ),
    fecha_ref: Optional[str] = typer.Option(
        None, "--fecha-ref", help="Fecha de referencia AAAA-MM-DD (antigüedad)"
    ),
) -> None:
    """Calcula el rango de precio y muestra la explicación."""
    cfg = cargar_config(config)
    comparables = leer_comparables_csv(csv)
    vivienda = Vivienda(
        direccion=direccion,
        barrio=barrio,
        m2_construidos=m2_construidos,
        m2_utiles=m2_utiles,
        habitaciones=habitaciones,
        banos=banos,
        planta=planta,
        ascensor=ascensor,
        estado=estado,
        orientacion=orientacion,
        terraza=terraza,
        m2_terraza=m2_terraza,
        garaje=garaje,
        trastero=trastero,
    )
    ref = date.fromisoformat(fecha_ref) if fecha_ref else date.today()
    try:
        resultado = estimar_precio(vivienda, comparables, cfg, fecha_referencia=ref)
    except ValueError as exc:
        typer.secho(str(exc), fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1) from exc

    typer.echo("")
    typer.secho("Estimación orientativa (NO es tasación)", bold=True)
    typer.echo(f"Vivienda: {vivienda.direccion} — {vivienda.barrio}")
    typer.echo(
        f"Rango: {_fmt_eur(resultado.precio_minimo)}  |  "
        f"recomendado {_fmt_eur(resultado.precio_recomendado)}  |  "
        f"{_fmt_eur(resultado.precio_maximo)}"
    )
    typer.echo(
        f"€/m² mediana: {resultado.eur_m2_mediana:,.1f}  "
        f"(media informativa: {resultado.eur_m2_medio:,.1f})"
    )
    typer.echo(
        f"Comparables usados: {len(resultado.comparables_usados)}  "
        f"| descartados: {len(resultado.comparables_descartados)}  "
        f"| anuncios: {resultado.n_anuncio}  cierres: {resultado.n_cierre}"
    )
    typer.echo("")
    typer.secho("Explicación de ajustes", bold=True)
    for linea in resultado.explicacion:
        typer.echo(f"  · {linea}")
    typer.echo("")
    typer.secho("Avisos", bold=True)
    for a in resultado.avisos:
        typer.echo(f"  ! {a}")

    if json_out:
        json_out.write_text(
            resultado.model_dump_json(indent=2),
            encoding="utf-8",
        )
        typer.echo(f"\nJSON guardado en {json_out}")


if __name__ == "__main__":
    app()
