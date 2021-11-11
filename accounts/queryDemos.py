from django.db import models
from accounts.models import Customer, Order, Product

#***(1)Returns all customers from customer table
customer = Customer.objects.all()

#(2)Returns first customer in table
FirstCustomer = Customer.objects.first()

#(3)Returns last customer in table
LastCustomer = Customer.objects.first()

#(4)Returns single customer by name
customerName = Customer.objects.get(name='Barry')

#****(5)Returns single customer by name
customerById = Customer.objects.get(id=4)

#****(6)Returns all orders related to customer (firstCustomer variable set above)
FirstCustomer.order_set.all()

#(7)****Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#(8)****Returns product from product table with value of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")

#(9)****Returns order/sort Objects by id
LeastToGreatest = Product.objects.all().order_by('id')
LeastToGreatest = Product.objects.all().order_by('-id')

#(10) Returns all products with tag of "Sports:" (Query many to many fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it is in the database?
A: Because there are many different products and this value changes contantly you would most likely not want to store the value in the database but rather just make this a function we can run each time we load the customer profile
'''

#Returns the total count for number of time of time a "Ball" was ordered by the first customer
ballOrders = FirstCustomer.order_set.filter(product__name="Ball").count()

#Returns total count for each product ordered
allOrders ={}

for order in FirstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
        
#Returns: allOrders: {'Ball': 2, 'BBQ': 1}

#RELATED SET EXAMPLE
class parentModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    
class parentModel(models.Model):
    parent = models.ForeignKey(parentModel)
    name = models.CharField(max_length=200, null=True)
    
parent = parentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()