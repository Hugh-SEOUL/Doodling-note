height = float(input("input your height(cm): "))
weight = float(input("input your weight(kg): "))

height /= 100.0

BMI = weight / (height * height)

print("BMI : ",BMI)

if (BMI >= 20.0) and (BMI < 25.0):
    print("standard")
else:
    print("out of standard")
    