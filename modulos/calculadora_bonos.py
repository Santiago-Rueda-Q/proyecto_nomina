class CalculadoraBonos:
    """Módulo base para cálculo de bonos"""
    
    def calcular_bono_antiguedad(self, salario_base, anos_servicio):
        """Calcula bono por antigüedad"""
        if anos_servicio >= 5:
            return salario_base * 0.15  
        elif anos_servicio >= 2:
            return salario_base * 0.08  
        else:
            return salario_base * 0.03  

    def calcular_bono_desempeno(self, salario_base, calificacion):
        """Calcula bono por desempeño"""
        if calificacion >= 90:
            return salario_base * 0.20  
        elif calificacion >= 80:
            return salario_base * 0.10  
        elif calificacion >= 70:
            return salario_base * 0.05 
        else:
            return 0

    def calcular_bonos(self, empleado):
        """Calcula bonos totales"""
        salario = empleado.get('salario_base', 0)
        anos = empleado.get('anos_servicio', 0)
        calificacion = empleado.get('calificacion', 0)
        
        bono_antiguedad = self.calcular_bono_antiguedad(salario, anos)
        bono_desempeno = self.calcular_bono_desempeno(salario, calificacion)
        
        return bono_antiguedad + bono_desempeno