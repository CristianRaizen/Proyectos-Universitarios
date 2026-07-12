"""
Agregar producto.
Actualizar stock.
Buscar producto.
Eliminar producto.
Mostrar inventario.
Calcular valor total del inventario.
"""

#App para la gestion de inventarios

#Agregar producto al inventario
def agregar_producto(inventory):
    try:
        product_name = input("Ingrese el nombre del producto: ").lower()
        product_price = float(input("Ingrese el precio del producto: "))
        product_stock = int(input("Ingrese el stock del producto: "))
        # Agregar el producto al inventario
        inventory[product_name] = {"price": product_price, "stock": product_stock}
        print(f"Producto {product_name} agregado al inventario.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el precio y el stock.")

#Actualizar stock de un producto existente
def actualizar_stock(inventory):
    try:
        product_name = input("Ingrese el nombre del producto a actualizar: ").lower()
        if product_name in inventory: #revisamos que el producto exista en el inventario
            new_stock = int(input("Ingrese el nuevo stock del producto: ")) #Actualizamos el stock del producto 
            inventory[product_name]["stock"] = new_stock # Asignamos el nuevo stock al producto
            print(f"Stock del producto {product_name} actualizado a {new_stock}.")
        else:
            print(f"El producto {product_name} no se encuentra en el inventario.")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")

#Buscamos el producto
def buscar_producto(inventory):
    try:
        product_name = input("Ingrese el nombre del producto a buscar: ").lower()
        if product_name in inventory: #revisamos que el producto exista en el inventario
            print(f"Producto encontrado: {product_name}")
            print(f"Precio: {inventory[product_name]['price']}")
            print(f"Stock: {inventory[product_name]['stock']}")
        else:
            print(f"El producto {product_name} no se encuentra en el inventario.")
    except ValueError:
        print("Error: Por favor, ingrese un nombre válido para la búsqueda.")

#Eliminamos un producto
def eliminar_producto(inventory):
    try:
        product_name = input("Ingrese el nombre del producto a eliminar: ").lower()
        if product_name in inventory: #revisamos que el producto exista en el inventario
            del inventory[product_name] # Eliminamos el producto del inventario
            print(f"Producto {product_name} eliminado del inventario.") 
        else:
            print(f"El producto {product_name} no se encuentra en el inventario.")
    except ValueError:
        print("Error: Por favor, ingrese un valor válido para la eliminación del producto.")  

#Mostramos el inevntario 
def mostrar_inventario(inventory):
    if inventory: #revisamos que el inventario no este vacio
        print("\n---Inventario---")
        for product_name, details in inventory.items(): #Mostramos todo el inventario con un for 
            print(f"Producto: {product_name}")
            print(f"Precio: {details['price']}")
            print(f"Stock: {details['stock']}")
            print("-" * 20)
    else:
        print("El inventario está vacío.")
    

#Calculamos el valor total del inventario
def calcular_valor_total(inventory):
        total_value = sum(details["price"] * details["stock"] for details in inventory.values())
        print(f"Valor total del inventario: ${total_value:.2f}")

#Calculamos el valor total de un producto
def calcular_valor_producto(inventory):
    try:
        product_name = input("Ingrese el nombre del producto: ").lower()
        if product_name in inventory:
            total_product = inventory[product_name]["price"] * inventory[product_name]["stock"]
            print(f"Valor total del producto: ${total_product:.2f}")
        else:
            print(f"El producto {product_name} no se encuentra en el inventario.")
    except ValueError:
        print("Error: Por favor, ingrese un nombre válido para el cálculo del producto.")
#Interfaz de usuario
def interfaz():
    inventory = {}
    while True:
        try:
            print("\n---Bienvenido al Sistema de Inventarios---")
            print("Seleccione una opción:")
            print("1. Agregar producto")
            print("2. Actualizar stock")
            print("3. Buscar producto")
            print("4. Eliminar producto")
            print("5. Mostrar inventario")
            print("6. Calcular valor total del inventario")
            print("7. Calcular valor total de un producto")
            print("8. Salir")   
            option = int(input("Ingrese el número de la opción deseada: "))
            if option == 1:
                agregar_producto(inventory)
            elif option == 2:
                actualizar_stock(inventory)
            elif option == 3:
                buscar_producto(inventory)
            elif option == 4:
                eliminar_producto(inventory)
            elif option == 5:
                mostrar_inventario(inventory)
            elif option == 6:
                calcular_valor_total(inventory)
            elif option == 7:
                calcular_valor_producto(inventory)
            elif option == 8:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")
        except ValueError:
                print("Error: Debe ingresar un número valido entre 1 y 8.")    
    
interfaz()
