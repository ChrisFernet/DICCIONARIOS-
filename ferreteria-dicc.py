"""

Construya un programa en python para gestionar un 
inventario de una ferreteria usando diccionarios

"""
def menu():
    print("\nMENÚ")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar productos por categoria")
    print("6. Productos con bajo stock")
    print("7. Valor total del inventario")
    print("8. Consultar todos los productos")
    print("9. Salir")


def cargar_datos(dic_inv):
   dic_inv = {
      "mart001": {
         "nombre":"Martillo de uña",
         "precio":"1500",
         "stock":25,
         "categoria":"herramienta"
      },
      "DEST002":{
         "nombre":"destorinillador plano",
         "precio":8000,
         "stock":40,
         "categoria":"herramienta"
      },
      "TALA003": {
         "nombre":"Taladro electrico",
         "precio":120000,
         "stock":8,
         "categoria":"herramienta electrica"
         
      }
   }
   return dic_inv

def consultar_producto(dinv):
   print()   

def consultar_datos(dinv):
   print("\n\n8. Mostrar todos los datos.")

   if not dinv:
    print("El inventario está vacío")   
    return
   
   print(f"{'codigo':<10} {'Nombre':<30} {'Precio':<15} {'Stock':<10} {'Categoria':<20}")
   print("-" * 90)

   for cod, prod in dinv.items():
    print(f"{cod:>10} {prod['nombre']:<30} ${prod['precio']:<15} {prod['stock']:<10} {prod['categoria']:<20}")
   print(f"\n Total de productos. {len(dinv)}")
   
def agregar_producto(dinv):
   print("\n\n. Agregar producto\n\n")

   cod = input("Código del producto")  

   if cod in dinv:
      print(f"Error. El producto con cod {cod} ya existe.")
      
      return dinv
   
   nombre = input("Nombre: ")
   precio = int(input("Precio: "))
   stock = int(input("Stock: "))
   categoria = input("Categoría: ")

   dinv[cod] = {
      "nombre": nombre,
      "precio": precio,
      "stock": stock,
      "categoría": categoria
   }
   return dinv

def main():
  inventario = {} 
  inventario = cargar_datos(inventario)
  print(inventario)  
  
  while True:
     menu()
     op = input("Opción?: ").strip()

     if op == "1":
        inventario = agregar_producto(inventario)
 
     elif op == "2":
        pass
 
     elif op == "3":
        pass
 
     elif op == "4":
        pass
 
     elif op == "5":
        pass
 
     elif op == "6":
        pass
 
     elif op == "7":
        pass
 
     elif op == "8":
        inventario = consultar_datos(inventario)
     elif op == "9":
        print("Gracias por usar el programa.")
        break
     input()
 

main()
