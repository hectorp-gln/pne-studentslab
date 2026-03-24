from ecommerce import Products, Customer

a = Products("Laptop", 3000)
b = Products("Scarf", 30)
c = Products("Chocolate", 3)

x = Customer("Hector", "hector@gmail.com")
y = Customer("Sokna", "sokna@gmail.com")

print(a.get_information())
print(b.get_information())
print(c.get_information())

x.add_to_cart("Laptop")
x.add_to_cart("Laptop")

y.add_to_cart("Scarf")
y.add_to_cart("Chocolate")

print(x.compute_total())
print(y.compute_total())
