word = input("Enter a word: ")

print("Length of word: ", len(word))
print("Uppercase: ", word.upper())
print("Lowercase: ", word.lower())

letter = input("Enter a letter: ")
print(f"'{letter}' appears {word.count(letter)} time(s) in '{word}'")

substring = input("Enter a substring: ")
print(f"'{substring}' appears {word.count(substring)} time(s) in '{word}")

reverse_word = word [::-1]
print("Reverse: ", reverse_word)

start_index = int(input("Enter a starting index: "))
end_index = int(input("Enter an ending index: "))
sliced_word = word[start_index:end_index]
print("Sliced word: ", sliced_word)

char_to_replace = input("Enter a character to replace: ")
replacement_char = input("Enter the replacement character: ")
new_word = word.replace(char_to_replace, replacement_char, 1)
print("Replaced: ", new_word)

second_word = input("enter a second word: ")
concatenated_word = word + second_word
print("Concatenated: ", concatenated_word)

is_palindrome = word = reverse_word
is_valid_identifier = word.isidentifier()

print("Is a palidrome?", is_palindrome)
print("Is a valid Python identifier?", is_valid_identifier)