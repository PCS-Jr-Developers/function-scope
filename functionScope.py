def modify_list():
    # Modify the list inside the function
    my_list.append(4)
    new_list = [3, 6, 8]
    print(new_list)
    
# Define a list
my_list = [10, 20, 30]

# Call the function with the list
modify_list()

# Print the original list outside the function
print("Outside the function:", my_list)
