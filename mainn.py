import numpy as np

#para todos
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def ingresar_matriz():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz = []
    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    return matriz

# operacion de Matrices

def validar(matriz1, matriz2, ope):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    if ope == "suma" or ope =="resta":
        if filas1 == filas2 and columnas1 == columnas2:
            return True
        else:
            return False
    else:
        if columnas1 == filas2:
            return True
        else:
            return False

def sumar_y_resta(matriz1, matriz2, operacion):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    if operacion == "suma":
        for i in range(filas):
            fila = []
            for j in range(columnas):
                suma = matriz1[i][j] + matriz2[i][j]
                fila.append(suma)
            resultado.append(fila)
    else:
        for i in range(filas):
            fila = []
            for j in range(columnas):
                resta = matriz1[i][j] - matriz2[i][j]
                fila.append(resta)
            resultado.append(fila)
    return resultado

def multiplicar(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    columnas2 = len(matriz2[0])
    resultado = []
    for i in range(filas1):
        fila = []
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1):
                producto = matriz1[i][k] * matriz2[k][j]
                suma += producto
            fila.append(suma)
        resultado.append(fila)
    return resultado

def mostrar_procedimiento_op(matriz1, matriz2, resultado, operacion):
    filas_1 = len(matriz1)
    columnas1 = len(matriz1[0])
    columnas2 = len(matriz2[0])

    print("\nProcedimiento: Operación: {operacion}\n")
    print("Matriz 1:")
    mostrar_matriz(matriz1)
    print("\nMatriz 2:")
    mostrar_matriz(matriz2)
    print("\nResultado:")
    mostrar_matriz(resultado)
    print("\n Pasos:")
    if operacion == "Suma" or operacion == "Resta":
        if operacion == "Suma":
            for i in range(filas_1):
                for j in range(columnas1):
                    print(f"\n{matriz1[i][j]} {'+'} {matriz2[i][j]} = {resultado[i][j]}")
        else:
            for i in range(filas_1):
                for j in range(columnas1):
                    print(f"\n{matriz1[i][j]} {'+'} {matriz2[i][j]} = {resultado[i][j]}")
    elif operacion == "Multiplicación":
        for i in range(filas_1):
            for j in range(columnas2):
                paso = []
                for k in range(columnas1):
                    paso.append(f"{matriz1[i][k]} * {matriz2[k][j]}")
                paso_str = " + ".join(paso)
                print(f"\n{paso_str} = {resultado[i][j]}")

# matriz inversa

def calcular_inversa(matriz):
    try:
        matriz_np = np.array(matriz)
        identidad = np.eye(matriz_np.shape[0])
        extendida = np.concatenate((matriz_np, identidad), axis=1)
        for i in range(extendida.shape[0]):
            pivote = extendida[i][i]
            extendida[i] /= pivote
            for j in range(extendida.shape[0]):
                if j != i:
                    factor = extendida[j][i]
                    extendida[j] -= factor * extendida[i]
        inversa = extendida[:, matriz_np.shape[1]:]
        return inversa.tolist()
    except np.linalg.LinAlgError:
        return None

# rango de matriz

def calcular_rango(matriz):
    matriz_np = np.array(matriz)

    # Realizar la eliminación Gaussiana
    filas, columnas = matriz_np.shape
    rango = 0
    for i in range(min(filas, columnas)):
        print(f"\nEtapa {i + 1}:")
        print(f"   Matriz actual:")
        for fila in matriz_np:
            print(f"   {fila}")
        print()

        if matriz_np[i, i] == 0:
            print(f"   No se puede hacer un pivote en la fila {i + 1}.")
            continue

        print(f"   Pivote en la fila {i + 1}: {matriz_np[i, i]}")

        rango += 1
        for j in range(i + 1, filas):
            coeficiente = matriz_np[j, i] / matriz_np[i, i]
            print(f"   Fila {j + 1} -= ({coeficiente}) * Fila {i + 1}")
            matriz_np[j, i:] -= coeficiente * matriz_np[i, i:]

    return rango

def mostrar_paso_a_paso(matriz):
    print("\nProcedimiento para calcular el rango de la matriz:")
    print("1. La matriz original es:")
    for fila in matriz:
        print(f"   {fila}")

    rango = calcular_rango(matriz)

    print("\n2. Paso a paso del cálculo:")
    print(f"   El rango final de la matriz es: {rango}")

# Determinate de una matriz

