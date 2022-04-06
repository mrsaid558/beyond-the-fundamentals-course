# chapter 4 Combining and manipulating strings
# this is the second lesson in chapter 4
# finding patterns in strings

first_name = "mohamed"
last_name = "ahmed"
note = 'award: Nobel Peace Prize'

# to make the first letter of the word is capital we write the string.capitalize()
first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
print(first_name_cap)
print(last_name_cap)

# finding text => [.find(), index(), .refind, .reindex]
award_location = note.find("award: ")
print(award_location)

# slicing => note[start:end]
award_text = note[7:]
print(award_text)