# Informe del laboratorio · Pruebas y versionamiento

> Reemplaza **cada** `<<COMPLETAR>>` con tu respuesta. No borres los encabezados.
> Extensión esperada: 1.5 a 2 páginas. Se entrega haciendo `git push` de este archivo.

## 1. Datos del equipo

- **Equipo (gNN):** <<COMPLETAR>>
- **Repositorio (URL):** <<COMPLETAR>>

| Integrante | Carnet | Usuario de GitHub |
|------------|--------|-------------------|
| Gabriel Toyom | 1051524| getoyom |
| Gabriel Cuyan | 1360324 | DurrysCode |
| Sophia Corea | 1185324 | scoreap |
| Nery Hernandez | 1098824 | NSHERNANDEZH |
| Javier Monje | 1260524 | jemonje1 |

## 2. Evidencia

Pega la salida real de estos comandos (bloque de código):

`python -m pytest -q`
```
================================================ short test summary info ================================================
FAILED tests/test_comision.py::test_monto_exacto_100_no_paga_comision - assert 1.5 == 0
FAILED tests/test_comision.py::test_tope_maximo_de_q25[3000] - assert 30.0 == 25
FAILED tests/test_comision.py::test_tope_maximo_de_q25[10000] - assert 100.0 == 25
FAILED tests/test_comision.py::test_tope_maximo_de_q25[1000000] - assert 10000.0 == 25
FAILED tests/test_total.py::test_total_incluye_la_comision[200-203.0] - assert 197.0 == 203.0
FAILED tests/test_total.py::test_total_incluye_la_comision[500-507.5] - assert 492.5 == 507.5
================================================ 6 failed, 6 passed in 0.10s ================================================
```

`git log v1.0.0..v1.0.1 --oneline --decorate`
```
6c9a53c (tag: v1.0.1) docs(changelog): registrar versión 1.0.1
c8985e3 fix(calcular_total): Cambiar el signo
339a179 fix(calcular_comision): Incluir validación para corregir las comisiones mayores a 25
2f597ea fix (comision): Incluir el valor de 100 para excluirlo de la comision
29637cc chore(equipo1): Agregar integrante DurrysCode
```

## 3. Bitácora de defectos

| # | Pruebas que fallaban | Síntoma (mensaje del error) | Causa raíz | Corrección (qué línea cambió) | Commit | Quién |
|---|----------------------|-----------------------------|------------|-------------------------------|--------|-------|
| 1 | tests/test_comision.py| assert 1.5 == 0 | El condicional evaluaba monto < 100 en lugar de monto <= 100, cobrando comisión a exactamente Q100 | if monto <= 100: return 0.0 | fix(comision): incluir limite de 100 en tramo exento | Gabriel Toyom, Nery Hernandez |
| 2 | tests/test_comision.py | assert 30.0 == 25, assert 100.0 == 25, assert 10000.0 == 25 | No se aplicaba la restricción del tope máximo de Q25 para comisiones mayores a dicho valor | comision = min(comision, 25.0) | fix(comision): aplicar tope maximo de comision | Ruddy Cuyan |
| 3 | tests/test_total.py | assert 197.0 == 203.0, assert 492.5 == 507.5 | La función calcular_total() restaba la comisión al monto en lugar de sumarla | return round(monto + comision, 2) | fix(total): sumar comision al monto en lugar de restar | Sophia Corea, javier Monje |

**Pregunta:** al inicio había 6 pruebas fallando pero solo 3 defectos. ¿Por qué? ¿Qué diferencia hay entre *síntoma* y *causa raíz*?

<<La diferencia clave entre síntoma y causa raíz radica en su origen:
* **Síntoma:** Es la manifestación externa, observable e inmediata del problema, como el reporte de error de pytest o la aserción que falla en consola (por ejemplo, `assert 30.0 == 25` o `AssertionError`).
* **Causa raíz:** Es el error o defecto fundamental presente en el código fuente que genera dichos síntomas (por ejemplo, no aplicar la constante `TOPE_COMISION` o usar un operador de comparación incorrecto como `<` en lugar de `<=`). Corregir una sola causa raíz resuelve todos los síntomas asociados a ella.>>

## 4. Versionamiento

1. Corrigieron 3 defectos sin cambiar la interfaz pública. ¿Por qué la nueva versión es `1.0.1` y no `1.1.0` ni `2.0.0`?
   Según el Versionado Semántico (SemVer: `MAJOR.MINOR.PATCH`), un incremento en patch (el tercer dígito) se utiliza exclusivamente cuando se corrigen defectos (*bug fixes*) garantizando retrocompatibilidad y sin alterar la API pública. No es `1.1.0` (MINOR) porque no se introdujo ninguna funcionalidad nueva, ni `2.0.0` (MAJOR) porque no se rompieron contratos preexistentes ni compatibilidad hacia atrás.

