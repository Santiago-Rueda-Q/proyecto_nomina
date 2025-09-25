class NominaSistema:
    """Sistema integrado usando módulos ya probados"""

    def __init__(self):
        # Integrar módulos base (ya probados)
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()

    def calcular_nomina_neta(self, empleado):
        salario = empleado['salario_base']

        # Usar módulos ya validados
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)

        return salario + bonos - isr - seguro