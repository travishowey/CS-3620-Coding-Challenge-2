#Part 1
def bmi_calculator(calc_weight, calc_height):
    calc_bmi = calc_weight / (calc_height ** 2)
    return calc_bmi
weight = float(input("Enter your weight in Kilograms"))
height = float(input("Enter your height in Meters"))
bmi = bmi_calculator(weight, height)
print(bmi)

#Part 2
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You can not divide by zero")
        return 0

#Part 3
x = float(input("Enter your divident"))
y = float(input("Enter your divisor"))
quotient = divide(x, y)
print(quotient)

f=open('demo.txt', 'w')
f.write("Random data into it.")
f.close()

f=open('demo.txt', 'r')
print(f.read())
f.close()

f=open ('demo.txt', 'a')
f.write('\nadditiona ltext to the existing file on a new line')
f.close()

#Part 4
products = {"Shirt":25, "Pants":30, "Socks":15, "Beanie":20, "Shoes":120}
enter_product = input("Enter in a product")
if(enter_product in products):
    print(products.get(enter_product))
else:
    print("Product Not Found")

#Part 5
num_list = list(range(1,100))
for x in num_list:
    if x % 2 != 0:
        print(x)

