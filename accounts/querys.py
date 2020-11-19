from .models import *

#* RETURN DE TODOS LOS CLIENTES DE LA TABLA
customers = Customer.objects.all()

# RETURN DEL PRIMER CLIENTE
firstCustomer = Customer.objects.first()

# RETURN ULTIMO CLIENTE
lastCustomer = Customer.objects.last()

# RETURN CLIENTE POR NOMBRE
customerByName = Customer.objects.get(name='Pepe')

# RETURN CLIENTE POR ID
customerById = Customer.objects.get(id=4)

# RETURN DE TODAS LAS ORDENES RELACIONADAS A CLIENTES
firstCustomer.order_set.all()

# -
order = Order.objects.first() 
parentName = order.customer.name

# -
products = Product.objects.filter(category="Exterior")

# ORDENA POR ID
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 


# RETURN DE PRODUCTOS ESPECIFICADOS POR ID
productsFiltered = Product.objects.filter(tags__name="Deportes")

# REGRESA EL NUMERO TOTAL DE VECES QUE CLIENTE REALIZO EL PEDIDO DE UN PRODUCTO
ballOrders = firstCustomer.order_set.filter(product__name="Licuadora").count()

# TODAS LAS ORDENES
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

# RETURN allOrders: {'PRODUCTO': 2, 'PRODUCTO': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
# REGRESA LOS MODELOS HIJOS RELACIONADOS AL MODELO PADRE
parent.childmodel_set.all()