from random import randint
from FINAL_integer_checker_v4 import int_check

numbers = ["tahi", "rua", "toru", "whā", "rima"]

random_number = randint(1, 5)
question = f"What number is this {numbers[random_number]}? (1-5)"
answer = int_check(question, 1, 5)

if answer ==