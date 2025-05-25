class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass

# Create an object of D
d = D()
d.show()

# Print MRO
print("MRO of class D:", D.__mro__)