def calcular_determinante(matriz):
    matriz_np = np.array(matriz)
    n = matriz_np.shape[0]
    etapas = []

    def mostrar_etapa(matriz, etapa):
        print(f"\nEtapa {etapa + 1}:")
        print("Matriz actual:")
        for fila in matriz:
            print(f"   {fila}")

    mostrar_etapa(matriz_np, -1)

    def calcular_cofactor(matriz, fila, columna):
        submatriz = np.delete(np.delete(matriz, fila, axis=0), columna, axis=1)
        print(f"Submatriz:")
        print(submatriz)
        return (-1) ** (fila + columna) * np.linalg.det(submatriz)

    for i in range(n):
        etapa = {}
        etapa["Paso"] = f"Paso {i + 1}"

        cofactores = [calcular_cofactor(matriz_np, 0, j) for j in range(n)]
        etapa["Cofactores"] = cofactores

        determinante_parcial = matriz_np[0, i] * cofactores[i]
        etapa["Determinante parcial"] = determinante_parcial

        etapas.append(etapa)
        mostrar_etapa(matriz_np, i)

    determinante = np.sum([etapa["Determinante parcial"] for etapa in etapas])
    return determinante, etapas

def mostrar_resultado(determinante, etapas):
    print("\nProcedimiento paso a paso:")
    for etapa in etapas:
        print(etapa)
    print(f"\nEl determinante de la matriz es: {determinante}")

# sarrus

def ingresar_sistema():
    sistema = []
    print("Ingrese los coeficientes y las constantes del sistema de ecuaciones:")

    for i in range(3):
        ecuacion = []
        for j in range(4):
            elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
            ecuacion.append(elemento)
        sistema.append(ecuacion)

    return sistema

def calcular_determinante_sa(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]
    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]
    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]

    determinante = a*e*i + b*f*g + c*d*h - c*e*g - a*f*h - b*d*i
    return determinante

def mostrar_resultado_sa(x, y, z):
    print("\nEl sistema de ecuaciones tiene la siguiente solución:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")

