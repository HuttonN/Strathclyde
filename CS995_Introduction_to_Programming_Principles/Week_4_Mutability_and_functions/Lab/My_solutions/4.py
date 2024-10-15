"""Write a program that includes a function that returns statements about the future. The function should
include a list of text statements and use the random module to pick a statement at random and return it.
The random.randint function should be used to pick an index from 0 to N, where N is the length of the
list."""

import random

def return_future_statement():
    statement_list = ["Earth has been taken over", "Men are obsolete", "Elon Musk is running for president"]
    list_length = len(statement_list)
    return statement_list[random.randint(0,list_length-1)]

future_statement = return_future_statement()
print(future_statement)