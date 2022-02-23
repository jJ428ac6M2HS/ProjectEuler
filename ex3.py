'''
Enoncé :

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''

def return_prime_factors(number):
    results = []
    # start at 2 to avoid 0 and 1, number is not checked which is good
    while(number != 1):
        factor = seek_prime_factor(number)
        results.append(factor)
        number = int(number/factor)
    print(results)
    results = list(set(results))
    results.sort()
    return results

def seek_prime_factor(number):
    # we want number to be checked to end the loop, so +1
    for i in range(2, number+1):
        if (number/i).is_integer():
            return i



print(return_prime_factors(600851475143))