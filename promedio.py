# Script para calcular el promedio de notas en Python

def calcular_promedio(notas):
    """
    Función que recibe una lista de notas y retorna el promedio.
    """
    if not notas:
        return 0
    return sum(notas) / len(notas)

def main():
    print("========================================")
    print("   CALCULADORA DE PROMEDIO DE NOTAS     ")
    print("========================================")
    
    # Lista de notas de ejemplo
    notas = [15.5, 18.0, 12.0, 20.0, 14.5]
    
    # Calcular promedio
    promedio = calcular_promedio(notas)
    
    # Mostrar resultados
    print(f"\nNotas registradas: {notas}")
    print(f"Cantidad de notas: {len(notas)}")
    print(f"Promedio final: {promedio:.2f}")
    
    # Determinar si aprobó (nota mínima aprobatoria: 10.5)
    if promedio >= 10.5:
        print("\nEstado: ¡APROBADO! 🎉")
    else:
        print("\nEstado: DESAPROBADO ❌")

if __name__ == "__main__":
    main()