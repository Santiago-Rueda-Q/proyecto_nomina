class CalculadoraImpuestos:
    """Módulo base para cálculo de impuestos"""

    def calcular_isr(self, salario_base):
        """Calcula Impuesto Sobre la Renta"""
        if salario_base <= 10000:
            return salario_base * 0.05  # 5%
        elif salario_base <= 20000:
            return salario_base * 0.10  # 10%
        else:
            return salario_base * 0.15  # 15%

    def calcular_seguro_social(self, salario_base):
        """Calcula aporte de seguro social"""
        return salario_base * 0.0625  # 6.25%