2. Si agregaran la función nueva `calcular_comision_con_iva(monto)` sin tocar nada existente, ¿qué versión sería y por qué?
   Sería la versión `1.1.0`. De acuerdo con SemVer, se incrementa el valor de minor (el segundo dígito) cuando se añade una nueva funcionalidad que mantiene la compatibilidad con las versiones anteriores, permitiendo que el código cliente existente continúe funcionando con normalidad sin necesidad de cambios.

3. Si cambiaran `calcular_comision(monto)` para exigir un segundo parámetro obligatorio `moneda`, ¿qué versión sería y por qué?
   Sería la versión `2.0.0`. Se debe incrementar el valor de major (el primer dígito) cuando se introducen cambios que rompen la compatibilidad hacia atrás (*breaking changes*). Al exigir un nuevo parámetro obligatorio, cualquier llamada existente de la forma `calcular_comision(monto)` fallará con un `TypeError`, rompiendo la interfaz pública para los clientes que dependían de la versión 1.x.x.

4. Ejecuten `git diff v1.0.0 v1.0.1 --stat`. ¿Qué archivos cambiaron y por qué es útil poder comparar dos versiones?
   Cambiaron los siguientes archivos:
   - `CHANGELOG.md` (documentación de los cambios y correcciones de la versión)
   - `equipo/DurrysCode.txt` (archivo de registro de participación del equipo)
   - `src/pagofacil/comision.py` (código fuente donde se corrigieron los 3 defectos)

   Es sumamente útil comparar versiones con herramientas de Git porque permite auditar con precisión qué archivos y líneas de código exactas se modificaron entre un lanzamiento y otro. Facilita las revisiones de código (*code review*), agiliza la localización de causas raíz si surge una regresión inesperada en producción y asegura que no se hayan introducido cambios no autorizados o fuera del alcance de la entrega.

## 5. Mini duelo

Tabla de casos que diseñaron (mínimo 6 filas; indiquen la técnica):

## 5. Mini duelo

Tabla de casos que diseñaron (mínimo 6 filas; indiquen la técnica):

| Partición o límite que cubre | Entrada | Resultado esperado | Técnica |
|------------------------------|---------|--------------------|---------|
| Límite superior Tramo 1 (exento de comisión) | `monto = 100` | `0.0` | Análisis de Valores Límite (BVA) |
| Límite inferior Tramo 2 (1.5% de comisión) | `monto = 100.01` | `1.50` | Análisis de Valores Límite (BVA) |
| Límite superior Tramo 2 (1.5% de comisión) | `monto = 1000` | `15.00` | Análisis de Valores Límite (BVA) |
| Límite inferior Tramo 3 (1% de comisión) | `monto = 1000.01` | `10.00` | Análisis de Valores Límite (BVA) |
| Límite del tope máximo de comisión (Q25.00) | `monto = 3000` | `25.00` | Partición de Equivalencia |
| Partición inválida: Números menores o iguales a cero | `monto = 0`, `-1`, `-0.01` | `ValueError` | Partición de Equivalencia y Valores Límite |
| Partición inválida: Tipos no numéricos y booleanos (mutante bonus) | `monto = True`, `False`, `"50"`, `None` | `TypeError` | Partición de Equivalencia |

- **Resultado del marcador (mutantes detectados de 7):** 7 de 7 detectados.
- **¿Qué mutantes sobrevivieron (si alguno) y qué caso de prueba les habría faltado?** Ninguno. Se logró detectar el 100% de los mutantes (incluyendo el mutante bonus) gracias a la combinación de Análisis de Valores Límite (BVA) en las fronteras exactas (100, 100.01, 1000, 1000.01) y Partición de Equivalencia exhaustiva sobre entradas no válidas (especialmente probando valores booleanos como `True` y `False`, que en Python heredan de `int` y suelen pasar desapercibidos si solo se valida con `isinstance(monto, (int, float))` sin restringir tipos booleanos).

## 6. Reflexión (5 a 8 líneas)

Su suite visible quedó 100 % en verde y, aun así, el duelo puede encontrar defectos escondidos.
¿Qué implica eso para la estrategia de pruebas? Relaciónenlo con la pirámide de pruebas, con
qué conviene automatizar y con el caso Knight Capital de la clase.

<<Tener una suite visible al 100 % en verde únicamente demuestra que el código satisface los casos evaluados, no la ausencia total de defectos. En la estrategia de pruebas, esto resalta que la calidad no se mide solo por la cobertura, sino por la efectividad del diseño de casos mediante valores límite y análisis de mutaciones. En la base de la pirámide de pruebas, conviene automatizar masivamente pruebas unitarias rigurosas y rápidas para validar reglas de negocio críticas antes de subir a niveles de integración. Esto evita fallas catastróficas como la de Knight Capital, donde código defectuoso y reutilizado sin pruebas de regresión adecuadas ni salvaguardas automatizadas causó pérdidas millonarias en minutos. Automatizar bien implica desafiar activamente los supuestos del sistema y no conformarse con un reporte en verde superficial>>