def mostrar_procedimiento(sistema):
    print("\nProcedimiento paso a paso:")
    print("1. Ingrese los coeficientes y las constantes del sistema de ecuaciones.")

    for i in range(3):
        for j in range(4):
            print(f"   Ingrese el elemento [{i+1}][{j+1}]: {sistema[i][j]}")

    print("\n2. Calcule el determinante principal del sistema de ecuaciones.")

    print("   Determinante Principal = (a*e*i) + (b*f*g) + (c*d*h) - (c*e*g) - (a*f*h) - (b*d*i)")
    print(f"                         = ({sistema[0][0]} * {sistema[1][1]} * {sistema[2][2]}) + "
          f"({sistema[0][1]} * {sistema[1][2]} * {sistema[2][0]}) + ({sistema[0][2]} * {sistema[1][0]} * {sistema[2][1]}) - "
          f"({sistema[0][2]} * {sistema[1][1]} * {sistema[2][0]}) - ({sistema[0][0]} * {sistema[1][2]} * {sistema[2][1]}) - "
          f"({sistema[0][1]} * {sistema[1][0]} * {sistema[2][2]})")

    determinante_principal = calcular_determinante_sa(sistema)

    print(f"                         = {determinante_principal}\n")

    x_coeficientes = [[sistema[0][3], sistema[0][1], sistema[0][2]],
                      [sistema[1][3], sistema[1][1], sistema[1][2]],
                      [sistema[2][3], sistema[2][1], sistema[2][2]]]

    y_coeficientes = [[sistema[0][0], sistema[0][3], sistema[0][2]],
                      [sistema[1][0], sistema[1][3], sistema[1][2]],
                      [sistema[2][0], sistema[2][3], sistema[2][2]]]

    z_coeficientes = [[sistema[0][0], sistema[0][1], sistema[0][3]],
                      [sistema[1][0], sistema[1][1], sistema[1][3]],
                      [sistema[2][0], sistema[2][1], sistema[2][3]]]

    determinante_x = calcular_determinante_sa(x_coeficientes)
    determinante_y = calcular_determinante_sa(y_coeficientes)
    determinante_z = calcular_determinante_sa(z_coeficientes)

    print("3. Calcule los determinantes de las incógnitas x, y y z.")

    print("   Determinante X = (constante_x * coeficiente_y * coeficiente_z) + "
          "(coeficiente_x * constante_y * coeficiente_z) + "
          "(coeficiente_x * coeficiente_y * constante_z) - "
          "(coeficiente_x * coeficiente_y * coeficiente_z) - "
          "(constante_x * coeficiente_y * constante_z) - "
          "(coeficiente_x * constante_y * coeficiente_z)")

    print(f"                 = ({sistema[0][3]} * {sistema[0][1]} * {sistema[0][2]}) + "
          f"({sistema[1][3]} * {sistema[1][1]} * {sistema[1][2]}) + "
          f"({sistema[2][3]} * {sistema[2][1]} * {sistema[2][2]}) - "
          f"({sistema[2][3]} * {sistema[1][1]} * {sistema[0][2]}) - "
          f"({sistema[0][3]} * {sistema[1][1]} * {sistema[2][2]}) - "
          f"({sistema[1][3]} * {sistema[2][1]} * {sistema[0][2]})")

    print(f"                 = {determinante_x}\n")

    print("   Determinante Y = (coeficiente_x * constante_y * coeficiente_z) + "
          "(constante_x * coeficiente_y * coeficiente_z) + "
          "(coeficiente_x * coeficiente_y * constante_z) - "
          "(coeficiente_x * coeficiente_y * coeficiente_z) - "
          "(coeficiente_x * constante_y * constante_z) - "
          "(constante_x * coeficiente_y * coeficiente_z)")

    print(f"                 = ({sistema[0][0]} * {sistema[0][3]} * {sistema[0][2]}) + "
          f"({sistema[1][0]} * {sistema[1][3]} * {sistema[1][2]}) + "
          f"({sistema[2][0]} * {sistema[2][3]} * {sistema[2][2]}) - "
          f"({sistema[0][0]} * {sistema[1][3]} * {sistema[2][2]}) - "
          f"({sistema[0][3]} * {sistema[1][0]} * {sistema[2][2]}) - "
          f"({sistema[1][3]} * {sistema[2][0]} * {sistema[0][2]})")

    print(f"                 = {determinante_y}\n")

    print("   Determinante Z = (coeficiente_x * coeficiente_y * constante_z) + "
          "(coeficiente_x * constante_y * coeficiente_z) + "
          "(constante_x * coeficiente_y * coeficiente_z) - "
          "(coeficiente_x * coeficiente_y * coeficiente_z) - "
          "(coeficiente_x * constante_y * coeficiente_z) - "
          "(constante_x * coeficiente_y * constante_z)")

    print(f"                 = ({sistema[0][0]} * {sistema[0][1]} * {sistema[0][3]}) + "
          f"({sistema[1][0]} * {sistema[1][1]} * {sistema[1][3]}) + "
          f"({sistema[2][0]} * {sistema[2][1]} * {sistema[2][3]}) - "
          f"({sistema[0][0]} * {sistema[1][1]} * {sistema[2][3]}) - "
          f"({sistema[0][1]} * {sistema[1][3]} * {sistema[2][0]}) - "
          f"({sistema[0][3]} * {sistema[1][1]} * {sistema[2][0]})")

    print(f"                 = {determinante_z}\n")

    print("4. Calcule las soluciones del sistema de ecuaciones.")

    x = determinante_x / determinante_principal
    y = determinante_y / determinante_principal
    z = determinante_z / determinante_principal

    print(f"   x = Determinante X / Determinante Principal")
    print(f"     = {determinante_x} / {determinante_principal}")
    print(f"     = {x}\n")

    print(f"   y = Determinante Y / Determinante Principal")
    print(f"     = {determinante_y} / {determinante_principal}")
    print(f"     = {y}\n")

    print(f"   z = Determinante Z / Determinante Principal")
    print(f"     = {determinante_z} / {determinante_principal}")
    print(f"     = {z}\n")

    mostrar_resultado_sa(x, y, z)

# markov

def ingresar_matriz_mae():
    print("Ingrese la matriz de transición:")
    n = int(input("Ingrese el número de filas: "))
    m = int(input("Ingrese el número de columnas: "))

    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = float(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)

    return matriz

def calcular_distribucion_estacionaria(matriz, estado_inicial, num_iteraciones):
    matriz_np = np.array(matriz)
    distribucion_actual = np.array(estado_inicial, ndmin=2).T
    print("\nCalculando la distribución estacionaria:")

    for i in range(num_iteraciones):
        print(f"\nIteración {i + 1}:")
        print(f"Distribución actual:\n{distribucion_actual}")

        distribucion_nueva = multiplicar(matriz_np, distribucion_actual)
        mostrar_procedimiento_op(matriz_np, distribucion_actual, distribucion_nueva, "Multiplicación")
        distribucion_actual = distribucion_nueva
    distribucion_estacionaria = distribucion_actual
    return distribucion_estacionaria

