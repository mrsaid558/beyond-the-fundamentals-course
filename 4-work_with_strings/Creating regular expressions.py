# chapter 4 Combining and manipulating strings
# this is the third lesson in chapter 4
# Creating regular expressions

#A regular expression lets you create a description of a pattern that you want to match.

import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'
five_digit_expression = r"\d{5}"
print(re.search(five_digit_expression, five_digit_zip))
print(re.search(five_digit_expression, nine_digit_zip))
print(re.search(five_digit_expression, phone_number))

# pin code should have 6 digits
pin_code_1 = "159753"
pin_code_2 = "123456"
pin_code_3 = "15975385462"
six_digits_expression = r"\d{6}"

print(re.search(six_digits_expression, pin_code_1))
print(re.search(six_digits_expression, pin_code_2))
print(re.search(six_digits_expression, pin_code_3))