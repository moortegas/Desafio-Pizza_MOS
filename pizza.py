# Importa las listas de ingredientes desde el módulo ingredientes
from ingredientes import proteicos, vegetales, masas

# Define la clase Pizza, atributo tamaño predeterminado y precio unico

class Pizza():
    tamano = "Familiar"
    precio = 10000


# Método estático para validar si un elemento está en una lista de posibles elementos
# Se convierte el elemento solicitado a minúsculas para una comparación insensible a mayúsculas
    @staticmethod
    def validar_elemento(solicitado, posibles):
        return solicitado.lower() in posibles

    # Método para tomar un pedido de pizza
    def pedir(self):
        # Se solicita al usuario ingresar la proteína deseada
        self.proteicos = input(f"""\nIngrese la proteina que desea.
        Las opciones de proteinas son: 
        Vacuno
        Pollo
        Proteina Vegetal
                               
        """)
        
        # Se inicializa la lista de vegetales de la pizza
        # Se solicita al usuario ingresar los vegetales deseados
        # Se almacena el primer vegetal ingresado
        self.vegetales = []
        self.vegetales.append(input(f"""\nIngrese el vegetal que desea.
        Las opciones de vegetales son:
        Aceitunas
        Tomate
        Champiñones
                                    
        """))
        
        # Se almacena el segundo vegetal ingresado
        self.vegetales.append(input(f"""\nIngrese el segundo vegetal que desea.
        Las opciones de vegetales son:
        Aceitunas
        Tomate
        Champiñones
                                    
        """))

        # Se solicita al usuario ingresar la masa deseada
        self.tipo_masa = input(f"""\nIngrese el tipo de masa que desea.
        Las opciones de masa son: 
        Tradicioanal
        Delgada
                               
        """)
    
    # Se verifica si la pizza es válida, es decir, si los ingredientes ingresados son válidos
        valida_proteicos = self.validar_elemento(self.proteicos, proteicos)
        valida_vegetales = self.validar_elemento(self.vegetales[0], vegetales) and self.validar_elemento(self.vegetales[1], vegetales)
        valida_masas = self.validar_elemento(self.tipo_masa, masas)
        self.pizza_valida = valida_proteicos and valida_vegetales and valida_masas
        
