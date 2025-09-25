# 🎯 Proyecto Nómina - Pruebas Bottom Up

## 📋 Descripción

Implementación de pruebas Bottom Up para un sistema de nómina, iniciando por módulos base y usando drivers de prueba. Este enfoque permite validar primero los módulos más básicos antes de integrarlos en el sistema completo.

## 🔧 Recursos Necesarios

- **Python 3.8+**
- **pytest-cov** (`pip install pytest-cov`)
- **Calculadora**

## 📂 Estructura del Proyecto

```
proyecto_nomina/
├── 📁 drivers/                    # Drivers de prueba
│   ├── 🐍 __init__.py
│   └── 🐍 test_driver.py
├── 📁 modulos/                    # Módulos base (se prueban primero)
│   ├── 🐍 __init__.py
│   ├── 🐍 calculadora_bonos.py
│   ├── 🐍 calculadora_deducciones.py
│   └── 🐍 calculadora_impuestos.py
├── 🐍 nomina_sistema.py           # Sistema integrado (se prueba último)
└── 🐍 test_bottom_up.py           # Pruebas progresivas Bottom Up
```

## 🎯 Metodología Bottom Up

### **Nivel 1: Módulos Base (Atómicos)**
Se prueban primero los módulos individuales más básicos:
- `CalculadoraImpuestos`: ISR y seguro social
- `CalculadoraBonos`: Bonos por antigüedad y desempeño  
- `CalculadoraDeducciones`: Préstamos y seguro de vida

### **Nivel 2: Integración**
Una vez validados los módulos base, se integran en:
- `NominaSistema`: Sistema completo que utiliza módulos ya probados

### **Nivel 3: Casos Completos**
Pruebas exhaustivas con drivers y casos límite.

## 🚀 Comandos de Ejecución

### **Nivel 1: Probar Módulos Base**
```
py -m pytest test_bottom_up.py::TestNivelBase -v
```

**Captura de pantalla - Nivel 1:**

<img width="817" height="732" alt="image" src="https://github.com/user-attachments/assets/169ae759-f6ef-4839-8840-bc8e1fdac270" />

---

### **Nivel 2: Probar Integración**
```
py -m pytest test_bottom_up.py::TestIntegracion -v
```

**Captura de pantalla - Nivel 2:**

<img width="822" height="357" alt="image" src="https://github.com/user-attachments/assets/1f585afd-072a-4b42-85bd-0a74a361b76e" />


---

### **Ejecutar Todas las Pruebas**
```bash
py -m pytest test_bottom_up.py -v
```

**Captura de pantalla - Todas las Pruebas:**

<img width="1666" height="751" alt="image" src="https://github.com/user-attachments/assets/56d52504-a44c-4d17-9bdc-4109721b0392" />


---

### **Generar Reporte de Cobertura**
```bash
py -m pytest --cov=modulos --cov-report=html test_bottom_up.py
```

**Captura de pantalla - Cobertura:**

<img width="1611" height="491" alt="image" src="https://github.com/user-attachments/assets/f8ebffd6-193f-4cb6-adf1-4dfc91da9794" />



---

### **Demostración Interactiva**
```bash
python test_bottom_up.py
```

**Captura de pantalla - Demostración:**

<img width="690" height="798" alt="image" src="https://github.com/user-attachments/assets/4953fffa-0789-4efd-8717-cc4c59b5f0bb" />


---

## 📊 Descripción de Módulos

### **drivers/test_driver.py**
```python
class TestDriver:
    """Driver para ejecutar pruebas en módulos base"""
    
    def ejecutar_prueba_unitaria(self, metodo, parametros, esperado):
        """Ejecuta una prueba y registra resultado"""
        # Implementación con tolerancia y registro de resultados
```

### **modulos/calculadora_impuestos.py**
```python
class CalculadoraImpuestos:
    """Módulo base para cálculo de impuestos"""
    
    def calcular_isr(self, salario_base):
        """Calcula Impuesto Sobre la Renta"""
        # 5%, 10%, 15% según rangos salariales
    
    def calcular_seguro_social(self, salario_base):
        """Calcula aporte de seguro social"""
        # 6.25% del salario base
```

