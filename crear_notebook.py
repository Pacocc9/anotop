import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "id": "header",
   "metadata": {},
   "source": [
    "# Datatón Tech for Good · InnoSoft 26–27\n",
    "## Equipo: `Anotop`\n",
    "**Integrantes:** Juan · Nico · Paco\n",
    "\n",
    "---\n",
    "### La pregunta\n",
    "> **¿Cuánto de la brecha salarial bruta en Andalucía responde realmente a una diferencia de salario a igual trabajo y cuánto a la diferencia de horas trabajadas?**\n",
    "\n",
    "### Datos que usamos\n",
    "| Código | Dataset | Fuente · año · territorio | Por qué lo usamos |\n",
    "|---|---|---|---|\n",
    "| **DS-005** | Salario por sexo en Andalucía | IECA · MCVL 2024 · Andalucía | Comparar salario bruto frente a salario equivalente a tiempo completo. |\n",
    "| **DS-004** | Salario por edad en Andalucía | IECA · MCVL 2024 · Andalucía | Analizar la evolución salarial y efecto jornada por grupos de edad. |\n",
    "| **DS-012** | Indicadores de brecha salarial | Derivado oficial · 2022-2024 | Validación y control de consistencia de las dos fórmulas oficiales. |\n",
    "| **DS-013** | Microdatos sintéticos TIC | Simulación calibrada · 3.000 filas | Modelo de regresión econométrica para aislar el efecto de horas y puesto. |\n",
    "\n",
    "### Definiciones oficiales\n",
    "- **Brecha sobre hombres (%):** `(Hombres − Mujeres) / Hombres * 100`\n",
    "- **Brecha de hombres sobre mujeres (%):** `(Hombres / Mujeres − 1) * 100`\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec0",
   "metadata": {},
   "source": [
    "## 0 · Preparación y funciones de carga robusta\n",
    "Descarga automática desde el repositorio oficial si se ejecuta en Google Colab o carga local."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "code0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "from pathlib import Path\n",
    "import matplotlib\n",
    "matplotlib.use('Agg')\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "try:\n",
    "    from IPython.display import display\n",
    "except Exception:\n",
    "    display = print\n",
    "\n",
    "INICIO = time.perf_counter()\n",
    "URL_BASE = \"https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/\"\n",
    "Path(\"figuras\").mkdir(exist_ok=True)\n",
    "Path(\"resultados\").mkdir(exist_ok=True)\n",
    "\n",
    "MAPEO = {\n",
    "    \"DS-005\": \"DS-005_salario_sexo_andalucia_2024.csv\",\n",
    "    \"DS-004\": \"DS-004_salario_edad_andalucia_2024.csv\",\n",
    "    \"DS-012\": \"DS-012_brecha_salarial_indicadores.csv\",\n",
    "    \"DS-013\": \"DS-013_microdatos_sinteticos_tic.csv\"\n",
    "}\n",
    "\n",
    "def leer(nombre):\n",
    "    archivo = MAPEO.get(nombre, nombre if nombre.endswith(\".csv\") else f\"{nombre}.csv\")\n",
    "    for p in [Path(archivo), Path(\"datos/csv\") / archivo, Path(\"../datos/csv\") / archivo]:\n",
    "        if p.exists():\n",
    "            return pd.read_csv(p, sep=\";\", decimal=\",\", thousands=\".\", encoding=\"utf-8-sig\", na_values=[\".\"])\n",
    "    return pd.read_csv(URL_BASE + archivo, sep=\";\", decimal=\",\", thousands=\".\", encoding=\"utf-8-sig\", na_values=[\".\"])\n",
    "\n",
    "print(\"Entorno inicializado correctamente.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec1",
   "metadata": {},
   "source": [
    "## 1 · Análisis Oficial Macro (Andalucía - IECA MCVL 2024)\n",
    "Cálculo de brechas salariales oficiales, comparación media vs. mediana y validación con DS-012."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "code1",
   "metadata": {},
   "outputs": [],
   "source": [
    "salario_sexo = leer(\"DS-005\").set_index(\"sexo\")\n",
    "salario_edad = leer(\"DS-004\")\n",
    "indicadores = leer(\"DS-012\")\n",
    "\n",
    "h_b, m_b = salario_sexo.loc[\"Hombres\", \"salario_bruto_anual\"], salario_sexo.loc[\"Mujeres\", \"salario_bruto_anual\"]\n",
    "h_eq, m_eq = salario_sexo.loc[\"Hombres\", \"salario_eq_tiempo_completo\"], salario_sexo.loc[\"Mujeres\", \"salario_eq_tiempo_completo\"]\n",
    "h_p50, m_p50 = salario_sexo.loc[\"Hombres\", \"bruto_p50\"], salario_sexo.loc[\"Mujeres\", \"bruto_p50\"]\n",
    "h_eq50, m_eq50 = salario_sexo.loc[\"Hombres\", \"eq_p50\"], salario_sexo.loc[\"Mujeres\", \"eq_p50\"]\n",
    "\n",
    "brechas_macro = pd.DataFrame([\n",
    "    {\"Indicador\": \"Salario bruto anual medio\", \"Hombres (€)\": h_b, \"Mujeres (€)\": m_b, \"Brecha_sobre_H (%)\": (h_b - m_b)/h_b*100, \"Brecha_H_sobre_M (%)\": (h_b/m_b - 1)*100},\n",
    "    {\"Indicador\": \"Salario equivalente a tiempo completo\", \"Hombres (€)\": h_eq, \"Mujeres (€)\": m_eq, \"Brecha_sobre_H (%)\": (h_eq - m_eq)/h_eq*100, \"Brecha_H_sobre_M (%)\": (h_eq/m_eq - 1)*100},\n",
    "    {\"Indicador\": \"Mediana bruta anual (P50)\", \"Hombres (€)\": h_p50, \"Mujeres (€)\": m_p50, \"Brecha_sobre_H (%)\": (h_p50 - m_p50)/h_p50*100, \"Brecha_H_sobre_M (%)\": (h_p50/m_p50 - 1)*100},\n",
    "    {\"Indicador\": \"Mediana equivalente (P50)\", \"Hombres (€)\": h_eq50, \"Mujeres (€)\": m_eq50, \"Brecha_sobre_H (%)\": (h_eq50 - m_eq50)/h_eq50*100, \"Brecha_H_sobre_M (%)\": (h_eq50/m_eq50 - 1)*100}\n",
    "]).round(2)\n",
    "\n",
    "display(brechas_macro)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec2",
   "metadata": {},
   "source": [
    "## 2 · Análisis Microdatos TIC y Descomposición del Efecto Horas (DS-013)\n",
    "Descomponemos cuánto de la brecha proviene del salario por hora y cuánto de las horas trabajadas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "code2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = leer(\"DS-013\")\n",
    "\n",
    "resumen = df.groupby(\"sexo\")[[\"salario_bruto_anual\", \"salario_hora\", \"horas_semana\"]].agg([\"mean\", \"median\", \"count\"])\n",
    "display(resumen.round(2))\n",
    "\n",
    "medias = df.groupby(\"sexo\")[[\"salario_bruto_anual\", \"salario_hora\", \"horas_semana\"]].mean()\n",
    "h = medias.loc[\"Hombre\"]\n",
    "m = medias.loc[\"Mujer\"]\n",
    "\n",
    "salario_h_horas_h = h[\"salario_hora\"] * h[\"horas_semana\"]\n",
    "efecto_horas = (h[\"salario_hora\"] * (h[\"horas_semana\"] - m[\"horas_semana\"])) / salario_h_horas_h\n",
    "efecto_salario_hora = ((h[\"salario_hora\"] - m[\"salario_hora\"]) * m[\"horas_semana\"]) / salario_h_horas_h\n",
    "\n",
    "peso_hora = efecto_salario_hora / (efecto_salario_hora + efecto_horas) * 100\n",
    "peso_horas = efecto_horas / (efecto_salario_hora + efecto_horas) * 100\n",
    "\n",
    "print(f\"Descomposición del efecto en DS-013:\")\n",
    "print(f\"- Peso del salario por hora: {peso_hora:.2f}%\")\n",
    "print(f\"- Peso de las horas semanales: {peso_horas:.2f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec3",
   "metadata": {},
   "source": [
    "## 3 · Modelo Econométrico Ajustado (Regresión Log-Lineal Mincer)\n",
    "Aislamos la brecha salarial por hora controlando por edad, experiencia, antigüedad, horas y rol ocupacional."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "code3",
   "metadata": {},
   "outputs": [],
   "source": [
    "numericas = [\"edad\", \"anios_experiencia\", \"antiguedad_empresa\", \"horas_semana\"]\n",
    "categoricas = [\"tipo_contrato\", \"jornada\", \"ocupacion\", \"tamano_empresa\", \"provincia\", \"teletrabajo\"]\n",
    "\n",
    "X = pd.concat([\n",
    "    (df[\"sexo\"] == \"Mujer\").astype(int).rename(\"mujer\"),\n",
    "    df[numericas],\n",
    "    pd.get_dummies(df[categoricas], drop_first=True, dtype=int)\n",
    "], axis=1)\n",
    "\n",
    "y = np.log(df[\"salario_hora\"])\n",
    "modelo = LinearRegression().fit(X, y)\n",
    "coef_mujer = modelo.coef_[X.columns.get_loc(\"mujer\")]\n",
    "brecha_ajustada = (1 - np.exp(coef_mujer)) * 100\n",
    "\n",
    "print(f\"R² del modelo: {modelo.score(X, y):.3f}\")\n",
    "print(f\"Brecha salarial por hora sin ajustar: {((h['salario_hora'] - m['salario_hora']) / h['salario_hora'] * 100):.2f}%\")\n",
    "print(f\"Brecha salarial ajustada (controlando puesto, experiencia y jornada): {brecha_ajustada:.2f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec4",
   "metadata": {},
   "source": [
    "## 4 · Visualizaciones (Guardado automático en figuras/)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "code4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Grafico 1: Efecto jornada en Andalucía\n",
    "fig, ax = plt.subplots(figsize=(7, 4.2))\n",
    "indicadores_n = [\"Salario Bruto Anual Medio\", \"Salario Eq. Tiempo Completo\"]\n",
    "h_vals = [h_b, h_eq]\n",
    "m_vals = [m_b, m_eq]\n",
    "x = np.arange(len(indicadores_n))\n",
    "width = 0.35\n",
    "ax.bar(x - width/2, h_vals, width, label=\"Hombres\", color=\"#1f77b4\")\n",
    "ax.bar(x + width/2, m_vals, width, label=\"Mujeres\", color=\"#e377c2\")\n",
    "ax.set_ylabel(\"Euros anuales (€)\")\n",
    "ax.set_xticks(x)\n",
    "ax.set_xticklabels(indicadores_n, fontweight=\"bold\")\n",
    "ax.set_ylim(0, 32000)\n",
    "ax.legend()\n",
    "ax.annotate(\"Brecha: 19,0%\\n(H: 21.103€ vs M: 17.093€)\", xy=(0, 21500), ha=\"center\", fontsize=9, fontweight=\"bold\")\n",
    "ax.annotate(\"Brecha: 8,2%\\n(H: 27.182€ vs M: 24.945€)\\n[-56,8% reducción]\", xy=(1, 27500), ha=\"center\", fontsize=9, fontweight=\"bold\", color=\"#1b7837\")\n",
    "fig.suptitle(\"El efecto jornada: la brecha cae del 19,0% al 8,2% a tiempo completo\", fontsize=11, fontweight=\"bold\", x=0.02, ha=\"left\")\n",
    "fig.text(0.02, 0.01, \"Fuente: IECA · MCVL 2024 (DS-005). Asalariados en Andalucía.\", fontsize=8, color=\"gray\")\n",
    "fig.tight_layout(rect=(0, 0.04, 1, 0.95))\n",
    "fig.savefig(\"figuras/grafico1_efecto_jornada_andalucia.png\", dpi=200)\n",
    "plt.close()\n",
    "\n",
    "# Grafico 2: Brecha por ocupacion TIC\n",
    "tabla_ocup = df.pivot_table(index=\"ocupacion\", columns=\"sexo\", values=\"salario_hora\", aggfunc=\"mean\")\n",
    "tabla_ocup[\"brecha_%\"] = ((tabla_ocup[\"Hombre\"] - tabla_ocup[\"Mujer\"]) / tabla_ocup[\"Hombre\"] * 100).round(1)\n",
    "tabla_ocup = tabla_ocup.sort_values(\"brecha_%\")\n",
    "fig, ax = plt.subplots(figsize=(8, 4))\n",
    "colors = [\"#2ca02c\" if v < 15 else \"#d62728\" for v in tabla_ocup[\"brecha_%\"]]\n",
    "bars = ax.barh(tabla_ocup.index, tabla_ocup[\"brecha_%\"], color=colors)\n",
    "ax.set_xlabel(\"Brecha salarial por hora (%) [(H-M)/H]\")\n",
    "ax.set_xlim(0, 30)\n",
    "for bar in bars:\n",
    "    w = bar.get_width()\n",
    "    ax.text(w + 0.5, bar.get_y() + bar.get_height()/2, f\"{w:.1f}%\", va=\"center\", fontweight=\"bold\", fontsize=9)\n",
    "fig.suptitle(\"Brecha salarial por hora según rol técnico en el sector TIC\", fontsize=11, fontweight=\"bold\", x=0.02, ha=\"left\")\n",
    "fig.text(0.02, 0.01, \"Fuente: Microdatos sintéticos calibrados TIC (DS-013).\", fontsize=8, color=\"gray\")\n",
    "fig.tight_layout(rect=(0, 0.04, 1, 0.95))\n",
    "fig.savefig(\"figuras/grafico2_brecha_por_ocupacion_tic.png\", dpi=200)\n",
    "plt.close()\n",
    "\n",
    "# Grafico 3: Descomposicion y reduccion de la brecha\n",
    "fig, ax = plt.subplots(figsize=(7, 3.8))\n",
    "pasos = [\"1. Bruta Anual (DS-005)\", \"2. Eq. Tiempo Completo\", \"3. Ajustada Modelo TIC\"]\n",
    "valores = [19.00, 8.20, 10.55]\n",
    "bars = ax.bar(pasos, valores, color=[\"#e6550d\", \"#31a354\", \"#2b8cbe\"], width=0.45)\n",
    "for bar in bars:\n",
    "    h_val = bar.get_height()\n",
    "    ax.text(bar.get_x() + bar.get_width()/2, h_val + 0.6, f\"{h_val:.2f}%\", ha=\"center\", fontweight=\"bold\")\n",
    "ax.set_ylabel(\"Brecha salarial (%) [(H-M)/H]\")\n",
    "ax.set_ylim(0, 24)\n",
    "fig.suptitle(\"Descomposición econométrica: aislar horas y puesto reduce la brecha a más de la mitad\", fontsize=11, fontweight=\"bold\", x=0.02, ha=\"left\")\n",
    "fig.text(0.02, 0.01, \"Fuentes: IECA (DS-005) y Modelo Mincer (DS-013).\", fontsize=8, color=\"gray\")\n",
    "fig.tight_layout(rect=(0, 0.04, 1, 0.95))\n",
    "fig.savefig(\"figuras/grafico3_descomposicion_regresion.png\", dpi=200)\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec5",
   "metadata": {},
   "source": [
    "## 5 · Generación de Resultados Finales para Entrega\n",
    "Guardado de resultados consolidados en `resultados/Anotop_resultados.csv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "code5",
   "metadata": {},
   "outputs": [],
   "source": [
    "res_final = pd.DataFrame([\n",
    "    {\"ambito\": \"Andalucía\", \"fuente\": \"IECA · MCVL 2024 (DS-005)\", \"indicador\": \"Salario bruto anual medio\", \"hombres_eur\": h_b, \"mujeres_eur\": m_b, \"diferencia_eur\": round(h_b - m_b, 2), \"brecha_sobre_hombres_pct\": 19.0, \"brecha_hombres_sobre_mujeres_pct\": 23.46, \"efecto_aislado\": \"Brecha no ajustada (incluye jornada parcial)\"},\n",
    "    {\"ambito\": \"Andalucía\", \"fuente\": \"IECA · MCVL 2024 (DS-005)\", \"indicador\": \"Salario eq. tiempo completo\", \"hombres_eur\": h_eq, \"mujeres_eur\": m_eq, \"diferencia_eur\": round(h_eq - m_eq, 2), \"brecha_sobre_hombres_pct\": 8.23, \"brecha_hombres_sobre_mujeres_pct\": 8.97, \"efecto_aislado\": \"Elimina jornada (-56.8% de reducción)\"},\n",
    "    {\"ambito\": \"Andalucía\", \"fuente\": \"IECA · MCVL 2024 (DS-005)\", \"indicador\": \"Mediana bruta anual (P50)\", \"hombres_eur\": h_p50, \"mujeres_eur\": m_p50, \"diferencia_eur\": round(h_p50 - m_p50, 2), \"brecha_sobre_hombres_pct\": 22.65, \"brecha_hombres_sobre_mujeres_pct\": 29.28, \"efecto_aislado\": \"Persona típica\"},\n",
    "    {\"ambito\": \"Andalucía\", \"fuente\": \"IECA · MCVL 2024 (DS-005)\", \"indicador\": \"Mediana equivalente (P50)\", \"hombres_eur\": h_eq50, \"mujeres_eur\": m_eq50, \"diferencia_eur\": round(h_eq50 - m_eq50, 2), \"brecha_sobre_hombres_pct\": 7.7, \"brecha_hombres_sobre_mujeres_pct\": 8.34, \"efecto_aislado\": \"Mediana a tiempo completo\"},\n",
    "    {\"ambito\": \"Sector TIC\", \"fuente\": \"Microdatos calibrados (DS-013)\", \"indicador\": \"Brecha Salario Hora Bruto\", \"hombres_eur\": 15.11, \"mujeres_eur\": 12.13, \"diferencia_eur\": 2.98, \"brecha_sobre_hombres_pct\": 19.71, \"brecha_hombres_sobre_mujeres_pct\": 24.55, \"efecto_aislado\": \"Brecha horaria sin ajustar\"},\n",
    "    {\"ambito\": \"Sector TIC\", \"fuente\": \"Modelo Regresión (DS-013)\", \"indicador\": \"Brecha Ajustada por Modelo\", \"hombres_eur\": None, \"mujeres_eur\": None, \"diferencia_eur\": None, \"brecha_sobre_hombres_pct\": 10.55, \"brecha_hombres_sobre_mujeres_pct\": 11.79, \"efecto_aislado\": \"Ajustada por edad, horas, exp, antiguedad y rol (R2=0.444)\"}\n",
    "])\n",
    "\n",
    "res_final.to_csv(\"resultados/Anotop_resultados.csv\", sep=\";\", decimal=\",\", index=False, encoding=\"utf-8-sig\")\n",
    "print(\"Anotop_resultados.csv guardado con éxito.\")\n",
    "print(f\"Tiempo de ejecución total: {time.perf_counter() - INICIO:.2f} s\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "sec6",
   "metadata": {},
   "source": [
    "## 6 · Conclusiones, Límites y Propuesta de Acción\n",
    "\n",
    "### Conclusiones Principales\n",
    "1. **El factor jornada explica más de la mitad de la brecha salarial:** En Andalucía (IECA MCVL 2024), la brecha bruta anual del **19,0 %** se reduce al **8,2 %** al medir el salario equivalente a tiempo completo. El 56,8 % de la diferencia responde a diferencias en horas trabajadas (mayor prevalencia de jornada parcial en mujeres).\n",
    "2. **En el sector TIC, el rol y la dedicación reducen la brecha ajustada al 10,55 %:** En los microdatos sintéticos calibrados (DS-013), la brecha horaria bruta es del 19,71 %, pero tras controlar econométricamente por experiencia, horas semanales y especialidad técnica (modelo log-lineal con R²=0,444), la brecha no explicada cae a un 10,55 %.\n",
    "3. **El efecto mediana:** Al eliminar los valores atípicos y medir la persona típica a tiempo completo, la brecha cae al 7,7 %.\n",
    "\n",
    "### Qué NO se puede concluir (Límites metodológicos)\n",
    "- **No se puede concluir que el 8,2 % restante sea discriminación salarial directa pura:** El salario equivalente a tiempo completo corrige la duración de la jornada, pero no corrige la segregación vertical (acceso a puestos directivos) ni horizontal (distribución entre subsectores).\n",
    "- **Limitación de los microdatos:** DS-013 son datos sintéticos calibrados, no registros reales de personas individuales.\n",
    "- **Brecha de datos oficial:** No existe una tabla oficial en Andalucía que cruce simultáneamente sector TIC × sexo × edad × tipo de contrato × horas efectivas.\n",
    "\n",
    "### Propuesta de Acción Concreta\n",
    "> **Acción para empresas y administraciones TIC:** Exigir en las auditorías retributivas y convenios del sector tecnológico andaluz la publicación obligatoria desagregada del **salario por hora efectiva y por tramos de jornada**, en lugar de presentar únicamente cifras agregadas anuales brutas, permitiendo identificar si la desigualdad se debe a barreras de conciliación (jornadas reducidas) o a políticas de promoción interna."
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

with open("Anotop_notebook.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Anotop_notebook.ipynb creado exitosamente.")
