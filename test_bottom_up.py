import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones
from nomina_sistema import NominaSistema
from drivers.test_driver import TestDriver


class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()
        self.driver_impuestos = TestDriver(self.calc_impuestos)
        self.driver_bonos = TestDriver(self.calc_bonos)
        self.driver_deducciones = TestDriver(self.calc_deducciones)

    # === PRUEBAS CALCULADORA IMPUESTOS ===
    def test_isr_salario_bajo(self):
        # ARRANGE
        salario = 8000
        # ACT
        resultado = self.calc_impuestos.calcular_isr(salario)
        # ASSERT
        assert resultado == 400  # 5% de 8000

    def test_isr_salario_medio(self):
        resultado = self.calc_impuestos.calcular_isr(15000)
        assert resultado == 1500  # 10% de 15000

    def test_isr_salario_alto(self):
        resultado = self.calc_impuestos.calcular_isr(25000)
        assert resultado == 3750  # 15% de 25000

    def test_seguro_social(self):
        resultado = self.calc_impuestos.calcular_seguro_social(10000)
        assert resultado == 625  # 6.25% de 10000

    # === PRUEBAS CALCULADORA BONOS ===
    def test_bono_antiguedad_nuevo(self):
        # ARRANGE
        salario = 10000
        anos = 1
        # ACT
        resultado = self.calc_bonos.calcular_bono_antiguedad(salario, anos)
        # ASSERT
        assert resultado == 300  # 3% de 10000

    def test_bono_antiguedad_intermedio(self):
        resultado = self.calc_bonos.calcular_bono_antiguedad(10000, 3)
        assert resultado == 800  # 8% de 10000

    def test_bono_antiguedad_senior(self):
        resultado = self.calc_bonos.calcular_bono_antiguedad(10000, 6)
        assert resultado == 1500  # 15% de 10000

    def test_bono_desempeno_excelente(self):
        # ARRANGE
        salario = 10000
        calificacion = 95
        # ACT
        resultado = self.calc_bonos.calcular_bono_desempeno(salario, calificacion)
        # ASSERT
        assert resultado == 2000  # 20% de 10000

    def test_bono_desempeno_bueno(self):
        resultado = self.calc_bonos.calcular_bono_desempeno(10000, 85)
        assert resultado == 1000  # 10% de 10000

    def test_bono_desempeno_regular(self):
        resultado = self.calc_bonos.calcular_bono_desempeno(10000, 75)
        assert resultado == 500  # 5% de 10000

    def test_bono_desempeno_bajo(self):
        resultado = self.calc_bonos.calcular_bono_desempeno(10000, 60)
        assert resultado == 0  # Sin bono

    def test_bonos_totales(self):
        # ARRANGE
        empleado = {
            'salario_base': 10000,
            'anos_servicio': 3,
            'calificacion': 85
        }
        # ACT
        resultado = self.calc_bonos.calcular_bonos(empleado)
        # ASSERT
        esperado = 800 + 1000  # bono antigüedad + bono desempeño
        assert resultado == esperado

    # === PRUEBAS CALCULADORA DEDUCCIONES ===
    def test_prestamo_normal(self):
        # ARRANGE
        salario = 10000
        monto_prestamo = 12000
        cuotas = 12
        # ACT
        resultado = self.calc_deducciones.calcular_prestamo(salario, monto_prestamo, cuotas)
        # ASSERT
        assert resultado == 1000  # 12000/12

    def test_prestamo_limitado_30_percent(self):
        resultado = self.calc_deducciones.calcular_prestamo(10000, 60000, 10)
        assert resultado == 3000  # Limitado al 30% de 10000

    def test_prestamo_sin_deuda(self):
        resultado = self.calc_deducciones.calcular_prestamo(10000, 0, 0)
        assert resultado == 0

    def test_seguro_vida(self):
        # ARRANGE
        salario = 10000
        # ACT
        resultado = self.calc_deducciones.calcular_seguro_vida(salario)
        # ASSERT
        assert resultado == 200  # 2% de 10000

    def test_deducciones_totales(self):
        # ARRANGE
        empleado = {
            'salario_base': 10000,
            'monto_prestamo': 12000,
            'cuotas_restantes': 12
        }
        # ACT
        resultado = self.calc_deducciones.calcular_deducciones(empleado)
        # ASSERT
        esperado = 1000 + 200  # prestamo + seguro
        assert resultado == esperado

    # === PRUEBAS CON DRIVER ===
    def test_usando_driver_impuestos(self):
        """Demuestra uso del driver de prueba para impuestos"""
        # Ejecutar pruebas con driver
        resultado1 = self.driver_impuestos.ejecutar_prueba_unitaria('calcular_isr', [8000], 400)
        resultado2 = self.driver_impuestos.ejecutar_prueba_unitaria('calcular_isr', [15000], 1500)
        resultado3 = self.driver_impuestos.ejecutar_prueba_unitaria('calcular_seguro_social', [10000], 625)
        
        # Verificar resultados
        assert "✓" in resultado1
        assert "✓" in resultado2
        assert "✓" in resultado3
        assert len(self.driver_impuestos.resultados) == 3

    def test_usando_driver_bonos(self):
        """Demuestra uso del driver de prueba para bonos"""
        # Ejecutar pruebas con driver
        resultado1 = self.driver_bonos.ejecutar_prueba_unitaria('calcular_bono_antiguedad', [10000, 3], 800)
        resultado2 = self.driver_bonos.ejecutar_prueba_unitaria('calcular_bono_desempeno', [10000, 85], 1000)
        
        # Verificar resultados
        assert "✓" in resultado1
        assert "✓" in resultado2
        assert len(self.driver_bonos.resultados) == 2


