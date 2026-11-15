"""
descargar_datos.py · Descarga (o actualiza) los 15 CSV del datatón en datos/csv/.

Los CSV ya vienen incluidos en el repositorio para poder trabajar sin internet.
Ejecuta esto solo si la organización avisa de que los datos han cambiado:

    python datos/descargar_datos.py
"""

from pathlib import Path
from urllib.request import urlretrieve

URL_BASE = "https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/"
DESTINO = Path(__file__).resolve().parent / "csv"

FICHEROS = [
    "DS-001_afiliacion_provincia_cnae_sexo_nacional_202609.csv",
    "DS-002_salario_cnae_sexo_nacional_2022.csv",
    "DS-003_empleo_tic_edad_sexo_andalucia_2025.csv",
    "DS-004_salario_edad_andalucia_2024.csv",
    "DS-005_salario_sexo_andalucia_2024.csv",
    "DS-006_salario_sexo_edad_nacional_2022.csv",
    "DS-007_salario_tipo_contrato_nacional_2022.csv",
    "DS-008_temporalidad_edad_sexo_andalucia_2025.csv",
    "DS-009_empleo_tic_edad_sector_andalucia_2025.csv",
    "DS-010_asalariados_sector_tic_andalucia_2025.csv",
    "DS-011_salario_sector_tic_sexo_andalucia_2022.csv",
    "DS-012_brecha_salarial_indicadores.csv",
    "DS-013_microdatos_sinteticos_tic.csv",
    "DS-014_salario_sector_tic_sexo_nacional_2022.csv",
    "DS-015_temporalidad_provincia_sexo_andalucia_2025.csv",
]

if __name__ == "__main__":
    DESTINO.mkdir(parents=True, exist_ok=True)
    for nombre in FICHEROS:
        urlretrieve(URL_BASE + nombre, DESTINO / nombre)
        print(f"✔ {nombre} ({(DESTINO / nombre).stat().st_size / 1024:,.0f} KB)")
    print(f"\nListo: {len(FICHEROS)} ficheros en {DESTINO}")
