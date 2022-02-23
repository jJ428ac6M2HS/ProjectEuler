'''
Enoncé :

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

'''
# Proof Of Concept
# la fonction range prend la deuxieme valeur comme max non-comprise, c'est donc OK
below = 10
sum = 0
for i in range(0,below):
    if i%3 == 0 or i%5 == 0:
        print(i)
        sum += i

print("Final")
print(sum)

# Et l'exercice
below = 1000
sum = 0
for i in range(0,below):
    if i%3 == 0 or i%5 == 0:
        print(i)
        sum += i

print("Final")
print(sum)