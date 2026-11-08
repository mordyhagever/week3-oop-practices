from classes.tar2 import *

customer1 = Customer("Avi", "TLV")
order1 = Order(customer1, 5)
order2 = Order(customer1, 7)
print(order1.customer.city)
print(order2.customer.city)