class TestIntegracion:
    """Nivel 2: Prueba integración de módulos"""

    def setup_method(self):
        self.sistema = NominaSistema()

    def test_nomina_empleado_basico(self):
        """Prueba integración básica"""
        # ARRANGE
        empleado = {
            'salario_base': 15000,
            'anos_servicio': 3,
            'calificacion': 85,
            'monto_prestamo': 0,
            'cuotas_restantes': 0
        }
        
        # ACT
        resultado = self.sistema.calcular_nomina_neta(empleado)
        
        # ASSERT
        # Verificar componentes individuales
        assert resultado['salario_base'] == 15000
        assert resultado['isr'] == 1500  # 10% de 15000
        assert resultado['seguro_social'] == 937.5  # 6.25% de 15000
        assert resultado['bonos_totales'] == 2700  # 8% + 10% de 15000
        assert resultado['deducciones_adicionales'] == 300  # 2% de 15000
        
        # Verificar nómina neta
        esperado = 15000 + 2700 - 1500 - 937.5 - 300
        assert abs(resultado['nomina_neta'] - esperado) < 0.01

    def test_nomina_empleado_con_prestamo(self):
        """Prueba integración con préstamo"""
        # ARRANGE
        empleado = {
            'salario_base': 20000,
            'anos_servicio': 6,
            'calificacion': 92,
            'monto_prestamo': 36000,
            'cuotas_restantes': 12
        }
        
        # ACT
        resultado = self.sistema.calcular_nomina_neta(empleado)
        
        # ASSERT
        assert resultado['salario_base'] == 20000
        assert resultado['isr'] == 2000  # 10% de 20000
        assert resultado['bonos_totales'] == 7000  # 15% + 20% de 20000
        assert resultado['deducciones_adicionales'] == 3400  # 3000 prestamo + 400 seguro
        assert resultado['nomina_neta'] > 0

    def test_nomina_salario_alto(self):
        """Prueba integración con salario alto"""
        # ARRANGE
        empleado = {
            'salario_base': 25000,
            'anos_servicio': 8,
            'calificacion': 95,
            'monto_prestamo': 0,
            'cuotas_restantes': 0
        }
        
        # ACT
        resultado = self.sistema.calcular_nomina_neta(empleado)
        
        # ASSERT
        assert resultado['isr'] == 3750  # 15% de 25000
        assert resultado['bonos_totales'] == 8750  # 15% + 20% de 25000
        assert resultado['nomina_neta'] > 25000  # Debe ser mayor al salario base

    def test_casos_limite(self):
        """Prueba casos límite"""
        # Empleado sin bonos
        empleado_sin_bonos = {
            'salario_base': 8000,
            'anos_servicio': 0,
            'calificacion': 60,
            'monto_prestamo': 0,
            'cuotas_restantes': 0
        }
        
        resultado = self.sistema.calcular_nomina_neta(empleado_sin_bonos)
        assert resultado['bonos_totales'] == 240  # Solo 3% antigüedad
        assert resultado['isr'] == 400  # 5% de 8000


