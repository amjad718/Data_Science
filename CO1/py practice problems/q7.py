class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def multiply(self, other):
        real_part = (self.real * other.real) 
        # - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) 
        # + (self.imaginary * other.real)
        return ComplexNumber(real_part, imaginary_part)

real1 = float(input("Enter the real part of the first complex number: "))
imaginary1 = float(input("Enter the imaginary part of the first complex number: "))
real2 = float(input("Enter the real part of the second complex number: "))
imaginary2 = float(input("Enter the imaginary part of the second complex number: "))

complex_num1 = ComplexNumber(real1, imaginary1)
complex_num2 = ComplexNumber(real2, imaginary2)

sum_result = complex_num1.add(complex_num2)
diff_result = complex_num1.subtract(complex_num2)
product_result = complex_num1.multiply(complex_num2)

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)
