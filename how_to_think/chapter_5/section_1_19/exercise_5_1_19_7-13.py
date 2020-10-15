def reverse(text):
    txet = ""
    for i in range(len(text) - 1, -1, -1):
        txet += text[i]
    return txet


def mirror(text):
    return text + reverse(text)


def remove_letter(letter, text):
    stripped = ""
    for letter_in_text in text:
        if letter_in_text != letter:
            stripped += letter_in_text
    return stripped


def is_palindrome(text):
    return text == reverse(text)


def remove(substring, text):
    return text.replace(substring, "", 1)


def remove_all(substring, text):
    return text.replace(substring, "")


print(reverse("happy"))
print(reverse("Python"))
print(reverse(""))
print(reverse("a"))
print()

print(mirror("good"))
print(mirror("Python"))
print(mirror(""))
print(mirror("a"))
print()

print(remove_letter("a", "apple"))
print(remove_letter("a", "banana"))
print(remove_letter("z", "banana"))
print(remove_letter("i", "Mississippi"))
print(remove_letter("b", ""))
print(remove_letter("b", "c"))
print()

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))
print(not is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome(""))  # yes it is
print()

print(remove("an", "banana"))
print(remove("cyc", "bicycle"))
print(remove("iss", "Mississippi"))
print(remove("eggs", "bicycle"))
print()

print(remove_all("an", "banana"))
print(remove_all("cyc", "bicycle"))
print(remove_all("iss", "Mississippi"))
print(remove_all("eggs", "bicycle"))