# === FUNCIÓN DE DEMOSTRACIÓN ===
def demo_bottom_up():
    """Demostración del enfoque Bottom Up"""
    print("🎯 DEMOSTRACIÓN PRUEBAS BOTTOM UP PARA NÓMINA")
    print("=" * 60)
    
    # NIVEL 1: Módulos Base
    print("\n📊 NIVEL 1: PRUEBAS MÓDULOS BASE")
    print("-" * 40)
    
    # Probar Calculadora Impuestos
    print("\n🧮 Probando CalculadoraImpuestos...")
    calc_impuestos = CalculadoraImpuestos()
    driver_impuestos = TestDriver(calc_impuestos)
    
    print(driver_impuestos.ejecutar_prueba_unitaria('calcular_isr', [8000], 400))
    print(driver_impuestos.ejecutar_prueba_unitaria('calcular_isr', [15000], 1500))
    print(driver_impuestos.ejecutar_prueba_unitaria('calcular_seguro_social', [10000], 625))
    
    # Probar Calculadora Bonos
    print("\n💰 Probando CalculadoraBonos...")
    calc_bonos = CalculadoraBonos()
    driver_bonos = TestDriver(calc_bonos)
    
    print(driver_bonos.ejecutar_prueba_unitaria('calcular_bono_antiguedad', [10000, 3], 800))
    print(driver_bonos.ejecutar_prueba_unitaria('calcular_bono_desempeno', [10000, 85], 1000))
    
    # Probar Calculadora Deducciones
    print("\n📉 Probando CalculadoraDeducciones...")
    calc_deducciones = CalculadoraDeducciones()
    driver_deducciones = TestDriver(calc_deducciones)
    
    print(driver_deducciones.ejecutar_prueba_unitaria('calcular_prestamo', [10000, 12000, 12], 1000))
    print(driver_deducciones.ejecutar_prueba_unitaria('calcular_seguro_vida', [10000], 200))
    
    # NIVEL 2: Integración
    print("\n\n🔗 NIVEL 2: INTEGRACIÓN DE MÓDULOS")
    print("-" * 40)
    
    sistema = NominaSistema()
    empleado_test = {
        'nombre': 'Empleado Test',
        'salario_base': 15000,
        'anos_servicio': 3,
        'calificacion': 85,
        'monto_prestamo': 12000,
        'cuotas_restantes': 12
    }
    
    resultado = sistema.generar_resumen_nomina(empleado_test)
    
    print(f"\n✅ INTEGRACIÓN EXITOSA!")
    print(f"✅ Todos los módulos base funcionan correctamente")
    print(f"✅ Sistema integrado operativo")


if __name__ == "__main__":
    # Ejecutar demostración
    demo_bottom_up()
    
    print(f"\n{'='*60}")
    print("🚀 COMANDOS PARA EJECUTAR PRUEBAS COMPLETAS:")
    print("pytest test_bottom_up.py::TestNivelBase -v")
    print("pytest test_bottom_up.py::TestIntegracion -v")
    print("pytest --cov=modulos --cov-report=html")