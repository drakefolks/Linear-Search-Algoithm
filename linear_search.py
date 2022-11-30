def linear_search(number_list, search_value):
    found = False

    for index in range(len(number_list)): #searching list linearly
        if number_list[index] == search_value:
            found = True
            break
    
    return found

numbers = [1,2,3,4,5,6,7,8,9,10] #initializing list of numbers
search_input = ' '

while search_input == ' ': #run input validation loop as long as search_input does not get assigned a new value
    try:
        search_input = int(input('Please enter a number you would like to search for\n'))

    except:
        print('Enter a valid integer')


is_found = linear_search(numbers,search_input) #pass user input to linear_search function

if is_found == False:
    print('{num} not found'.format(num=search_input))

if is_found == True:
    print('{num} found'.format(num=search_input))


