# Method Resolution Order (MRO) and diamond inheritance

'''
A<--B
^   ^
|   |
C<--D
'''

class A:
    def show(self):
        print("Hello from A")

class B(A):
    def show(self):
        print("Hello from B")

class C(A):
    def show(self):
        print("Hello from C")

class D(B,C):
    pass


def main():
    d : D = D()
    d.show()
    print(D.mro())

if __name__ == '__main__':
    main()
