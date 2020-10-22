# get the book from http://www.gutenberg.org/files/11/11-0.txt saved here as alice.txt
import urllib.request

# retrieve the book
url = "http://www.gutenberg.org/files/11/11-0.txt"
file_name = "alice.txt"
urllib.request.urlretrieve(url, file_name)

# read the book
with open(file_name) as alice_book:
    alice_text = alice_book.read()

# process the book
words = alice_text.lower().split()
word_count = {}
for word in words:
    # Getting this right is actually pretty hard
    # (scroll throught the list of words and mess around with it to get a feel for how hard)
    # Is a - part of the word, or is it punctuation?
    # should the mark be removed or should the word be split on this sign?
    word = word.strip("!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~!”")   # we need to keep "-" so string.punctution doesn't work
    if len(word) > 0 and word[0].isalpha():
        word_count[word] = word_count.get(word, 0) + 1

# get the longest word
longest_word = ""
for word in word_count.keys():
    if len(word) > len(longest_word):
        longest_word = word

# print to output file
with open("alice_words.txt", "w") as alice_output:
    string_format = "{:<" + str(len(longest_word)) + "} {:>5}\n"

    alice_output.write(string_format.format("Word", "Count"))
    alice_output.write("=" * (len(longest_word) + 6) + "\n")

    for word in sorted(word_count.keys()):
        alice_output.write(string_format.format(word, word_count[word]))

# exercise 4
print("The longest word is", longest_word, " and its lengths is:", len(longest_word), "characters")
