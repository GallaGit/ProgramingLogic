"""App Streamlit sencilla en español: vivienda + comparables → rango."""

from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import streamlit as st

from calculadora_precio.calculo import estimar_precio
from calculadora_precio.comparables import leer_comparables_csv, validar_lista_comparables
from calculadora_precio.configuracion import cargar_config
from calculadora_precio.modelos import Comparable, Estado, Orientacion, Vivienda

st.set_page_config(page_title="Calculadora de precio", layout="wide")

st.title("Calculadora de precio por comparables")
st.caption(
    "Estimación orientativa para preparar valoraciones. "
    "**No es una tasación oficial** ni sustituye la visita. Sin scraping de portales."
)

with st.sidebar:
    st.header("Configuración")
    usar_ejemplo = st.toggle("Usar coeficientes de ejemplo", value=True)
    config_file = None
    if not usar_ejemplo:
        config_file = st.file_uploader("TOML de coeficientes", type=["toml"])
    st.info(
        "Los coeficientes son **EJEMPLO, AJUSTAR**. "
        "No son datos de mercado."
    )


def _cargar_cfg():
    if usar_ejemplo or config_file is None:
        return cargar_config()
    import tempfile
    from pathlib import Path

    with tempfile.NamedTemporaryFile(suffix=".toml", delete=False) as tmp:
        tmp.write(config_file.getvalue())
        path = Path(tmp.name)
    return cargar_config(path)


col_v, col_c = st.columns(2)

with col_v:
    st.subheader("Vivienda a valorar")
    direccion = st.text_input("Dirección", value="Calle Ejemplo 1")
    barrio = st.text_input("Barrio", value="BarrioEjemplo")
    c1, c2 = st.columns(2)
    with c1:
        m2_construidos = st.number_input("m² construidos", min_value=1.0, value=90.0)
        habitaciones = st.number_input("Habitaciones", min_value=0, value=3, step=1)
        planta = st.number_input("Planta (0 = bajo)", min_value=0, value=3, step=1)
        estado = st.selectbox(
            "Estado",
            options=[e.value for e in Estado],
            index=1,
        )
        terraza = st.checkbox("Terraza")
        garaje = st.checkbox("Garaje")
    with c2:
        m2_utiles = st.number_input("m² útiles", min_value=1.0, value=75.0)
        banos = st.number_input("Baños", min_value=0, value=2, step=1)
        ascensor = st.checkbox("Ascensor", value=True)
        orientacion = st.selectbox(
            "Orientación",
            options=[o.value for o in Orientacion],
            index=0,
        )
        m2_terraza = st.number_input("m² terraza", min_value=0.0, value=0.0)
        trastero = st.checkbox("Trastero")

with col_c:
    st.subheader("Comparables (3–10)")
    modo = st.radio("Entrada", ["CSV", "Manual"], horizontal=True)
    comparables: list[Comparable] = []
    error_comp = None

    if modo == "CSV":
        st.caption("UTF-8, coma. Datos inventados de ejemplo en `examples/`.")
        uploaded = st.file_uploader("Subir CSV", type=["csv"])
        if uploaded is not None:
            import tempfile
            from pathlib import Path

            with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
                tmp.write(uploaded.getvalue())
                try:
                    comparables = leer_comparables_csv(Path(tmp.name))
                    st.success(f"{len(comparables)} comparables cargados")
                except Exception as exc:  # noqa: BLE001
                    error_comp = str(exc)
                    st.error(error_comp)
    else:
        n = st.number_input("Número de comparables", min_value=3, max_value=10, value=3)
        filas = []
        hoy = date.today()
        for i in range(int(n)):
            with st.expander(f"Comparable {i + 1}", expanded=(i == 0)):
                p1, p2, p3 = st.columns(3)
                precio = p1.number_input(f"Precio € #{i+1}", min_value=1.0, value=200000.0 + i * 10000, key=f"p{i}")
                m2 = p2.number_input(f"m² #{i+1}", min_value=1.0, value=85.0 + i * 5, key=f"m{i}")
                tipo = p3.selectbox(f"Tipo #{i+1}", ["anuncio", "cierre"], key=f"t{i}")
                fuente = st.text_input(f"Fuente #{i+1}", value="Manual", key=f"f{i}")
                fecha = st.date_input(f"Fecha #{i+1}", value=hoy - timedelta(days=30 * i), key=f"d{i}")
                b = st.text_input(f"Barrio #{i+1}", value=barrio or "BarrioEjemplo", key=f"b{i}")
                pl = st.number_input(f"Planta #{i+1}", min_value=0, value=2, key=f"pl{i}")
                asc = st.checkbox(f"Ascensor #{i+1}", value=True, key=f"a{i}")
                est = st.selectbox(f"Estado #{i+1}", [e.value for e in Estado], index=1, key=f"e{i}")
                ori = st.selectbox(f"Orientación #{i+1}", [o.value for o in Orientacion], key=f"o{i}")
                filas.append(
                    {
                        "precio": precio,
                        "m2": m2,
                        "tipo_precio": tipo,
                        "fuente": fuente,
                        "fecha": fecha,
                        "barrio": b,
                        "planta": pl,
                        "ascensor": asc,
                        "estado": est,
                        "orientacion": ori,
                    }
                )
        try:
            comparables = [
                Comparable.model_validate({**f, "url": None, "terraza": False, "garaje": False, "trastero": False})
                for f in filas
            ]
            validar_lista_comparables(comparables)
        except Exception as exc:  # noqa: BLE001
            error_comp = str(exc)
            st.error(error_comp)

