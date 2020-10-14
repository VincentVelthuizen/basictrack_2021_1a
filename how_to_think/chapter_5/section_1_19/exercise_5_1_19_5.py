import string

piet_hein = """
The road to wisdom? ---
Well, it's plain and simple to express:
Err
    and err
       and err again,
but less
    and less
        and less."""


def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct


def count_words(text):
    return len(remove_punctuation(text).split())


def count_words_containing(text, letter):
    count = 0
    for word in remove_punctuation(text).split():
        if letter in word:
            count += 1
    return count


no_words = count_words(piet_hein)
letter = "e"
no_words_containing = count_words_containing(piet_hein, letter)
percentage = 100 * (no_words_containing / no_words)

print("Your text contains {} words, of which {} ({:.1f}%) contain an \"{}\"."
      .format(no_words, no_words_containing, percentage, letter))
