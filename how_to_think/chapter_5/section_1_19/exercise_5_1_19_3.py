def count_letters(word, letter):
    count = 0
    for word_letter in word:
        if word_letter == letter:
            count += 1
    return count


print(count_letters("banana", "a"))
