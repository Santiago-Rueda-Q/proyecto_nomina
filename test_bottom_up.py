import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from drivers.test_driver import TestDriver

class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc = CalculadoraImpuestos()
        self.driver = TestDriver(self.calc)

    def test_isr_salario_bajo(self):
        # ARRANGE
        salario = 8000
        # ACT
        resultado = self.calc.calcular_isr(salario)
        # ASSERT
        assert resultado == 400  # 5% de 8000

    def test_isr_salario_medio(self):
        resultado = self.calc.calcular_isr(15000)
        assert resultado == 1500  # 10% de 15000

    def test_seguro_social(self):
        resultado = self.calc.calcular_seguro_social(10000)
        assert resultado == 625  # 6.25% de 10000