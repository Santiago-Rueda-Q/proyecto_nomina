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
    
    def generar_reporte(self):
        """Genera reporte de todas las pruebas ejecutadas"""
        total = len(self.resultados)
        exitosas = sum(1 for r in self.resultados if r['exito'])
        
        print(f"\n=== REPORTE DE PRUEBAS ===")
        print(f"Total pruebas: {total}")
        print(f"Exitosas: {exitosas}")
        print(f"Fallidas: {total - exitosas}")
        
        for resultado in self.resultados:
            estado = "✓" if resultado['exito'] else "✗"
            print(f"{estado} {resultado['metodo']}: {resultado['resultado']} (esperado: {resultado['esperado']})")