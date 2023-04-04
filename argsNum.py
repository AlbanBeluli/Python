def any_num(*args):
    average = sum(args) / len(args)
    return f'The average is {average}'

print(any_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#The *args simply tells the function that we are not sure how many arguments we will need, 
# so the function lets us add as many arguments as possible.
