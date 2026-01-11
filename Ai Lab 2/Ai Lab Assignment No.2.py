from basic import basic_calc   # import the base class

class s_calc(basic_calc):   # inherited class
    def factorial(self, n):
        if n < 0:
            return "Error!"
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def x_power_y(self):
        result = 1
        for _ in range(self.y):
            result *= self.x
        return result

    # Natural log approximation
    def ln(self):
        if self.x <= 0:
            return "Error: Natural log undefined for non-positive numbers"
        y = (self.x - 1) / (self.x + 1)
        result = 0
        for n in range(1, 50, 2):
            result += (y ** n) / n
        return 2 * result

    # Logarithm using change of base
    def log(self, base):
        if self.x <= 0 or base <= 0 or base == 1:
            return "Error: Logarithm undefined"
        ln_x = s_calc(self.x, 1).ln()
        ln_b = s_calc(base, 1).ln()
        return ln_x / ln_b


# ---------------- MAIN PROGRAM ----------------

print("----- Basic Operations -----")
class1 = basic_calc(20, 8)
print("Addition:", class1.addition())
print("Subtraction:", class1.subtraction())
print("Multiplication:", class1.multiplication())
print("Division:", class1.division())

print("\n----- Factorial -----")
a = int(input("Enter the value for factorial: "))
sub_obj = s_calc(a, 1)
print("Factorial of", a, ":", sub_obj.factorial(a))

print("\n----- X^Y -----")
x_val = int(input("Enter value of x for x^y: "))
y_val = int(input("Enter value of y for x^y: "))
power_obj = s_calc(x_val, y_val)
print(f"{x_val}^{y_val} =", power_obj.x_power_y())

print("\n----- Logarithm -----")
base = int(input("Enter the base for log: "))
num = int(input("Enter the number for log: "))
log_obj = s_calc(num, 1)
print(f"log base {base} of {num} =", log_obj.log(base))

print("\n----- Natural Log -----")
ln_val = int(input("Enter the number for natural log: "))
ln_obj = s_calc(ln_val, 1)
print(f"ln({ln_val}) =", ln_obj.ln())