while True:
    print('MENU')
    print('1. Operaciones entre matrices.')
    print('2. Matriz Inversa.')
    print('3. Rango de una Matriz.')
    print('4. Determinante de una matriz.')
    print('5. Sistema de ecuaciones 3x3 por Sarrus.')
    print('6. Cadena de Markov.')
    print('7. Salir.')
    opcion = int(input('Ingrese la opcion deseada: '))

    if opcion == 1:
        while True:
            print("Operaciones con Matrices:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            opcion = input("Seleccione una opción: ")

            if opcion == "1" or opcion == "2" or opcion == "3":
                matriz1 = ingresar_matriz()
                matriz2 = ingresar_matriz()
                if opcion == "1":
                    if validar(matriz1, matriz2, "suma"):
                        resultado = sumar_y_resta(matriz1, matriz2, "suma")
                        mostrar_procedimiento_op(matriz1, matriz2, resultado, "Suma")
                        print("\nLa suma de las matrices es:")
                        mostrar_matriz(resultado)
                        break
                    else:
                        print("Las matrices no tienen las mismas dimensiones. La operación no es válida.")
                elif opcion == "2":
                    if validar(matriz1, matriz2, "resta"):
                        resultado = sumar_y_resta(matriz1, matriz2, "resta")
                        mostrar_procedimiento_op(matriz1, matriz2, resultado, "Resta")
                        print("\nLa resta de las matrices es:")
                        mostrar_matriz(resultado)
                        break
                    else:
                        print("Las matrices no tienen las mismas dimensiones. La operación no es válida.")
                elif opcion == "3":
                    if validar(matriz1, matriz2, "multipli"):
                        resultado = multiplicar(matriz1, matriz2)
                        mostrar_procedimiento_op(matriz1, matriz2, resultado, "Multiplicación")
                        print("\nEl producto de las matrices es:")
                        mostrar_matriz(resultado)
                        break
                    else:
                        print(
                            "El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2. La operación no es válida.")
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")

    elif opcion == 2:
        while True:
            print("Cálculo de la Matriz Inversa:")
            print("1. Ingresar una matriz")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                matriz = ingresar_matriz()
                matriz_inversa = calcular_inversa(matriz)
                fila = len(matriz)
                if matriz_inversa is not None:
                    print("\nProcedimiento paso a paso:")
                    print("Matriz original:")
                    mostrar_matriz(matriz)
                    print("\nMatriz identidad extendida:")
                    mostrar_matriz(np.concatenate((np.array(matriz), np.eye(fila)), axis=1))
                    print("\nEliminación Gaussiana:")
                    mostrar_matriz(np.array(matriz_inversa))
                    print("\nLa matriz inversa es:")
                    mostrar_matriz(matriz_inversa)
                    break
                else:
                    print("\nLa matriz no tiene inversa.")
                    break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")

    elif opcion == 3:
        while True:
            print("Cálculo del Rango de una Matriz:")
            print("1. Ingresar una matriz")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                matriz = ingresar_matriz()
                print("\nLa matriz ingresada es:")
                mostrar_matriz(matriz)
                mostrar_paso_a_paso(matriz)
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                continue

    elif opcion == 4:
        while True:
            print("\nCálculo del Determinante de una Matriz:")
            print("1. Ingresar una matriz")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                matriz = ingresar_matriz()
                print("\nLa matriz ingresada es:")
                mostrar_matriz(matriz)
                determinante, etapas = calcular_determinante(matriz)
                mostrar_resultado(determinante, etapas)
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                continue

    elif opcion == 5:
        while True:
            print("\nSistema de ecuaciones lienales por Sarrus.")
            print("1.Ingresar el sistema de ecuaciones")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                sistema = ingresar_sistema()
                mostrar_procedimiento(sistema)
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                continue

    elif opcion == 6:
        while True:
            print('1. Ingresar cadena de Markov')
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                matriz = ingresar_matriz_mae()

                print("\nMatriz de transición:")
                print(np.array(matriz))

                estado_inicial = input("Ingrese el estado inicial separado por comas: ")
                estado_inicial = [float(x.strip()) for x in estado_inicial.split(",")]
                print(estado_inicial)

                num_iteraciones = int(input("Ingrese el número de iteraciones: "))

                distribucion_estacionaria = calcular_distribucion_estacionaria(matriz, estado_inicial, num_iteraciones)

                print("\nLa distribución estacionaria es:")
                for i, probabilidad in enumerate(distribucion_estacionaria):
                    print(f"P({i}) = {probabilidad}")
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                continue

    elif opcion == 7:
        print('Programa Finalizado')
        break

    else:
        print("Opcion invalida.")
        continue
