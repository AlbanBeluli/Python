def count_words(arr: str):
    words = []
    for word in arr.split():
        words.append(word)
        print(words)
    return f"There are {len(words)} words in the sentence."

print(count_words("Hello, I am learning Python!"))



def count_characters(a):
    a = a.replace(' ', '') 
    return f'The string has ' \
           f'{len(a)} elements '
print(count_characters('I love learning'))


def capitalize(a: str):
    upper = []
    for i, word in enumerate(a.split()):
        if word[0].islower():
            upper.append(word.capitalize())
        else:
            upper.append(word)
    return ' '.join(upper)

print(capitalize('hello, i am learning python!'))


# zip() function in Python
#The function combines the two lists into pairs of tuples.
def make_tuples(a, b):
    a = zip(a, b)
    return list(tuple(a))
print(make_tuples([1, 2, 3], [4, 5, 6]))




def average_calories():
    scores = []
    while True:
        score = input("Enter calories burned or enter done to quit: ")
        if score == "done":
            break
        else:
            scores.append(int(score))
    return sum(scores) / len(scores)

print(average_calories())
