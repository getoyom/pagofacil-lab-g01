"""MINI DUELO - Parte 2 del laboratorio.

Escribe aquí tus pruebas. El docente las ejecutará contra versiones del código
con defectos escondidos ("mutantes") y contará cuántos logran detectar.

REGLAS
  1. Solo puedes importar de `pytest` y de `pagofacil.comision`.
  2. TODAS tus pruebas deben PASAR con el código correcto (el que cumple
     ESPECIFICACION.md). Si una falla con el código correcto, no puntúas.
  3. Diseña desde la especificación (caja negra): particiones y valores límite.
  4. Evita montos cuyo resultado caiga justo en medio centavo (redondeo ambiguo).
  5. Trabaja SOLO en este archivo durante el duelo.
"""
import pytest

from pagofacil.comision import calcular_comision, calcular_total, validar_monto  # noqa: F401


def test_ejemplo_monto_bajo():  # ejemplo que ya pasa; puedes borrarlo o conservarlo
    assert calcular_comision(50) == 0


# --- Tus pruebas empiezan aquí ---

@pytest.mark.parametrize(
    "monto, esperado",
    [
        (100, 0.0),
        (100.01, 1.5),
        (500, 7.5),
        (1000, 15.0),
        (1000.01, 10.0),
        (3000, 25.0),
    ],
)
def test_limites_y_tasas_de_la_comision(monto, esperado):
    assert calcular_comision(monto) == esperado


def test_comision_se_redondea_a_dos_decimales():
    assert calcular_comision(100.01) == 1.5
    assert calcular_comision(1000.01) == 10.0


def test_total_incluye_comision_y_redondea_a_dos_decimales():
    assert calcular_total(100.01) == 101.51
    assert calcular_total(3000) == 3025.0


@pytest.mark.parametrize("monto", [0, -1, -0.01])
def test_montos_no_positivos_son_invalidos(monto):
    with pytest.raises(ValueError):
        validar_monto(monto)


@pytest.mark.parametrize("monto", [None, "50", [], {}, True, False])
def test_valores_no_numereicos_son_invalidos(monto):
    with pytest.raises(TypeError):
        validar_monto(monto)


@pytest.mark.parametrize("monto", [1, 50.5, 100.01])
def test_validar_monto_devuelve_float(monto):
    assert validar_monto(monto) == float(monto)
    assert isinstance(validar_monto(monto), float)


def test_monto_cero_es_invalido():
    with pytest.raises(ValueError):
        calcular_comision(0)

