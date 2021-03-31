#operators +, -, *, /

firstValue = 11 #assignment operator
secondValue = 7

#comparison operator
thirdValue = (firstValue == secondValue) #isequalto
fourthValue = (firstValue > secondValue) #isgreaterthan
fifthValue = (firstValue < secondValue) #islessthan
sixthValue = (firstValue >= secondValue) #isgreaterthanorequalto
seventhValue = (firstValue <= secondValue) #islessthanorequalto

#reminder
quotient = firstValue % secondValue

print(firstValue + secondValue)
print(firstValue - secondValue)
print(firstValue * secondValue)
print(firstValue / secondValue)
print(thirdValue)
print(fourthValue)
print(fifthValue)
print(sixthValue)
print(seventhValue)
print(quotient)

#conditionals
age = 10
height = 5

if(age >= 10 and height >= 5):
    print("You can get on the ride".title())

elif(age < 10 and height < 5):
    print("Too short or Too Young")

else:
    print("Invalid Input")