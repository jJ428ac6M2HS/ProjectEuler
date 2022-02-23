'''
Enoncé :

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''

def find_product():
    list_results = []
    # 100 and 1000 for 3-digit numbers only
    for a in range(100,1000):
        for b in range(100,1000):
            #print("a is {} and b is {} making a*b = {}".format(a, b, a*b))
            pal_result = test_palindrome(a*b)
            if pal_result != None:
                list_results.append(int(pal_result))
                print(a, b, pal_result)
    return list_results

def test_palindrome(number):
    number = str(number)
    for i in range(0, len(number)):
        #print("number is {}, letter {} and letter {} should match".format(number, number[i], number[len(number)-1-i]))
        if number[i] == number[len(number)-1-i]:
            pass
        else:
            return None
    #print(number)
    return number

results = find_product()
print(results)
results.sort(reverse=True)
print(results)