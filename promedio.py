# Script para calcular el promedio de notas en Python

def calcular_promedio(notas):
    """
    Función que recibe una lista de notas, filtra valores válidos (0-20) 
    y retorna el promedio final.
    """
    if not notas:
        return 0
    
    # Validar que las notas estén dentro del rango académico de 0 a 20
    notas_validas = [n for n in notas if 0 <= n <= 20]
    
    if not notas_validas:
        return 0
        
    return sum(notas_validas) / len(notas_validas)

def main():
    print("========================================")
    print("   CALCULADORA DE PROMEDIO DE NOTAS     ")
    print("========================================")
    
    # Lista de notas de ejemplo (incluye una nota no válida de prueba)
    notas = [15.5, 18.0, 12.0, 20.0, 14.5]
    
    # Calcular promedio de notas válidas
    promedio = calcular_promedio(notas)
    
    # Mostrar resultados
    print(f"\nNotas registradas: {notas}")
    print(f"Cantidad de notas evaluadas: {len(notas)}")
    print(f"Promedio final: {promedio:.2f}")
    
    # Condición de aprobación
    if promedio >= 10.5:
        print("\nEstado del estudiante: APROBADO 🎉")
    else:
        print("\nEstado del estudiante: DESAPROBADO ❌")

if __name__ == "__main__":
    main()