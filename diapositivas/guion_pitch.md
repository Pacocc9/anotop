# Guion del pitch · Equipo ANOTOP

**2 minutos de exposición + 1 minuto de preguntas.** Unas 290 palabras en total, a ritmo tranquilo.
Reparto propuesto: Juan abre y cierra, Nico explica los datos y Paco los hallazgos (cada uno presenta la parte del notebook de la que es responsable).

---

## Diapositiva 1 · La pregunta — Juan (20 s)

> Somos ANOTOP: Juan, Nico y Paco.
> En Andalucía, las mujeres cobran al año un **19 % menos** que los hombres.
> Nuestra pregunta es sencilla: **¿cobran menos por hora, o trabajan menos horas?**
> Importa porque cada respuesta pide una política distinta: **conciliación** en un caso, **igualdad retributiva** en el otro.

*Pausa breve antes de «¿cobran menos por hora…?». Es la frase que tiene que quedarse.*

## Diapositiva 2 · Datos y método — Nico (20 s)

> Usamos los salarios oficiales del **IECA, Muestra Continua de Vidas Laborales 2024, en Andalucía**: el salario bruto anual y el equivalente a tiempo completo.
> Medimos la brecha como **hombres menos mujeres, entre hombres**, y comprobamos en el propio código que nuestras cifras coinciden con los indicadores oficiales.
> Para el sector TIC usamos **microdatos sintéticos** —lo decimos claro— y una regresión sobre el salario por hora.

*Señalar la etiqueta naranja «Datos sintéticos» al decirlo.*

## Diapositiva 3 · Hallazgos — Paco (50 s)

> **[Señalar gráfico izquierdo]** Con el salario anual, los hombres cobran unos 21.100 euros y las mujeres 17.100: un 19 % de brecha.
> Pero si comparamos **a tiempo completo**, la brecha baja al **8,2 %**.
> Es decir, **más de la mitad de la brecha, un 57 %, viene de que las mujeres trabajan menos horas remuneradas**.
>
> **[Señalar gráfico derecho]** En el sector TIC el patrón se repite: la brecha por hora es del 19,7 %, y al tener en cuenta edad, experiencia, horas y rol baja al **10,5 %**, casi a la mitad.
>
> Pero fijaos en las barras claras: **en ningún caso llega a cero**.

*No leer todos los números del gráfico: solo 19 → 8,2 y 19,7 → 10,5.*

## Diapositiva 4 · Conclusión y acción — Juan (30 s)

> Nuestra conclusión: **más de la mitad de la brecha es jornada, pero a igual jornada sigue habiendo un 8,2 %.**
> Lo que **no** podemos decir es que ese 8,2 % sea discriminación directa, ni que la parte explicada sea neutral: trabajar menos horas también puede ser desigualdad.
> Por eso proponemos que **empresas TIC y Junta de Andalucía publiquen en sus planes de igualdad la brecha por salario/hora y por tramo de jornada**, no solo la cifra anual. Así se sabe si el problema es de conciliación o de retribución, y se actúa sobre la causa correcta.
> Gracias.

---

## Preguntas del jurado (1 min) — respuestas preparadas

**1. ¿Y esto qué implica?** — *Juan*
Que con la cifra anual no basta para decidir qué hacer. Si la mayor parte es jornada, las medidas que más reducen la brecha son de conciliación y de reducir la parcialidad no deseada; el 8,2 % restante pide auditar salarios a igual jornada.

**2. ¿Por qué esa definición de brecha y no la otra?** — *Nico*
`(H − M) / H` es la que usan el INE y Eurostat y se lee como «cuánto menos cobra una mujer por cada euro de un hombre». La otra, `H / M − 1`, también está en nuestro CSV: da un 23,5 % bruto y un 9,0 % a tiempo completo. La conclusión no cambia.

**3. ¿Y si usáis la mediana en vez de la media?** — *Nico*
Lo calculamos: con la mediana la brecha bruta es mayor, un 22,7 %, pero a tiempo completo baja al 7,7 %. El efecto jornada es incluso más fuerte para la persona típica.

**4. ¿Esto es discriminación o composición?** — *Paco*
Las dos cosas, y no podemos separarlas del todo. La jornada explica más de la mitad, pero a igual jornada queda un 8,2 %, y en el modelo TIC un 10,5 % que no explican edad, experiencia, horas ni rol. Además, «explicada» no significa «justa»: si las mujeres trabajan menos horas por cuidados, eso también es desigualdad.

**5. ¿Qué dato os habría gustado tener?** — *Paco*
Una tabla oficial que cruce sector TIC × sexo × edad × jornada en Andalucía, con horas efectivas y el motivo de la parcialidad. No existe: por eso usamos microdatos sintéticos para el sector TIC.

---

## Antes de salir

- [ ] Cronometrar una pasada completa: debe salir entre 1:50 y 2:00.
- [ ] PDF abierto en pantalla completa en el portátil.
- [ ] Cada uno sabe cuándo le toca y en qué frase pasa la palabra.
- [ ] Cifras que hay que saberse de memoria: **19,0 % → 8,2 %**, **57 %**, **19,7 % → 10,5 %**.
