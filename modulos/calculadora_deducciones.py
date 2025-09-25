class CalculadoraDeducciones:
    """Módulo base para cálculo de deducciones"""
    
    def calcular_prestamo(self, salario_base, monto_prestamo, cuotas_restantes):
        """Calcula deducción por préstamo"""
        if cuotas_restantes <= 0 or monto_prestamo <= 0:
            return 0
        
        cuota_mensual = monto_prestamo / cuotas_restantes
        max_deduccion = salario_base * 0.30  # Máximo 30% del salario
        
        return min(cuota_mensual, max_deduccion)
    
    def calcular_seguro_vida(self, salario_base):
        """Calcula deducción por seguro de vida"""
        return salario_base * 0.02  # 2%
    
    def calcular_deducciones(self, empleado):
        """Calcula deducciones totales (excluyendo impuestos)"""
        salario = empleado.get('salario_base', 0)
        prestamo = empleado.get('monto_prestamo', 0)
        cuotas = empleado.get('cuotas_restantes', 0)
        
        ded_prestamo = self.calcular_prestamo(salario, prestamo, cuotas)
        ded_seguro = self.calcular_seguro_vida(salario)
        
        return ded_prestamo + ded_seguro