### **modulos/calculadora_bonos.py**
```python
class CalculadoraBonos:
    """Módulo base para cálculo de bonos"""
    
    def calcular_bono_antiguedad(self, salario_base, anos_servicio):
        """Bono por antigüedad: 3%, 8%, 15%"""
    
    def calcular_bono_desempeno(self, salario_base, calificacion):
        """Bono por desempeño: 0%, 5%, 10%, 20%"""
    
    def calcular_bonos(self, empleado):
        """Suma todos los bonos"""
```

### **modulos/calculadora_deducciones.py**
```python
class CalculadoraDeducciones:
    """Módulo base para cálculo de deducciones"""
    
    def calcular_prestamo(self, salario_base, monto_prestamo, cuotas_restantes):
        """Deducción por préstamo (máx 30% del salario)"""
    
    def calcular_seguro_vida(self, salario_base):
        """Seguro de vida: 2% del salario"""
    
    def calcular_deducciones(self, empleado):
        """Suma todas las deducciones"""
```

### **nomina_sistema.py**
```python
class NominaSistema:
    """Sistema integrado usando módulos ya probados"""
    
    def calcular_nomina_neta(self, empleado):
        """Calcula nómina completa usando módulos validados"""
        # salario + bonos - impuestos - deducciones
```

## 🧪 Tipos de Pruebas

### **TestNivelBase**
- ✅ Pruebas unitarias de cada módulo
- ✅ Casos de boundary (límites)
- ✅ Validación con drivers
- ✅ Cobertura: ISR, bonos, deducciones

### **TestIntegracion**
- ✅ Integración módulo por módulo
- ✅ Casos reales de empleados
- ✅ Validación de cálculos completos
- ✅ Casos con y sin préstamos

### **TestDriverCompleto**
- ✅ Suites automatizadas
- ✅ Batería completa de pruebas
- ✅ Reportes automáticos
- ✅ Validación exhaustiva

## 📈 Resultados Esperados

### **Cobertura de Código**
- **Módulos**: 100% de cobertura
- **Integración**: Validación completa
- **Casos límite**: Todos cubiertos

### **Métricas de Calidad**
- ✅ Todos los tests pasan
- ✅ Sin errores de importación
- ✅ Módulos independientes
- ✅ Integración exitosa

## 🔍 Ejemplo de Uso

```python
# Crear sistema de nómina
sistema = NominaSistema()

# Datos del empleado
empleado = {
    'nombre': 'Juan Pérez',
    'salario_base': 15000,
    'anos_servicio': 3,
    'calificacion': 85,
    'monto_prestamo': 12000,
    'cuotas_restantes': 12
}

# Calcular nómina
resultado = sistema.calcular_nomina_neta(empleado)

# Resultado esperado:
# {
#     'salario_base': 15000,
#     'bonos_totales': 2700,      # 8% + 10%
#     'isr': 1500,                # 10%
#     'seguro_social': 937.5,     # 6.25%
#     'deducciones_adicionales': 1300,  # préstamo + seguro
#     'nomina_neta': 13962.5
# }
```

## 🎓 Conceptos Demostrados

- **Bottom Up Testing**: Pruebas desde módulos base hacia integración
- **Test Drivers**: Automatización de pruebas unitarias
- **Tolerancia de Errores**: Manejo de decimales en cálculos
- **Cobertura de Código**: Validación exhaustiva
- **Integración Progresiva**: Construcción incremental del sistema

## 🏆 Beneficios del Enfoque Bottom Up

1. **Detección Temprana**: Errores encontrados en módulos base
2. **Confiabilidad**: Módulos probados antes de integrar
3. **Mantenibilidad**: Cambios aislados y controlados
4. **Trazabilidad**: Fallas localizadas fácilmente
5. **Reutilización**: Módulos validados reutilizables
