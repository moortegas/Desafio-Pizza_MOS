# Importa la clase Pizza del módulo pizza
from pizza import Pizza

# Punto a: Imprime el tamaño y el precio predeterminado de todas las pizzas
print("Todas las pizzas tienen un tamaño {} a un valor de {} pesos.\n".format(
    Pizza.tamano, Pizza.precio
))
# Punto b: Print nuevos ingredientes
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Punto C: Crea una instancia de la clase Pizza y realiza un pedido

pizza1 = Pizza()
# print (pizza1.tamano)
pizza1.pedir()
# print(pizza1.pizza_valida)



# Punto d: Imprime los detalles de la pizza pedida, incluyendo vegetales, proteína, tipo de masa y si es válida
print(f"\n\nResumen del Pedido:\nProteicos: {pizza1.proteicos} -- Vegetales: {pizza1.vegetales} --  Tipo de Masa: {pizza1.tipo_masa} -- ¿Es una pizza válida? : {pizza1.pizza_valida}\n \n")

# Punto e: Print validación 
print("El Resultado del Pedido es: {}.\n\nSi el resultado es False = Lo sentimos su pedido no se realizó, ¡¡¡ Vuelva a intentarlo, lo queremos atender !!!.\n\nSi el resultado es True = Todo salió bien ¡¡¡ Felicidades estamos armando su pizza !!!.\n\n".format(
    pizza1.pizza_valida, pizza1.pizza_valida
))
