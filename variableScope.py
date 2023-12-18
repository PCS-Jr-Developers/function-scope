def modify_list(input_list):
    # Modify the list inside the function
    input_list.append(4)
    input_list = [1, 2, 3]  # This reassignment won't affect the original list outside the function
    print("Inside the function:", input_list)

# Define a list
my_list = [10, 20, 30]

# Call the function with the list
modify_list(my_list)

# Print the original list outside the function
print("Outside the function:", my_list)
