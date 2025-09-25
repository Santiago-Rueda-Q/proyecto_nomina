class TestDriver:
    """Driver para ejecutar pruebas en módulos base"""

    def __init__(self, modulo):
        self.modulo = modulo
        self.resultados = []

    def ejecutar_prueba_unitaria(self, metodo, parametros, esperado):
        """Ejecuta una prueba y registra resultado"""
        resultado = getattr(self.modulo, metodo)(*parametros)
        exito = abs(resultado - esperado) < 0.01  # Tolerancia

        self.resultados.append({
            'metodo': metodo,
            'exito': exito,
            'resultado': resultado,
            'esperado': esperado
        })

        assert exito, f"Fallo: {resultado} != {esperado}"
        return f"✓ {metodo}: OK"