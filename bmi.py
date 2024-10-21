def calcualate_bmi (weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print("BMI = " + str(bmi))

    if (bmi < 18.5): print("Under Weight")
    if (bmi > 25.0): print("Over Weight")
    else: print ("Normal Weight")

calcualate_bmi(weight = 57, height = 1.73)