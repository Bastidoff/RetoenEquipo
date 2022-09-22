def calcular():
    ancho= int(input("Digite el ancho: "))
    largo =int(input("Digite el largo: "))

    area = ancho*largo
    perimetro = largo+largo+ancho+ancho

    print(f'el area del rectangulo es {area} ')
    print(f'el perimetro del rectangulo es {perimetro} ')


calcular()
    