# Path for the file
book_path = "books/frankenstein.txt"

# Initizied the project
def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

# Create a for loop that will iterate through each word 
# See how many times you find the same letter [A..Z]
# Print how many times it found it
# Use isalpha() to orginize your findings 
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")

# Get number of the words
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

# Start soring with an empty array and then add the values that you find
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# Get all the characters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Create the sum and split
def get_character_sums(text):
    words= text.split
    return len(words)

# Get the book/file
def get_book_text(path):
    with open(book_path) as f:
        return f.read()

main()