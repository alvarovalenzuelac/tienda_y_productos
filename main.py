from tienda import Tienda
from producto import Producto

tienda_1 = Tienda("Doña Maria")

arroz = Producto("Arroz",2000,"Alimentos",45)
leche = Producto("leche",1200,"Lacteos",56)
mantequilla = Producto("Mantequilla",900,"Lacteos",156)
yoghurt = Producto("Yoghurt",450,"Lacteos",875)


tienda_1.add_product(arroz).add_product(leche).add_product(mantequilla).add_product(yoghurt).print_tienda()

tienda_1.sell_product(2).print_tienda()

tienda_1.inflation(5).print_tienda()

tienda_1.set_clearance("Lacteos", 10).print_tienda()

tienda_1.sell_product_id(875).print_tienda()
print(tienda_1.lista_productos)
#import pdb; pdb.set_trace()