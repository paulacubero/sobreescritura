#crea una clase llamada Producto
class Producto():
    def __init__(self, nombre, unidades, precio): #nombre, unidades y precio
        self.nombre=nombre
        self.unidaddes=unidades
        self.precio=precio
    def info(self):
        print(f'El nombre del producto es: {self.nombre}') #muestra el nombre de producto por consola
    def infoProducto(self):
        print(f'El nombre del producto es: {self.nombre} hay {self.unidaddes} unidades y su precio por unidad es {self.precio} U * P : {self.unidaddes * self.precio}')#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

producto1=Producto('camisa', 10, 9.95 ) #creas un producto camisa, 10, 9.95 de precio
producto1.infoProducto()

#práctica de sobreescritura.

#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Servicio():
    def consultarDetalle(self):
        print('el servicio es básico')

class Estandar(Servicio):
    def consultarDetalle(self):
        print('el servicio es estandar')

class Premium(Servicio):
    def consultarDetalle(self):
        print('el servicio es premium')

x=input('que servicio quieres?')
match x:
    case 'estandar':
        servicio=Estandar()
        servicio.consultarDetalle()
    case 'premium':
        servicio = Premium()
        servicio.consultarDetalle()
    case _:
        print('no tenemos ese servicio')


