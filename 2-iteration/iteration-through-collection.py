# this is the lesson number 2 in the chapter two
# this lesson about iteration through collection

'''
iteration through collection

    - for => Specifies a variable name that we can use in each iteration
        of the loop to reference the current value
        
    - in => this is a python keyword and it indicates that what follows is the set
        of values that we want to iterate through
        
    -> for variable_name in values_we_want_to_iterate:
            print(variable_name)
            
    * Using loops with lists or other collections 
        allows us to work with sets of data without writing repetitive code
'''

spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric',
]

for spice in spices:
    print(spice)
    # print("enough omelets!") => this is wrong we should delete the indentation
print("enough omelets!")