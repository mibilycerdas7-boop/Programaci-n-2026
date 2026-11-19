# Semana 8 — Nos contratan para analizar atenciones hospitalarias

## Nuestro caso

Una red de hospitales nos contrata como **analistas de datos**. Nos entrega
registros de atenciones y nos pide organizar la información para
responder preguntas sencillas sobre medicamentos, hospitales y diagnósticos.
Los nombres de medicamentos se usan solo para practicar el conteo; no son
recomendaciones médicas. Las personas y sus identificaciones también son
ficticias.

## Nuestra meta

Vamos a construir, paso a paso, un informe que nos permita responder:

- ¿Qué medicamentos aparecen en las primeras tres atenciones?
- ¿Cuántas veces se menciona cada medicamento en todos los registros?
- ¿Cómo agrupamos nombres que representan el mismo medicamento?
- ¿Cuántas atenciones corresponden a cada hospital?
- ¿Cuántas atenciones tienen cada diagnóstico?

Al final comprobaremos que los conteos tengan sentido y podremos explicar qué
representa cada cifra.

## Los datos que recibimos

La conexión preparada nos entrega `registros`, una **lista**. Cada elemento de
la lista es un **diccionario** que representa una atención. Por ejemplo, una
atención contiene claves como estas:

| Clave | Qué dato encontramos |
|---|---|
| `codigo` | Identificador del registro, por ejemplo `REG-001` |
| `hospital` | Hospital donde se registra la atención |
| `paciente_id` | Código ficticio que permite reconocer al mismo paciente |
| `paciente_nombre` | Nombre ficticio del paciente |
| `paciente_cedula` | Identificación ficticia |
| `diagnostico` | Diagnóstico asociado a esa atención |
| `medicamentos` | Lista de nombres de medicamentos de esa atención |

Usaremos los corchetes para consultar una clave, por ejemplo:

```python
registro["hospital"]
registro["diagnostico"]
registro["medicamentos"]
```

Un registro representa **una atención**. Un paciente puede aparecer en más de
una atención, y una atención puede mencionar varios medicamentos.

## Fase 1 — Mostramos y contamos tres atenciones

Usaremos `range(3)` para recorrer las posiciones `0`, `1` y `2` de la lista.
Por eso necesitamos que la fuente tenga al menos tres registros.

En cada registro mostraremos la identificación, el nombre, el diagnóstico y
la lista de medicamentos. Después recorreremos `registro["medicamentos"]` con
otro `for` y contaremos los nombres **tal como aparecen**.

Para guardar los resultados usaremos un diccionario contador:

```python
conteo_medicamentos = {}
```

Cada nombre será una clave y la cantidad de veces que aparece será su valor.
Si la clave ya existe, aumentaremos el valor; si no existe, la crearemos con
valor `1`. También aumentaremos `total_menciones` una vez por cada nombre que
recorramos.

**Nos preguntamos:** si recorremos tres atenciones, ¿por qué podemos contar
más de tres menciones de medicamentos?

## Fase 2 — Contamos los medicamentos de todas las atenciones

Ahora recorreremos todos los registros y, dentro de cada uno, todos sus
medicamentos. Para juntar diferencias de espacios exteriores y mayúsculas,
limpiaremos el nombre con:

```python
nombre = medicamento.strip().lower()
```

Luego consultaremos este diccionario de equivalencias:

```python
equivalencias = {
    "acetaminofén": "acetaminofen",
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido",
    "losartán": "losartan",
}
```

La **clave** es una variante que encontramos en los datos; el **valor** es el
nombre común bajo el que la contamos. Por ejemplo, `paracetamol` se cuenta
como `acetaminofen`. Si un nombre no aparece en el diccionario, lo contamos
con el nombre que quedó después de limpiarlo. Las tildes necesitan una regla
explícita: `lower()` no las quita.

Guardaremos los resultados en otro diccionario contador. Compararemos su suma
con `total_menciones`: agrupar nombres puede cambiar las claves y sus
cantidades, pero no el número total de menciones recorridas.

**Nos preguntamos:** ¿qué nombres se juntaron gracias a las equivalencias?
¿Cambió la cantidad total de menciones?

## Fase 3 — Contamos las atenciones por hospital

Crearemos `conteo_hospitales`, un diccionario contador. Recorreremos cada
registro y usaremos `registro["hospital"]` como clave. Cada registro aumentará
en uno el contador de su hospital.

Al final sumaremos los valores del diccionario y los compararemos con
`len(registros)`. La suma debe coincidir porque cada atención corresponde a un
hospital.

**Nos preguntamos:** ¿cuál hospital tiene más atenciones en los datos que
recibimos?

## Fase 4 — Contamos las atenciones por diagnóstico

Crearemos `conteo_enfermedades`, otro diccionario contador. En cada registro
leeremos `registro["diagnostico"]` y usaremos ese texto como clave. Si ya
aparece, aumentaremos su contador; si es la primera vez, guardaremos el valor
`1`.

La suma de los valores debe coincidir con `len(registros)`. Este conteo indica
cuántas **atenciones** tienen cada diagnóstico. No indica cuántos pacientes
distintos tienen ese diagnóstico, porque una persona podría tener más de una
atención.

**Nos preguntamos:** ¿qué diagnóstico aparece más? ¿Por qué el número de
atenciones puede ser mayor que el número de pacientes?

## Estructuras que practicamos

- Una **lista** de registros: `registros`.
- Un **diccionario** por atención: cada registro guarda datos bajo claves.
- Una **lista** de medicamentos dentro de cada registro.
- **Diccionarios contadores**: guardan una categoría como clave y su cantidad
  como valor.
- Ciclos `for` para recorrer registros y medicamentos.
- Condiciones `if` y `else` para crear una clave o aumentar su contador.
- `range(3)` para visitar las tres primeras posiciones.
- `len()` y `sum()` para comprobar cantidades.

## Antes de ejecutar

El programa importa `cargar_datos()` desde `conexion_api.py`. El docente deja
ese módulo preparado junto al archivo de análisis. La fuente pública debe
tener al menos tres atenciones para que funcione la muestra de `range(3)`.
Si la conexión falla, avisaremos al docente para revisar la fuente.
