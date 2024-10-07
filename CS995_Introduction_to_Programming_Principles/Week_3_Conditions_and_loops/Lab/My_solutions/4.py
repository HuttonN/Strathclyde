#Write a program that converts the string values "one", "two", "three", "four", "five", "six", "seven",
#"eight" and "nine" into the corresponding integer value. For example, the program should print 1, when
#a string variable contains "one". The program should use a dictionary to solve this problem and check if
#the string is a dictionary key before using it to lookup the value.

num_values_dict = {
    "one": 1,
    "two": 2,
    "three": 3, 
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

word = input("Enter a number (word) between 1 and 9 inclusive: ").lower()

for key in num_values_dict:
    if word == key:
        print(num_values_dict[key])
        break
else:
    print("number not recognised")