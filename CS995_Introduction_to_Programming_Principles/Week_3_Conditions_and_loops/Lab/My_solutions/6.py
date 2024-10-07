# Write a program that prints all numbers between 10 and 26 that are not multiples of 2 and 3. The operator
# % can be used to test if a number is a multiple of another number. For example, i % 2 returns 0 if i is a
# multiple of 2.

non_multiples = []

num = 10

while num <27:
    if num % 2 > 0 or num % 3 > 0:
        non_multiples.append(num)
    num +=1

print(non_multiples)