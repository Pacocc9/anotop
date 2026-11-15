"""
dataton.py · Utilidades mínimas para el Datatón Tech for Good (InnoSoft 26–27).

No es obligatorio usarlo: los notebooks definen sus propias funciones para que
se entienda todo lo que pasa. Este módulo existe para no copiar y pegar lo mismo
en cada script.

Uso:
    import sys; sys.path.append("src")      # si ejecutas desde la raíz del repo
    from dataton import leer, brecha

    df = leer("DS-005")
    print(brecha(21103, 17093))
"""

from __future__ import annotations

import time
from contextlib import contextmanager
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Dónde están los datos
# ---------------------------------------------------------------------------

URL_BASE = "https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/"

# Carpeta local con los CSV (relativa a este fichero, así funciona desde
# cualquier directorio y sin rutas absolutas).
CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos" / "csv"

CATALOGO = {
    "DS-001": "DS-001_afiliacion_provincia_cnae_sexo_nacional_202609.csv",
    "DS-002": "DS-002_salario_cnae_sexo_nacional_2022.csv",
    "DS-003": "DS-003_empleo_tic_edad_sexo_andalucia_2025.csv",
    "DS-004": "DS-004_salario_edad_andalucia_2024.csv",
    "DS-005": "DS-005_salario_sexo_andalucia_2024.csv",
    "DS-006": "DS-006_salario_sexo_edad_nacional_2022.csv",
    "DS-007": "DS-007_salario_tipo_contrato_nacional_2022.csv",
    "DS-008": "DS-008_temporalidad_edad_sexo_andalucia_2025.csv",
    "DS-009": "DS-009_empleo_tic_edad_sector_andalucia_2025.csv",
    "DS-010": "DS-010_asalariados_sector_tic_andalucia_2025.csv",
    "DS-011": "DS-011_salario_sector_tic_sexo_andalucia_2022.csv",
    "DS-012": "DS-012_brecha_salarial_indicadores.csv",
    "DS-013": "DS-013_microdatos_sinteticos_tic.csv",
    "DS-014": "DS-014_salario_sector_tic_sexo_nacional_2022.csv",
    "DS-015": "DS-015_temporalidad_provincia_sexo_andalucia_2025.csv",
}

# Opciones de lectura que sirven para LOS 15 ficheros.
OPCIONES_CSV = dict(
    sep=";",               # separador de columnas
    decimal=",",           # 27,5  -> 27.5
    thousands=".",         # 1.835.875 -> 1835875
    encoding="utf-8-sig",  # quita el BOM invisible del nombre de la 1.ª columna
    na_values=["."],       # el INE usa "." para "dato no disponible" (DS-002)
)

# ---------------------------------------------------------------------------
# 2. Leer
# ---------------------------------------------------------------------------

_cache: dict[str, pd.DataFrame] = {}


def leer(codigo_o_fichero: str) -> pd.DataFrame:
    """Lee un dataset por código ("DS-005") o por nombre de fichero.

    - Si el CSV está en datos/csv/, lo lee de ahí (rápido y sin internet).
    - Si no, lo descarga de la web del datatón.
    - Guarda el resultado en memoria: leer dos veces no cuesta nada
      (InnoSoft Reciclator: no repitas trabajo).
    """
    fichero = CATALOGO.get(codigo_o_fichero, codigo_o_fichero)
    if fichero not in _cache:
        ruta_local = CARPETA_DATOS / fichero
        origen = ruta_local if ruta_local.exists() else URL_BASE + fichero
        _cache[fichero] = pd.read_csv(origen, **OPCIONES_CSV)
    return _cache[fichero].copy()


# ---------------------------------------------------------------------------
# 3. Limpiezas habituales
# ---------------------------------------------------------------------------

# Cada fichero escribe el sexo a su manera: Hombres / Varones / Hombre ...
MAPA_SEXO = {
    "Hombre": "Hombres", "Hombres": "Hombres", "Varones": "Hombres",
    "Mujer": "Mujeres", "Mujeres": "Mujeres",
    "Ambos sexos": "Ambos sexos",
}


def normalizar_sexo(serie: pd.Series) -> pd.Series:
    """Unifica las etiquetas de sexo para poder comparar ficheros."""
    return serie.map(MAPA_SEXO).fillna(serie)


def negativos_a_nan(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    """Un salario no puede ser negativo. Si aparece, NO es un dato usable:
    lo convertimos en ausente (NaN), nunca en 0, y avisamos."""
    df = df.copy()
    for col in columnas:
        n = int((df[col] < 0).sum())
        if n:
            print(f"⚠️  {col}: {n} valores negativos -> NaN (revisa la fuente original)")
            df.loc[df[col] < 0, col] = float("nan")
    return df


# ---------------------------------------------------------------------------
# 4. La brecha
# ---------------------------------------------------------------------------

def brecha(hombres: float, mujeres: float) -> dict[str, float]:
    """Devuelve la brecha con las dos definiciones habituales, en %.

    - sobre_hombres  = (H - M) / H  -> "qué parte del sueldo masculino falta"
    - hombres_sobre_mujeres = H / M - 1 -> "cuánto cobran de más los hombres"
    """
    return {
        "brecha_sobre_hombres_pct": round((hombres - mujeres) / hombres * 100, 2),
        "brecha_hombres_sobre_mujeres_pct": round((hombres / mujeres - 1) * 100, 2),
    }


# ---------------------------------------------------------------------------
# 5. Medir el tiempo (InnoSoft Reciclator)
# ---------------------------------------------------------------------------

@contextmanager
def cronometro(etiqueta: str = "bloque"):
    """with cronometro("lectura"): ...  -> imprime cuánto ha tardado."""
    inicio = time.perf_counter()
    yield
    print(f"⏱️  {etiqueta}: {time.perf_counter() - inicio:.3f} s")
