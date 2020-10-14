def count_letters(word, letter):
    count = 0
    prev = word.find(letter)  # find the first occurrence
    while prev >= 0:  # if a new occurrence was found look at the remaing part of the string
        prev = word.find(letter, prev + 1)
        count += 1
    return count


print(count_letters("banana", "a"))
