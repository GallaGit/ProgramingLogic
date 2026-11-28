"""CLI Typer."""

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from calculadora_precio.cli import app

DATA = Path(__file__).parent / "data"
runner = CliRunner()


def test_cli_estimar_ok():
    result = runner.invoke(
        app,
        [
            "estimar",
            "--csv",
            str(DATA / "comparables_ok.csv"),
            "--direccion",
            "Calle Ejemplo 1",
            "--barrio",
            "BarrioEjemplo",
            "--m2-construidos",
            "90",
            "--m2-utiles",
            "75",
            "--habitaciones",
            "3",
            "--banos",
            "2",
            "--planta",
            "3",
            "--ascensor",
            "--estado",
            "buen_estado",
            "--orientacion",
            "exterior",
            "--fecha-ref",
            "2026-11-28",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "recomendado" in result.output.lower() or "Recomendado" in result.output or "Rango" in result.output
    assert "Explicación" in result.output or "explicación" in result.output.lower()


def test_cli_csv_faltante():
    result = runner.invoke(
        app,
        [
            "estimar",
            "--csv",
            "/tmp/no-existe-comparables.csv",
            "--direccion",
            "x",
            "--barrio",
            "y",
            "--m2-construidos",
            "90",
            "--m2-utiles",
            "75",
            "--habitaciones",
            "3",
            "--banos",
            "1",
            "--planta",
            "1",
            "--ascensor",
            "--estado",
            "buen_estado",
            "--orientacion",
            "exterior",
        ],
    )
    assert result.exit_code != 0
