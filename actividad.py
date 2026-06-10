#funciones
def datos_productos(name, stock, price):
    print(" =================================")
    print(f"|| Nombre del producto {name}  ||")
    print(f"|| Precio del producto {price} ||")
    print(f"|| Stock del producto {stock}  ||")
    print(" =================================")

#Codigo principal
name = input("Ingrese el nombre del producto: ")
while True:
    try:
        price = int(input("Ingrese el precio del producto: "))
        if price <= 0:
            raise ValueError
        else:
            break
    except ValueError:
       print("Debe escribir numeros positivos")
while True:
    try:
       stock = int(input("Ingrese el stock del producto: "))
       if stock < 0:
           raise ValueError
       else:
        break
    except ValueError:
       print("Debe escribir numeros mayor o igual a cero")
datos_productos(name,stock,price)