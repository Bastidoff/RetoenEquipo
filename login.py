""" -Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
 """

def login():
    admin = False
    intentos = 0
    while admin == False:
        intentos += 1
        user = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")
        if(user == 'admim' and password == 'admin123'):
            admin = True
        else: 
            print('Usuario o contraseña no valida')
            
    print(admin)
    print(f"El numero de intentos fue {intentos}")      

login()  
    


