result = 0
for j in range(1000):
    import random
    array = []
    count = 0
    test = 100
    for i in range(100):
        array.append(random.randint(1,100))
    total_cases = len(array)
    for element in array:
        if element == 10:
            count += 1
    probability = count/total_cases
    if probability > 0: #this here means that Our selected value which is between 1 and hundred occurs, which is sure shot probality as I am running the random numbers between 1 and 100, and definitely I will find any number.
        result += 1
print(result)#but here results are always indicating that in one third of the cases your element does not appear
    
