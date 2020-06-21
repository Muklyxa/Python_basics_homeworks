class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if not(isinstance(other, type(Complex(0, 0)))):
            other = Complex(other, 0)

        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):

        if not(isinstance(other, type(Complex(0, 0)))):
            other = Complex(other, 0)

        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i"


a = Complex(1, 5)
b = Complex(10, -10)
print(a + b)
print(a * b)
