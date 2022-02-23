'''
Enoncé :

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def find_smallest(max):
    # set a limit to 10 000 to avoid infinite loop
    # CAREFUL it's kinda long
    LIMIT_MAX = 1000000000
    PRINT = False
    list_results = []
    for a in range(1, LIMIT_MAX+1):
        if PRINT: print(a)
        for b in range(1, max+1):
            #print("a is {} and b is {} making a*b = {}".format(a, b, a*b))
            if a % b == 0:
                if b == max:
                    if PRINT: print(b)
                    list_results.append(a)
                else:
                    if PRINT: print(b)
                    continue
            else:
                break


    return list_results

result = find_smallest(20)
print(result)