# Write a program that prints all numbers between 10 and 26 that are not multiples of 2 and 3. The operator
# % can be used to test if a number is a multiple of another number. For example, i % 2 returns 0 if i is a
# multiple of 2.

for i in range(10, 26):
    if i%2 != 0 and i%3 !=0:
        print(i)