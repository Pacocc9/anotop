# Datatón Tech for Good · InnoSoft 26–27

> **¿Cuánto vale tu trabajo? Y cuánto vale el de la persona de al lado.**
>
> *Los datos no son neutrales.*

Un datatón de **tres horas** para analizar la **brecha salarial por género, temporalidad y edad en el sector tecnológico andaluz**, con datos abiertos de verdad, preguntas incómodas y visualizaciones que se entiendan sin ser experta.

Actividad del **Comité de Igualdad y Sostenibilidad de InnoSoft** · ETSII, Universidad de Sevilla.

🌐 **Web:** <https://innosoft-igualdad-sostenibilidad.vercel.app/> · ✉️ **Contacto:** [dataton.innosoft@us.es](mailto:dataton.innosoft@us.es)

---

## Índice

1. [En corto](#en-corto)
2. [El reto](#el-reto)
3. [Los datos](#los-datos)
4. [Agenda del día](#agenda-del-día)
5. [Entregables](#entregables)
6. [Evaluación](#evaluación)
7. [Premios](#premios)
8. [Guía de lectura](#guía-de-lectura)
9. [Participar](#participar)
10. [Sostenibilidad: la huella de la web](#sostenibilidad-la-huella-de-la-web)
11. [Preguntas frecuentes](#preguntas-frecuentes)
12. [Fuentes, licencias y cómo citar](#fuentes-licencias-y-cómo-citar)
13. [Contacto y créditos](#contacto-y-créditos)

---

## En corto

| | |
|---|---|
| 📅 **Fecha** | Lunes 16 de noviembre de 2026 *(ver nota abajo)* |
| 🕞 **Horario** | 15:30–18:30 · entrega a las **18:15** · presentaciones de 18:15 a 18:30 |
| 📍 **Lugar** | A2.11 · ETSII (Universidad de Sevilla) |
| 👥 **Equipos** | De 1 a 3 personas (si vienes sin equipo, te emparejan en la acogida) |
| 🎓 **Nivel** | Desde cero, de verdad: no hace falta experiencia previa |
| 💻 **Qué llevar** | Portátil con Python 3 + Jupyter, o cuenta de Google Colab |
| 📊 **Datos** | 15 datasets documentados · 13.647 filas · 3.000 microdatos sintéticos · coste 0 € |
| ⏱️ **Formato** | 3 horas, 5 fases |
| 📝 **Inscripción** | <https://innosoft-igualdad-sostenibilidad.vercel.app/inscripcion> (plazas limitadas) |

### Secciones de la web

| Sección | Para qué sirve |
|---|---|
| [El reto](https://innosoft-igualdad-sostenibilidad.vercel.app/reto) | Las cuatro dimensiones, qué preguntas sí y cuáles no, preguntas semilla |
| [Datos](https://innosoft-igualdad-sostenibilidad.vercel.app/datos) | Catálogo con fichas, diccionarios, limitaciones y descargas |
| [Dashboard](https://innosoft-igualdad-sostenibilidad.vercel.app/dashboard) | Cuadro de mando interactivo: salario y edad, género, temporalidad, empleo TIC, brecha |
| [Aprende](https://innosoft-igualdad-sostenibilidad.vercel.app/aprende) | Calculadora de brecha, trampas, glosario, checklist y FAQ |
| [Participa](https://innosoft-igualdad-sostenibilidad.vercel.app/participa) | Bases, entregables, rúbrica, premios y código de conducta |
| [Fuentes](https://innosoft-igualdad-sostenibilidad.vercel.app/fuentes) | 20 fuentes oficiales verificadas y cómo citar |
| [Juego](https://innosoft-igualdad-sostenibilidad.vercel.app/juego) | Cinco preguntas rápidas para calentar antes de venir |
| [Huella](https://innosoft-igualdad-sostenibilidad.vercel.app/huella) | Cuánto consume la propia web y cómo se mide |

---

## El reto

> **La brecha no es una línea. Es un sistema.**

No se trata de dibujar la brecha más bonita, sino de entender **qué la produce, a quién golpea y qué se puede hacer** con los datos que tenemos (y con los que no tenemos). Es un reto de datos abiertos, pero sobre todo un reto de honestidad: separar lo que se puede demostrar de lo que nos gustaría demostrar.

### Las cuatro dimensiones

| Eje | Cifra de partida | Qué cuenta |
|---|---|---|
| **01 · Género** | **19,0 % → 8,2 %**<br><sub>brecha bruta vs. equivalente · Andalucía 2024</sub> | Los hombres cobran de media 21.103 € brutos al año y las mujeres 17.093 € (19,0 % sobre el salario masculino). Con el mismo tiempo trabajado, la brecha cae al 8,2 %. La diferencia entre ambas cifras no es un error: es jornada parcial, interrupciones de carrera y segregación ocupacional. |
| **02 · Edad** | **+8.300 €**<br><sub>salario equivalente entre &lt;30 y 60+ · Andalucía 2024</sub> | El salario equivalente pasa de 21.725 € (menores de 30) a 30.019 € (60 y más), pero el bruto anual se estanca a partir de los 50 por la jornada parcial y las salidas del empleo. La brecha de género se ensancha con la edad. |
| **03 · Temporalidad** | **49,8 %**<br><sub>temporalidad de 20–24 años · Andalucía 2025</sub> | A los 45–54 años baja al 13,3 %. En el sector privado, la temporalidad de las mujeres es del 19,7 % frente al 17,6 % de los hombres. La precariedad tiene edad, sexo y sector. |
| **04 · Sector TIC** | **26,6 %**<br><sub>mujeres sobre el empleo TIC andaluz · 2025</sub> | 93.000 personas ocupadas en el sector TIC andaluz: 68.300 hombres y 24.700 mujeres. En 2022, la AEAT situaba la brecha del sector (NACE J) en el 26,1 % (30.076 € vs. 22.217 €); la EAES nacional, con otra metodología, en el 12,3 %. Dos fuentes, dos verdades: aprende a leerlas. |

### La brecha de datos

> *"El dato que falta también cuenta. Y a veces cuenta más que el que está."*

**No existe una única tabla oficial que cruce sexo, edad, temporalidad y salario dentro del sector TIC andaluz.** Eso no es un fracaso del reto: es uno de sus hallazgos. Documentar qué falta, por qué falta y cómo aproximarlo es una habilidad profesional de primer nivel.

Cómo lo resuelve la organización: se usa la mejor fuente disponible para cada dimensión, se marca su ámbito y periodo, y se añade un dataset sintético calibrado (DS-013) para el modelado. **El cruce que no existe no se inventa: se declara.**

### El museo de las preguntas responsables

Estas dos listas son el filtro de calidad que usará el jurado.

| ✅ Preguntas que sí | ⚠️ Preguntas que no |
|---|---|
| Comparar salarios medios y medianos por sexo, edad y tipo de contrato en Andalucía o España. | Afirmar que la brecha es solo discriminación: hay composición, jornada y segregación. |
| Medir la tasa de temporalidad por edad, sexo, sector público/privado y provincia. | Calcular una brecha TIC andaluza con cruce de edad y contrato: esa tabla no existe. |
| Describir la estructura de edad y sexo del empleo TIC andaluz. | Comparar directamente AEAT, EAES e IECA como si midieran lo mismo. |
| Calcular dos definiciones de brecha y explicar por qué difieren. | Inferir salarios individuales reales a partir de medias agregadas. |
| Construir un modelo predictivo con microdatos sintéticos calibrados. | Usar los microdatos sintéticos para conclusiones sobre personas o empresas reales. |
| Detectar qué combinaciones de variables no publica ninguna fuente oficial. | |

### Preguntas semilla

¿No sabes por dónde empezar? Elige una, dale la vuelta y comprueba si los datos la sostienen. No hay una pregunta correcta: hay preguntas bien formuladas.

| Pregunta | Datasets sugeridos |
|---|---|
| ¿La brecha TIC es mayor o menor que la del conjunto de la economía? | DS-011 (AEAT Andalucía), DS-005 (MCVL Andalucía) y DS-014 (EAES nacional). Ojo a la metodología. |
| ¿La brecha se explica por edad o por ocupación? | DS-006 (sexo × edad nacional) y DS-013 (microdatos) para descomponer. |
| ¿Quién sostiene la temporalidad en Andalucía? | DS-008 y DS-015: edad, sexo, sector público/privado y provincia. |
| ¿Hay provincias donde la temporalidad femenina es especialmente alta? | DS-015: compara la tasa femenina con la masculina dentro de cada provincia. |
| ¿Qué pasa si uso salario bruto en vez de equivalente? | DS-004 y DS-005: calcula la brecha con ambas medidas y explica la diferencia. |
| ¿Qué combinación de variables no puedo responder y por qué? | Documenta la brecha de datos. Es una respuesta válida y muy valorada. |

---

## Los datos

**15 datasets catalogados**: 13 preparados a partir de fuentes oficiales (IECA, INE, AEAT, Seguridad Social) y 2 elaborados por el equipo organizador (DS-012, indicadores derivados, y DS-013, microdatos sintéticos). Cada uno incluye fuente original, periodo, territorio, unidad, diccionario de variables y limitaciones.

### Formato de los CSV

- Codificación **UTF-8 con BOM**
- Separador de campo **`;`**
- Decimal **`,`**
- Separador de miles **`.`** en varios ficheros (p. ej. `1.835.875,00` o `27.615,00`)
- Algunas celdas están vacías (DS-001, DS-008, DS-009, DS-010, DS-012): **no conviertas ausencias en ceros**, la rúbrica lo penaliza.
- Cada fila incluye columnas de trazabilidad (`periodo`, `territorio`, `fuente`), salvo DS-013.

### Cargar los datos con pandas

> [!IMPORTANT]
> La web sugiere `pd.read_csv("…", sep=";", decimal=",")`, pero **11 de los 15 CSV usan `.` como separador de miles**. Sin `thousands="."`, columnas como los salarios se leen como texto. Añádelo siempre: ningún fichero usa el punto como decimal, así que es seguro en todos.

```python
import pandas as pd

BASE = "https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/"

def leer(nombre: str) -> pd.DataFrame:
    return pd.read_csv(
        BASE + nombre,
        sep=";",
        decimal=",",
        thousands=".",
        encoding="utf-8-sig",  # elimina el BOM del nombre de la primera columna
    )

salario_sexo = leer("DS-005_salario_sexo_andalucia_2024.csv")
microdatos   = leer("DS-013_microdatos_sinteticos_tic.csv")
```

Brecha con las dos definiciones (DS-005):

```python
s = salario_sexo.set_index("sexo")
for col in ["salario_bruto_anual", "salario_eq_tiempo_completo"]:
    h, m = s.loc["Hombres", col], s.loc["Mujeres", col]
    print(f"{col}: (H-M)/H = {(h - m) / h:.1%} · (H/M)-1 = {h / m - 1:.1%}")
# salario_bruto_anual: (H-M)/H = 19.0% · (H/M)-1 = 23.5%
# salario_eq_tiempo_completo: (H-M)/H = 8.2% · (H/M)-1 = 9.0%
```

### Catálogo

| ID | Dataset | Fuente | Periodo | Ámbito | Filas | Ejes | Descarga |
|---|---|---|---|---|---:|---|---|
| [DS-001](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-001) | Afiliación por provincia, actividad y sexo | Seguridad Social | Sep 2026 | España · provincias | 8.484 | Empleo · Género · Territorio | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-001_afiliacion_provincia_cnae_sexo_nacional_202609.csv) |
| [DS-002](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-002) | Distribución salarial por sexo y actividad | INE · EAES | 2022 | España | 1.728 | Salario · Género · Sector | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-002_salario_cnae_sexo_nacional_2022.csv) |
| [DS-003](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-003) | Empleo TIC por edad y sexo | IECA · EPA | 2025 | Andalucía | 8 | Edad · Género · Empleo TIC | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-003_empleo_tic_edad_sexo_andalucia_2025.csv) |
| [DS-004](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-004) | Salario por edad en Andalucía | IECA · MCVL | 2024 | Andalucía | 6 | Edad · Salario | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-004_salario_edad_andalucia_2024.csv) |
| [DS-005](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-005) | Salario por sexo en Andalucía | IECA · MCVL | 2024 | Andalucía | 3 | Género · Salario | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-005_salario_sexo_andalucia_2024.csv) |
| [DS-006](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-006) | Salario por sexo y edad (nacional) | INE · EAES | 2022 | España | 33 | Edad · Género · Salario | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-006_salario_sexo_edad_nacional_2022.csv) |
| [DS-007](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-007) | Salario por tipo de contrato | INE · EAES | 2022 | España | 9 | Temporalidad · Salario · Género | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-007_salario_tipo_contrato_nacional_2022.csv) |
| [DS-008](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-008) | Temporalidad por edad y sexo ⭐ | IECA · EPA | 2025 | Andalucía | 90 | Temporalidad · Edad · Género | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-008_temporalidad_edad_sexo_andalucia_2025.csv) |
| [DS-009](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-009) | Empleo por edad, sexo y actividad | IECA · EPA | 2025 | Andalucía | 180 | Edad · Género · Sector | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-009_empleo_tic_edad_sector_andalucia_2025.csv) |
| [DS-010](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-010) | Asalariados y salarización por sector | IECA · EPA | 2025 | Andalucía | 66 | Género · Sector · Empleo | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-010_asalariados_sector_tic_andalucia_2025.csv) |
| [DS-011](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-011) | Salario TIC por sexo en Andalucía | AEAT | 2022 | Andalucía | 3 | Salario · Género · TIC | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-011_salario_sector_tic_sexo_andalucia_2022.csv) |
| [DS-012](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-012) | Indicadores de brecha salarial | Derivado (IECA, INE, AEAT) | 2022–2024 | Andalucía / España | 7 | Brecha · Género · Metodología | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-012_brecha_salarial_indicadores.csv) |
| [DS-013](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-013) | Microdatos sintéticos TIC 🧪 | Simulación calibrada | 2026 (sim.) | Andalucía (simulada) | 3.000 | Microdatos · Sintético · ML | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-013_microdatos_sinteticos_tic.csv) |
| [DS-014](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-014) | Salario TIC por sexo (nacional) | INE · EAES | 2022 | España | 3 | Salario · Género · TIC | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-014_salario_sector_tic_sexo_nacional_2022.csv) |
| [DS-015](https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-015) | Temporalidad por provincia y sexo | IECA · EPA | 2025 | Andalucía · provincias | 27 | Temporalidad · Territorio · Género | [CSV](https://innosoft-igualdad-sostenibilidad.vercel.app/data/csv/DS-015_temporalidad_provincia_sexo_andalucia_2025.csv) |

⭐ Dataset central para el eje de temporalidad. 🧪 **Sintético: no son personas reales.** No tienes que usarlos todos: empieza por una pregunta y busca los datos que puedan responderla.

### Columnas y limitaciones por dataset

<details>
<summary><b>DS-001</b> · Afiliación por provincia, actividad y sexo</summary>

Afiliación a la Seguridad Social por provincia, actividad CNAE-2009 a dos dígitos y sexo. Sirve para contextualizar el volumen de empleo y el peso de las actividades tecnológicas en cada provincia.

**Columnas:** `fecha` (AAAAMM), `provincia`, `cod_cnae`, `cnae`, `sexo`, `afiliados`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- No contiene salarios.
- Los valores protegidos (<5) del fichero municipal original se imputaron al valor central 2 para poder agregar.
- CNAE a dos dígitos: no equivale automáticamente a la definición TIC estricta.
</details>

<details>
<summary><b>DS-002</b> · Distribución salarial por sexo y actividad</summary>

Medias y percentiles salariales por sexo y secciones/divisiones CNAE-2009. Referencia nacional para comparar la brecha dentro de las actividades tecnológicas. INE, EAES 2022, tablas 8748 / 36829.

**Columnas:** `sexo`, `cnae`, `medida` (media o percentil), `salario_euros`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Resultados nacionales: no permite aislar Andalucía.
- La CNAE J (Información y comunicaciones) es más amplia que la definición TIC.
- Se aplicó *forward-fill* para propagar celdas combinadas de sexo y actividad del original.
</details>

<details>
<summary><b>DS-003</b> · Empleo TIC por edad y sexo</summary>

Personas ocupadas en el sector TIC andaluz (CNAE-2009: 261-264, 268, 465, 582, 61, 6201-6209, 631, 951) por grupo de edad y por sexo, con el peso del sector sobre el empleo total de cada grupo. IECA, EPA anual 2025, consultas 55563 y 55786.

**Columnas:** `dimension` (edad | sexo), `categoria`, `sexo`, `ocupados_miles`, `pct_sobre_ocupados`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Edad y sexo **no están cruzados**: no permiten reconstruir la distribución conjunta.
- La definición de sector TIC no coincide con la CNAE J completa.
- Medias anuales sujetas al error de muestreo de la EPA.
</details>

<details>
<summary><b>DS-004</b> · Salario por edad en Andalucía</summary>

Salario bruto anual y equivalente a tiempo completo por grupo de edad, con cuartiles y desviación típica. Permite separar el efecto de la jornada del efecto puro de la edad. IECA, MCVL 2024, consultas 20541 y 20546.

**Columnas:** `grupo_edad`, `asalariados`, `salario_bruto_anual`, `bruto_p25`, `bruto_p50`, `bruto_p75`, `bruto_desv_tipica`, `salario_eq_tiempo_completo`, `eq_p25`, `eq_p50`, `eq_p75`, `eq_desv_tipica`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- El salario bruto anual incluye personas que no trabajaron todo el año y jornadas parciales.
- El equivalente elimina el efecto de la jornada, pero no el de la composición por ocupación o sector.
- La MCVL es una muestra administrativa, no un censo.
</details>

<details>
<summary><b>DS-005</b> · Salario por sexo en Andalucía</summary>

Salario bruto anual y equivalente a tiempo completo por sexo, con cuartiles. Base para calcular la brecha con dos definiciones. IECA, MCVL 2024, consultas 20526 y 20535.

**Columnas:** `sexo`, `asalariados`, `salario_bruto_anual`, `bruto_p25`, `bruto_p50`, `bruto_p75`, `salario_eq_tiempo_completo`, `eq_p25`, `eq_p50`, `eq_p75`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- No cruza sexo y edad (para eso, DS-006, nacional).
- La brecha bruta y la equivalente miden cosas distintas.
- No debe interpretarse como discriminación pura: hay diferencias de composición.
</details>

<details>
<summary><b>DS-006</b> · Salario por sexo y edad (nacional)</summary>

Media y percentiles salariales por sexo y grupo de edad en España. Permite explorar la intersección edad-género cuando la fuente andaluza no publica ese cruce. INE, EAES 2022, tabla 36834.

**Columnas:** `sexo`, `grupo_edad`, `salario_medio`, `p10`, `p25`, `p50`, `p75`, `p90`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Ámbito nacional: no es Andalucía.
- No cruza edad con tipo de contrato.
- Los percentiles altos pueden tener mayor error de muestreo.
</details>

<details>
<summary><b>DS-007</b> · Salario por tipo de contrato</summary>

Salario medio y percentiles por sexo y tipo de contrato (indefinido/temporal). Permite estudiar si la temporalidad se asocia a menores salarios y si afecta igual a mujeres y hombres. INE, EAES 2022, tabla 36833.

**Columnas:** `sexo`, `tipo_contrato` (Total | Indefinido | Temporal), `salario_medio`, `p10`, `p25`, `p50`, `p75`, `p90`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Ámbito nacional.
- No cruza tipo de contrato con edad ni con sector.
- Contrato temporal no equivale a jornada parcial.
</details>

<details>
<summary><b>DS-008</b> · Temporalidad por edad y sexo</summary>

Asalariados indefinidos y temporales, y tasa de temporalidad, por sector público/privado, grupo de edad y sexo. Dataset central del eje de temporalidad. IECA, EPA anual 2025, consulta 28976.

**Columnas:** `sector` (Público | Privado | Total), `grupo_edad`, `sexo`, `indefinido_miles`, `temporal_miles`, `total_miles`, `tasa_temporalidad`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Mide *stock* de asalariados, no flujos de contratación.
- La tasa de temporalidad es la proporción de asalariados con contrato temporal.
- No está cruzada con actividad CNAE.
</details>

<details>
<summary><b>DS-009</b> · Empleo por edad, sexo y actividad</summary>

Personas ocupadas por sexo, grupo de edad y rama de actividad CNAE-2009, con una fila específica para Información y comunicaciones (CNAE J). Permite comparar la estructura de edad del sector TIC con el resto. IECA, EPA anual 2025, consulta 14646.

**Columnas:** `sexo`, `grupo_edad`, `codigo_actividad`, `actividad`, `ocupados_miles`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- CNAE J incluye telecomunicaciones, edición y servicios de información: no es solo desarrollo de software.
- Grupos de edad amplios (16-29, 30-44, 45-64).
- No contiene salarios.
</details>

<details>
<summary><b>DS-010</b> · Asalariados y salarización por sector</summary>

Asalariados y tasa de salarización por sexo y rama de actividad CNAE-2009. Contextualiza el peso del empleo asalariado en el sector TIC y las diferencias de género. IECA, EPA anual 2025, consulta 22865.

**Columnas:** `codigo_actividad`, `actividad`, `sexo`, `asalariados_miles`, `tasa_salarizacion`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- No contiene salarios.
- La tasa de salarización es asalariados / ocupados.
- CNAE J es más amplia que la definición TIC.
</details>

<details>
<summary><b>DS-011</b> · Salario TIC por sexo en Andalucía</summary>

Asalariados y salario medio anual en la sección J (Información y comunicaciones) de Andalucía, por sexo. Una de las pocas fuentes que permite aproximar la brecha salarial TIC andaluza. AEAT, Mercado de trabajo y pensiones 2022.

**Columnas:** `sexo`, `asalariados`, `percepciones_por_persona`, `salario_medio_anual`, `sector`, `periodo`, `territorio`, `fuente`, `url`

**Limitaciones:**
- Datos de 2022: no reflejan la evolución más reciente.
- NACE J es más amplia que la definición TIC.
- Fuente tributaria: no es directamente comparable con la EAES.
- Solo tres filas (hombres, mujeres, total): no permite cruces.
</details>

<details>
<summary><b>DS-012</b> · Indicadores de brecha salarial</summary>

Tabla comparativa de brechas calculadas con dos definiciones, (H−M)/H y (H/M−1): salario bruto, equivalente, mediana y sector TIC en Andalucía y España. Elaboración propia a partir de IECA, INE y AEAT.

**Columnas:** `indicador`, `territorio`, `periodo`, `medida`, `hombres`, `mujeres`, `brecha_sobre_hombres`, `brecha_hombres_sobre_mujeres`, `fuente`, `nota`

**Limitaciones:**
- No es una fuente primaria: es un cálculo derivado.
- Las fuentes no son directamente comparables entre sí (periodo, ámbito, metodología).
- Una brecha no demuestra por sí sola discriminación: hay que controlar la composición.
</details>

<details>
<summary><b>DS-013</b> · Microdatos sintéticos TIC 🧪</summary>

Dataset individual **simulado** de 3.000 personas trabajadoras del sector TIC andaluz, calibrado con los marginales oficiales de edad, sexo, temporalidad y salario (IECA, INE, AEAT). Diseñado para la fase de modelado y para enseñar análisis de equidad.

**Columnas:** `id`, `edad`, `grupo_edad`, `sexo`, `provincia`, `ocupacion`, `tipo_contrato`, `jornada`, `horas_semana`, `antiguedad_empresa`, `anios_experiencia`, `tamano_empresa`, `teletrabajo`, `salario_bruto_anual`, `salario_hora`, `sector`, `es_sintetico`

También disponible en JSON: <https://innosoft-igualdad-sostenibilidad.vercel.app/data/microdata_sample.json>

> [!WARNING]
> **NO son personas reales.** Úsalo para aprender metodología, no para extraer conclusiones sobre el mercado laboral real.

**Limitaciones:**
- Datos 100 % sintéticos: no describen personas ni empresas reales.
- Calibrados a marginales publicados, pero no reproducen la estructura conjunta real.
- La variable sexo es binaria porque las fuentes oficiales lo son; no agota la diversidad real.
</details>

<details>
<summary><b>DS-014</b> · Salario TIC por sexo (nacional)</summary>

Salario medio y percentiles en la sección J (Información y comunicaciones) por sexo en España. Permite comparar la brecha TIC nacional con la aproximación andaluza de la AEAT. INE, EAES 2022, tabla 36829.

**Columnas:** `sexo`, `salario_medio`, `p10`, `p25`, `p50`, `p75`, `p90`, `sector`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Ámbito nacional.
- CNAE J es más amplia que la definición TIC.
- No cruza con edad ni contrato.
</details>

<details>
<summary><b>DS-015</b> · Temporalidad por provincia y sexo</summary>

Tasa de temporalidad de las personas asalariadas en las ocho provincias andaluzas y en el total regional, por sexo. Añade la dimensión territorial. IECA, EPA anual 2025, consulta 22985.

**Columnas:** `provincia`, `sexo`, `tasa_temporalidad`, `periodo`, `territorio`, `fuente`

**Limitaciones:**
- Solo tasa de temporalidad: no incluye salarios.
- Algunas provincias tienen muestras pequeñas y mayor error.
- No está cruzada con actividad económica.
</details>

### Indicadores de referencia

Brecha calculada como (H − M) / H. Fuente: DS-012 y [dashboard](https://innosoft-igualdad-sostenibilidad.vercel.app/dashboard).

| Indicador | Ámbito | Hombres | Mujeres | Brecha | Fuente |
|---|---|---:|---:|---:|---|
| Salario bruto anual medio | Andalucía · 2024 | 21.103 € | 17.093 € | **19,0 %** | IECA · MCVL |
| Salario equivalente a tiempo completo | Andalucía · 2024 | 27.182 € | 24.945 € | **8,2 %** | IECA · MCVL |
| Mediana bruta anual | Andalucía · 2024 | 18.148 € | 14.038 € | **22,6 %** | IECA · MCVL |
| Mediana equivalente | Andalucía · 2024 | 22.189 € | 20.481 € | **7,7 %** | IECA · MCVL |
| Todas las actividades | España · 2022 | 29.382 € | 24.360 € | **17,1 %** | INE · EAES |
| Sector TIC (CNAE J) | España · 2022 | 39.135 € | 34.307 € | **12,3 %** | INE · EAES |
| Sector TIC (CNAE J) | Andalucía · 2022 | 30.076 € | 22.217 € | **26,1 %** | AEAT |

> [!CAUTION]
> Las filas **no son directamente comparables** entre sí: cambian el territorio, el periodo y la metodología. La tabla sirve para ver cuánto cambia la brecha según la decisión metodológica, no para ordenar fuentes.

Otras cifras de contexto: empleo TIC en Andalucía 93.000 personas (definición IECA) o 95.800 (CNAE J completa) · salario medio TIC 27.370 € · salario equivalente medio en Andalucía 26.123 € · temporalidad de 45–54 años 13,3 %.

### Tres ideas antes de tocar el código

- **Dos definiciones de brecha.** (H−M)/H dice qué parte del sueldo masculino falta; (H/M)−1, cuánto cobran de más los hombres. En Andalucía 2024 dan 19,0 % y 23,5 %. Usa la que uses, dilo.
- **Stock no es flujo.** La EPA mide personas asalariadas en un momento; el SEPE mide contratos firmados. Un contrato temporal de una semana pesa distinto en cada fuente.
- **Sector TIC ≠ CNAE J.** El sector TIC del IECA (CNAE 261-264, 268, 465, 582, 61, 6201-6209, 631, 951) es más estrecho que la sección J, que incluye edición, telecomunicaciones y otros servicios. No son intercambiables: si comparas, di qué definición usas.

---

## Agenda del día

Un formato pensado para que nadie se quede atrás: primero se nivelan los perfiles, después se analiza, se visualiza y se cuenta.

| Hora | Fase | Qué se hace | Duración |
|---|---|---|---|
| **15:30** | Acogida + charla verde | Bienvenida, normas y 5–10 min sobre computación verde y el coste energético de un mal análisis. Formación de equipos para quien venga sin él. | 10 min |
| **15:40** | Fase 1 · EDA | Introducción a la ciencia de datos y primera inspección guiada de los datasets. | 40 min |
| **16:20** | Fase 2 · Modelar | Formular preguntas, construir indicadores y probar un modelo o análisis predictivo. | 65 min |
| **17:25** | Fase 3 · Contar | 3–4 visualizaciones, narrativa y preparación de la presentación. | 40 min |
| **18:05** | Fase 4 · Entregar | Control de calidad y entrega del notebook, el CSV y las diapositivas en el formulario **antes de las 18:15**. | 10 min |
| **18:15** | Lo contamos | Cada equipo explica su trabajo: 2 min + 1 min de preguntas. | 15 min |

Los **premios se entregan el jueves**, después de que el jurado revise las entregas.

La primera media hora está pensada para nivelar: si ya sabes programar, puedes ayudar a tu equipo; si no, empiezas por el EDA guiado.

---

## Entregables

**Tres archivos. Nada más.** Todo se sube al [formulario de entrega](https://forms.gle/z2CNdi5BManDt7A6A) **antes de las 18:15**. La organización facilita una plantilla y las instrucciones paso a paso (README, sección 12).

| Entregable | Requisitos |
|---|---|
| 📓 **Notebook reproducible** | Un `.ipynb` o script que se ejecute de principio a fin, sin rutas absolutas ni dependencias ocultas. |
| 📄 **CSV de resultados** | Los indicadores calculados, con nombres de columna claros y unidades. |
| 🖼️ **3–4 diapositivas (PDF)** | La pregunta, el método, 3–4 gráficos y la conclusión, con el nombre del equipo. Se acompaña de un pitch de 2 minutos. |

> **Regla de oro:** si no puedes explicar tu conclusión en una frase, no la entregues. El jurado preguntará *"¿y esto qué implica?"*.

---

## Evaluación

> **No gana el gráfico más bonito.** Gana el equipo que entiende mejor el problema, lo cuenta mejor y lo ejecuta sin romper nada.

Cinco criterios, 100 puntos:

| # | Criterio | Peso | Qué se valora |
|:-:|---|:-:|---|
| 1 | **¿Funciona y está bien ordenado?** | 30 % | El código se ejecuta de principio a fin, está comentado y no depende de rutas locales. Los datos se leen con cuidado: no se convierten ausencias en ceros. |
| 2 | **¿Cuenta algo que importa?** | 25 % | Responde a una pregunta real, reconoce los límites de los datos y propone una acción concreta para una empresa, una administración o la propia universidad. |
| 3 | **¿Se entiende sin ser experta?** | 20 % | 3–4 gráficos con título, ejes, unidades y una idea clara. La presentación se sigue sin haber visto el código. |
| 4 | **¿Es eficiente?** | 15 % | Mismo resultado en menos tiempo: evita bucles innecesarios, cachea operaciones y justifica las decisiones. |
| 5 | **¿Se entrega bien?** | 10 % | Notebook reproducible, CSV de resultados y PDF de diapositivas con el nombre del equipo. A tiempo. |

### ♻️ Bonus · InnoSoft Reciclator Challenge

**+10 % extra** al equipo que logre el mismo resultado en menor tiempo de ejecución. Menos cómputo, menos energía, menos huella.

- Medición con `time`; `memory_profiler` es opcional.
- La memoria se registra como métrica complementaria, no eliminatoria.
- El código eficiente tiene premio propio, pero no compensa un análisis vacío.

---

## Premios

Presupuesto 0 €, premios modestos y honestos. No se promete un MacBook: se promete reconocimiento y, si se puede, merendar.

| Puesto | Premio |
|---|---|
| 🥇 **Primer premio** | Diploma + vale para un bocadillo sencillo en el Ñam Ñam* |
| 🥈 **Segundo premio** | Diploma + vale para un bocadillo sencillo en el Ñam Ñam* |
| 🥉 **Tercer premio** | Diploma + vale para un bocadillo sencillo en el Ñam Ñam* |
| ⭐ **Menciones** | Mejor visualización, código más eficiente y pregunta más incómoda |

\* Los vales están sujetos a disponibilidad: se confirmarán por los canales oficiales de InnoSoft.

🏆 **La entrega de premios es el jueves.** El jurado valora las entregas y las presentaciones del día y comunica el resultado entonces.

---

## Guía de lectura

> **Un número no es una historia.** Guía completa, con calculadora interactiva de brecha: <https://innosoft-igualdad-sostenibilidad.vercel.app/aprende>

### Cinco formas de equivocarse

No son errores de programación, son errores de interpretación, y son los que más cuesta detectar.

1. **Comparar peras con manzanas.** Salario anual vs. por hora, bruto vs. neto, tiempo completo vs. parcial. Comprueba que las dos cifras se miden igual.
2. **Confundir brecha con discriminación.** La brecha bruta incluye composición (edad, ocupación, sector, jornada). Los datos solos no separan segregación de discriminación.
3. **Mirar solo la media.** La media se mueve con los extremos; la mediana y los percentiles cuentan mejor qué le pasa a la persona típica. Compara siempre media y mediana.
4. **Ignorar la temporalidad.** Un contrato temporal de una semana y un indefinido a jornada completa no son el mismo empleo.
5. **No decir qué fuente usas.** IECA, INE y AEAT miden cosas distintas. Sin fuente, periodo, ámbito y definición, el número no es reproducible.

> Si no puedes explicar tu número en una frase sin mirar el código, todavía no lo entiendes.

### Checklist antes de entregar

Diez preguntas que el jurado también se hará:

- [ ] ¿He formulado una pregunta concreta antes de mirar los datos?
- [ ] ¿Sé qué fuente, periodo, territorio y unidad estoy usando?
- [ ] ¿He comprobado cuántos valores faltantes hay y cómo los trato?
- [ ] ¿He separado stock (EPA) de flujo (SEPE)?
- [ ] ¿He comparado media y mediana?
- [ ] ¿He calculado la brecha con al menos dos definiciones?
- [ ] ¿He mirado si la composición por edad/ocupación explica parte de la diferencia?
- [ ] ¿Mis gráficos tienen título, ejes, unidades y fuente?
- [ ] ¿He dicho qué no puedo concluir con estos datos?
- [ ] ¿El notebook se ejecuta de principio a fin en otra máquina?

¿Y si no sabes responder alguna? Escríbelo en la entrega. Un análisis que reconoce sus límites vale más que uno que finge certezas.

<details>
<summary><b>Glosario</b> (15 términos + InnoSoft Reciclator)</summary>

| Término | Definición |
|---|---|
| **Brecha salarial bruta** | Diferencia entre el salario medio de hombres y mujeres sin corregir por características. Andalucía 2024: 19,0 % sobre el salario masculino. |
| **Brecha equivalente a tiempo completo** | Compara lo que cobrarían dos personas si trabajaran el mismo tiempo y la misma jornada. Andalucía 2024: 8,2 %. |
| **Brecha ajustada** | Intenta aislar la discriminación controlando por ocupación, edad, educación, experiencia, sector, etc. Requiere microdatos y modelos; no es un número único. |
| **Salario bruto anual** | Retribución antes de impuestos y cotizaciones, con pagas extra y variables. Se ve afectado por periodos sin empleo y jornada parcial. |
| **Salario equivalente** | Salario normalizado por tiempo trabajado y parcialidad. Permite comparar personas que no trabajaron las mismas horas o días. |
| **Temporalidad** | Proporción de asalariados con contrato temporal sobre el total de asalariados. Es un stock, no un flujo de contratos. |
| **EPA** | Encuesta de Población Activa: encuesta trimestral a hogares sobre ocupación, paro y características laborales. En Andalucía la explota el IECA. |
| **MCVL** | Muestra Continua de Vidas Laborales: muestra administrativa de la Seguridad Social para analizar trayectorias y salarios. |
| **EAES** | Encuesta Anual de Estructura Salarial (INE): distribución de ganancias por sexo, edad, ocupación, actividad y tipo de contrato. |
| **CNAE** | Clasificación Nacional de Actividades Económicas. La sección J es Información y comunicaciones; no equivale a "sector TIC" en sentido estricto. |
| **Sector TIC (IECA)** | Agrupación específica: CNAE 261-264, 268, 465, 582, 61, 6201-6209, 631 y 951. Más estrecha que la sección J. |
| **Mediana** | Valor que deja al 50 % de la población por debajo. Menos sensible a extremos que la media. |
| **Percentil** | Valor que deja un porcentaje de la población por debajo. P25 = primer cuartil; P75 = tercero. |
| **Interseccionalidad** | Cómo se combinan varios ejes de desigualdad (género, edad, origen, discapacidad, territorio). No basta con mirar cada eje por separado. |
| **Brecha de datos** | Ausencia de datos oficiales para responder una pregunta relevante. Documentarla es parte del análisis, no un fracaso. |
| **InnoSoft Reciclator** | Métrica de eficiencia: mismo resultado con menos tiempo de ejecución y menos consumo de recursos. |
</details>

---

## Participar

### Inscripción

👉 **<https://innosoft-igualdad-sostenibilidad.vercel.app/inscripcion>**

- Dos minutos, sin experiencia previa.
- **Cada persona del equipo rellena su propio formulario** (sirve para calcular el aforo).
- Plazas limitadas por la capacidad del laboratorio. **La plaza se confirma por correo**, no al enviar el formulario.
- El formulario pide nombre, correo, titulación, curso, equipo (opcional), experiencia con ciencia de datos, necesidades de accesibilidad y alergias o dieta. Hay que aceptar el tratamiento de datos y el código de conducta.
- ¿Necesitas un cruce de datos que no está en el catálogo? Indícalo en el formulario o escribe al comité.

### Checklist de mochila

- [ ] Portátil cargado y cargador
- [ ] Python 3 + Jupyter, o cuenta de Google Colab
- [ ] Ganas de preguntar en voz alta
- [ ] Botella de agua (la sostenibilidad empieza por no generar residuos)
- [ ] Si tienes datos o enlaces que creas relevantes, tráelos

Habrá agua y un pequeño catering. Si tienes alergias o dieta especial, indícalo en la inscripción.

### Código de conducta

InnoSoft es un **espacio libre de acoso, comentarios discriminatorios, machismo y LGTBIfobia**. Cualquier persona que incumpla el código de conducta será invitada a abandonar la actividad. Si presencias o sufres una situación incómoda, habla con cualquier miembro del comité o escribe a [dataton.innosoft@us.es](mailto:dataton.innosoft@us.es). El buzón es confidencial.

### Calienta antes de venir

[**¿Sabrías detectar la brecha?**](https://innosoft-igualdad-sostenibilidad.vercel.app/juego) Cinco preguntas rápidas con datos reales. Sin registro, sin nota, sin culpa.

---

## Sostenibilidad: la huella de la web

No solo se habla de sostenibilidad: también se mide la propia.

| Métrica (home, por visita) | Valor |
|---|---|
| Peso | ~147 KB (medido sin caché, 2 nov 2026) |
| CO₂e estimado | 0,045 g |
| Energía estimada | 0,12 Wh |
| Agua de refrigeración (orientativa) | 0,21 ml |
| **100 visitas** | **4,5 g de CO₂ y 11,9 Wh** |

En serio: una visita equivale a unos 54 s de una bombilla LED de 8 W o 38 cm en coche. En broma: a 0,3 s de secador de pelo, y una foto de gato de 4 MB pesa más que la web.

**Metodología.** Peso medido con la Performance API (`transferSize` / `encodedBodySize`). Energía y carbono con el modelo Sustainable Web Design / [CO2.js](https://www.thegreenwebfoundation.org/co2-js/): 810 Wh/GB y 307 g CO₂e/GB; agua a 1,8 L/kWh. Son estimaciones de orden de magnitud, no una auditoría de ciclo de vida.

**Qué se ha aligerado.** Logo de 558 KB a 15 KB en WebP, rutas con carga diferida, datos en JSON, sin trackers, sin vídeos ni autoplay, CSS/JS minificados.

Más detalle: <https://innosoft-igualdad-sostenibilidad.vercel.app/huella>

---

## Preguntas frecuentes

<details>
<summary><b>¿Necesito saber programar o ciencia de datos?</b></summary>

No. El datatón está diseñado para mezclar perfiles. La primera fase nivela a todo el mundo y hay una guía con el código mínimo para leer los datos. Si ya sabes Python, puedes ir directo al modelado; si no, empieza por el EDA guiado.
</details>

<details>
<summary><b>¿Puedo ir solo o sola?</b></summary>

Sí. Los equipos son de 1 a 3 personas. Si vienes sin equipo, te emparejan con otras personas en la acogida según intereses y nivel.
</details>

<details>
<summary><b>¿Qué tengo que entregar?</b></summary>

Un notebook reproducible (`.ipynb`) o script, un CSV con los resultados principales y un PDF de 3–4 diapositivas. Se suben al [formulario de entrega](https://forms.gle/z2CNdi5BManDt7A6A) antes de las 18:15; la organización facilita una plantilla.
</details>

<details>
<summary><b>¿Los datos son reales?</b></summary>

Sí, salvo DS-013, que es una simulación calibrada y está marcado como sintético en cada fila (`es_sintetico = SI`). Todos los datasets indican su fuente, periodo, ámbito y limitaciones.
</details>

<details>
<summary><b>¿Por qué hay datos de España y no solo de Andalucía?</b></summary>

Porque no todas las fuentes publican el mismo cruce. Cuando una tabla andaluza no existe, se usa la mejor referencia nacional y se advierte. Detectar y documentar ese hueco también es parte del reto: se llama brecha de datos.
</details>

<details>
<summary><b>¿Cómo se calcula la brecha?</b></summary>

Depende. La definición estándar es (salario hombres − salario mujeres) / salario hombres. Otra habitual es cuánto cobran de más los hombres: (hombres / mujeres − 1). En Andalucía 2024, la brecha bruta es 19,0 % con la primera fórmula y 23,5 % con la segunda. Ninguna es "la correcta": hay que decir cuál se usa.
</details>

<details>
<summary><b>¿Hay premios?</b></summary>

Sí, modestos: diploma para los tres primeros puestos y, si es posible, un vale para un bocadillo sencillo en el Ñam Ñam. También hay menciones especiales del jurado. El presupuesto es 0 €, así que se prioriza el reconocimiento.
</details>

<details>
<summary><b>¿La fecha es definitiva?</b></summary>

La fecha propuesta es el lunes 16 de noviembre de 2026, de 15:30 a 18:30. El documento marco del comité menciona también el miércoles 18, así que la confirmación final llegará por los canales oficiales de InnoSoft.
</details>

<details>
<summary><b>¿Qué pasa con mis datos personales?</b></summary>

Solo se usan para gestionar la inscripción y la actividad. No se comparten con terceros. Puedes solicitar acceso, rectificación o supresión en [dataton.innosoft@us.es](mailto:dataton.innosoft@us.es).
</details>

---

## Fuentes, licencias y cómo citar

Todas las fuentes son públicas y se verificaron el **1 de noviembre de 2026** (acceso, contenido y reproducibilidad). Si una institución cambia una URL, el dato sigue siendo válido, pero el enlace puede necesitar actualización. Listado completo: <https://innosoft-igualdad-sostenibilidad.vercel.app/fuentes>

| Organismo | Fuente | Usada en |
|---|---|---|
| IECA | [Portal de digitalización · Mercado de trabajo](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/dega/portal-de-digitalizacion-y-sociedad-digital/mercado-de-trabajo) | DS-003 |
| IECA | [Encuesta de Población Activa (EPA)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/dega/encuesta-de-poblacion-activa-epa) | DS-008, DS-009, DS-010, DS-015 |
| IECA | [Ocupados TIC por edad (consulta 55563)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/operaciones/consulta/anual/55563?CodOper=b3_2514&codConsulta=55563) | DS-003 |
| IECA | [Ocupados TIC por sexo (consulta 55786)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/operaciones/consulta/anual/55786?CodOper=b3_2514&codConsulta=55786) | DS-003 |
| IECA | [Los salarios en Andalucía · nota divulgativa 2024](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/dega/los-salarios-en-andalucia/nota-divulgativa-2024) | DS-005 |
| IECA | [Los salarios en Andalucía · producto estadístico](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/dega/los-salarios-en-andalucia) | DS-004 |
| IECA | [Salario bruto anual por edad (consulta 20541)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/operaciones/consulta/anual/20541?CodOper=b3_2034&codConsulta=20541) | DS-004 |
| IECA | [Salario equivalente por edad (consulta 20546)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/operaciones/consulta/anual/20546?CodOper=b3_2034&codConsulta=20546) | DS-004 |
| IECA | [Temporalidad por edad, sexo y sector (consulta 28976)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/operaciones/consulta/anual/28976?CodOper=b3_65&codConsulta=28976) | DS-008 |
| IECA | [Empleo por edad, sexo y actividad (consulta 14646)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/operaciones/consulta/anual/14646?CodOper=b3_65&codConsulta=14646) | DS-009 |
| IECA | [La temporalidad en Andalucía (PDF)](https://www.juntadeandalucia.es/institutodeestadisticaycartografia/dega/sites/default/files/docs/temporalidad-andalucia.pdf) | Contexto |
| INE | [Encuesta de estructura salarial 2022](https://www.ine.es/dynt3/inebase/index.htm?padre=6712&capsel=6716) | DS-002, DS-006, DS-007, DS-014 |
| INE | [EAES 2022 · sexo y edad (tabla 36834)](https://www.ine.es/jaxiT3/Tabla.htm?t=36834&L=0) | DS-006 |
| INE | [EAES 2022 · sexo y tipo de contrato (tabla 36833)](https://www.ine.es/jaxiT3/Tabla.htm?t=36833&L=0) | DS-007 |
| INE | [EAES 2022 · sexo y actividad (tabla 36829)](https://www.ine.es/jaxiT3/Tabla.htm?t=36829&L=0) | DS-002, DS-014 |
| AEAT | [Mercado de trabajo y pensiones 2022 · NACE J · Andalucía](https://www3.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/mercado/2022/jrubik2783e5831cd43ccfedc4c9ad933209ca33a084e1.html) | DS-011 |
| Seguridad Social | [Afiliación por régimen, CNAE y sexo](https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8/EST10/EST305/c43ad8ea-fe79-4329-ac8e-e5758f3c4d7a/f83fe4aa-2dee-49c5-8317-98d105813796) | DS-001 |
| SEPE | [Estadísticas de contratos](https://www.sepe.es/HomeSepe/que-es-el-sepe/estadisticas/datos-avance/contratos.html) | Complementaria (flujos) |
| SEPE | [Catálogo de datos abiertos](https://sede.sepe.gob.es/portalSede/es/datos-abiertos/catalogo-de-datos-del-SEPE) | Complementaria |
| Eurostat | [Gender pay gap in unadjusted form](https://ec.europa.eu/eurostat/databrowser/view/sdg_05_20/default/table?lang=en) | Comparativa UE |

### Licencia

Datos abiertos con atribución. Para los datos del INE, consulta su licencia **CC BY-SA 4.0**; para el resto se aplica la normativa de reutilización de información del sector público. Conserva siempre la atribución y no presentes datos modificados como si fueran originales.

### Cómo citar un dataset

```text
InnoSoft 26–27 · Datatón Tech for Good (2026). Título del dataset [código].
Fuente: organismo. URL. Consultado el 1 de noviembre de 2026.
```

Ejemplo:

```text
InnoSoft 26–27 · Datatón Tech for Good (2026). Microdatos sintéticos TIC [DS-013].
Fuente: Elaboración propia. https://innosoft-igualdad-sostenibilidad.vercel.app/datos/DS-013
```

---

## Contacto y créditos

- ✉️ **Correo:** [dataton.innosoft@us.es](mailto:dataton.innosoft@us.es) (también para incidencias de conducta; buzón confidencial)
- 🏛️ **Lugar:** Escuela Técnica Superior de Ingeniería Informática · Universidad de Sevilla
- 🌐 **Web:** <https://innosoft-igualdad-sostenibilidad.vercel.app/>

Una actividad del **Comité de Igualdad y Sostenibilidad de InnoSoft**. Datos abiertos, pensamiento crítico y un rato incómodo mirando la brecha.

Diseño y datos de la web: Marcos Ayala · © 2026 InnoSoft · Comité de Igualdad y Sostenibilidad

---

<p align="center"><b>16 de noviembre · 15:30 · ETSII</b><br><i>Ven con una pregunta. Vete con datos.</i></p>
