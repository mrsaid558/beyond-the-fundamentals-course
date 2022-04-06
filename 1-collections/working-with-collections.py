# this is lesson number 4 in the chapter one
# Working with collections

'''
Working with collections

    - Each item in a list is automatically assigned a consecutive number based on its position, known as an index number. 
        It's important to note that index numbering does not start at one.
        for example => ["one", "two", "three"]
.                         0      1       2    => this is index sorting
    - to print the items in the list by it's index we write the name of the list and write []
        square brackets and put in these brackets the index of the items => print(friends[0])
    
    => printing items in the dictionary:
        - we write the name of the dictionary and write [] square brackets and put in these
            brackets the name of variable that stores the dictionary value
'''

# in this example i will write my friends in a list and i will print any friend i want by this index

#friends
friends = [
    "Ahmed",   # index (0)
    "Mahmoud", # index (1)
    "Zaki",    # index (2)
    "Khaled",  # index (3)
    "fetian",  # index (4)
    "Mohamed"  # index (5)
]
# to print the first items (Ahmed)
print(friends[0])
# and to print the second items (Mahmoud)
print(friends[1])


# printing items in the dictionary
person_data = {
    'name': "Ahmed",
    'address': "suhaj 15 street",
    'school_name': "kadry about hussin",
    'age': 16,
    'courses': ["html", "css", "كالنبيان المرصوص", "javascript"]
}

print(person_data['name'])