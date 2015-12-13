
name = input("Hi, what is your name? ")
mass = float(input("What is your body weight in kilograms ? "))
height = float(input("What is your height in meters ? "))
sex = input("What is your gender? ")
country = input("What country do you live in? ")
BMI = float(mass / (height*height))
BMI = float(format(BMI,'.2f'))
print("Hi {}, your BMI (Body Mass Index) is {}". format(name,BMI))

print("Here come information about your gender:")

if BMI < 18.5:
	print("You have to gain a lot of weight to be overweight")
elif 18.5 <= BMI <= 24:
	print("You are normal weight, that is good")
elif 24 < BMI <= 25:
	print("You are normal weight, but you have to be careful")
elif 25 < BMI < 30:
	print("You are overweight")
else:
	print("You are obese, get help!")

