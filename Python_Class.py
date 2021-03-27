numbers = [1,4,5,6,7,10.5,6.7]
for num in numbers:
    if num%2 == 0:
        print("{} is even".format(num))
        print("%d is even" % num)
        print(str(num) + " is even")