st.divider()
calcular = st.button("Calcular estimación", type="primary")

if calcular:
    if error_comp:
        st.stop()
    if len(comparables) < 3:
        st.error("Introduce al menos 3 comparables (CSV o manual).")
        st.stop()
    try:
        vivienda = Vivienda(
            direccion=direccion,
            barrio=barrio,
            m2_construidos=m2_construidos,
            m2_utiles=m2_utiles,
            habitaciones=int(habitaciones),
            banos=int(banos),
            planta=int(planta),
            ascensor=ascensor,
            estado=Estado(estado),
            orientacion=Orientacion(orientacion),
            terraza=terraza,
            m2_terraza=m2_terraza if terraza and m2_terraza > 0 else None,
            garaje=garaje,
            trastero=trastero,
        )
        cfg = _cargar_cfg()
        resultado = estimar_precio(vivienda, comparables, cfg)
    except Exception as exc:  # noqa: BLE001
        st.error(str(exc))
        st.stop()

    m1, m2, m3 = st.columns(3)
    m1.metric("Mínimo", f"{resultado.precio_minimo:,.0f} €")
    m2.metric("Recomendado", f"{resultado.precio_recomendado:,.0f} €")
    m3.metric("Máximo", f"{resultado.precio_maximo:,.0f} €")

    st.write(
        f"**€/m² mediana:** {resultado.eur_m2_mediana:,.1f} · "
        f"**media (informativa):** {resultado.eur_m2_medio:,.1f} · "
        f"**base:** {resultado.base_m2} ({resultado.m2_usados} m²)"
    )

    st.subheader("Explicación de ajustes")
    for linea in resultado.explicacion:
        st.markdown(f"- {linea}")

    st.subheader("Avisos")
    for a in resultado.avisos:
        st.warning(a)

    with st.expander("Comparables usados"):
        rows = [
            {
                "precio": p.comparable.precio,
                "m2": p.comparable.m2,
                "tipo": p.comparable.tipo_precio.value,
                "€/m² bruto": round(p.eur_m2_bruto, 1),
                "€/m² tras anuncio": round(p.eur_m2_tras_anuncio, 1),
                "€/m² normalizado": round(p.eur_m2_normalizado, 1),
                "barrio": p.comparable.barrio,
                "fecha": str(p.comparable.fecha),
            }
            for p in resultado.comparables_usados
        ]
        st.dataframe(pd.DataFrame(rows), use_container_width=True)

    if resultado.comparables_descartados:
        with st.expander("Comparables descartados"):
            rows = [
                {
                    "precio": p.comparable.precio,
                    "m2": p.comparable.m2,
                    "motivo": p.motivo_descarte,
                }
                for p in resultado.comparables_descartados
            ]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
