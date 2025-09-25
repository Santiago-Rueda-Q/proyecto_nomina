from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones


class NominaSistema:
    """Sistema integrado usando módulos ya probados"""

    def __init__(self):
        # Integrar módulos base (ya probados)
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()

    def calcular_nomina_neta(self, empleado):
        """Calcula la nómina neta de un empleado"""
        salario = empleado['salario_base']

        # Usar módulos ya validados
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)
        deducciones = self.calc_deducciones.calcular_deducciones(empleado)

        nomina_neta = salario + bonos - isr - seguro - deducciones
        
        return {
            'salario_base': salario,
            'bonos_totales': bonos,
            'isr': isr,
            'seguro_social': seguro,
            'deducciones_adicionales': deducciones,
            'nomina_neta': nomina_neta
        }
    
    def generar_resumen_nomina(self, empleado):
        """Genera un resumen detallado de la nómina"""
        resultado = self.calcular_nomina_neta(empleado)
        
        print(f"\n=== RESUMEN NÓMINA - {empleado.get('nombre', 'Empleado')} ===")
        print(f"Salario Base:           ${resultado['salario_base']:,.2f}")
        print(f"Bonos Totales:          ${resultado['bonos_totales']:,.2f}")
        print(f"ISR:                   -${resultado['isr']:,.2f}")
        print(f"Seguro Social:         -${resultado['seguro_social']:,.2f}")
        print(f"Otras Deducciones:     -${resultado['deducciones_adicionales']:,.2f}")
        print(f"{'='*50}")
        print(f"NÓMINA NETA:            ${resultado['nomina_neta']:,.2f}")
        
        return resultado