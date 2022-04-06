miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344


# that's how i solved the challenge
miles_float = float(miles)
kilometers_value = miles_float * 1.609344
print(f"your number with miles = {miles_float} and with kilometers = {kilometers_value}")

print("-" * 90)

# that's how the instructor solved the challenge
miles_float = float(miles)
kilometers = miles_float * 1.609344
print("that value in kelometers is")
print(kilometers)