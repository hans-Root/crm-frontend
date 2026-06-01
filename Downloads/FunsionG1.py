# Raíz cuadrática Ecuación-lineal
# ******************************************************************************
# Desarrollado por: Hansel Batista
# Cédula: 8-1032-961
# ITSE - Programación 5 (Individual)
# ******************************************************************************

# --- FUNCIÓN 1: Par o Impar ---
def determinar_par_impar(numero):
    """
    Función que recibe un número entero y determine si es par o impar.
    """
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"
        
    print(f"Hansel Batista - El número {numero} es {resultado}")
    return resultado


# --- FUNCIÓN 2: Mayor de dos números ---
def obtener_mayor(num1, num2):
    """
    Función que recibe dos números y retorne el mayor de ellos.
    """
    if num1 > num2:
        mayor = num1
    else:
        mayor = num2
        
    print(f"Hansel Batista - Entre {num1} y {num2}, el mayor es {mayor}")
    return mayor


# --- PRUEBAS DE BUEN FUNCIONAMIENTO ---
print("--- Ejecutando Pruebas ---")
determinar_par_impar(8)
determinar_par_impar(7)
obtener_mayor(15, 42)