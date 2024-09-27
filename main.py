import os


def main():
# Start up fuctions at the begining of the program
    # current_directory = os.getcwd()
    # print(f"Current Directory: {current_directory}")

    book_path = "/home/noobzy/workspace/github.com/mohald-3/BookBot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    list_of_dict = get_list_dict(num_char)
    list_of_dict_sorted = sorted(list_of_dict, reverse = True, key = sort_on)

# End up fuctions at the begining of the program

# Start Console Text

    print (f"=== Begin report of {book_path} ===")
    # print(text)
    print(f"{num_words} words found in the document")
    print("Character appearance in the document:")
    # print(num_char)
    # print(list_of_dict)
    # print(list_of_dict_sorted)
    print_sorted_list(list_of_dict_sorted)

    print("=== End report ===")

# End Console Text

# Fuctions start

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)
# returns the word count of the book

# fuction that returns a dictionary of unique character and its occurrence in the book 
def get_num_char(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

# assigns the letter to its occurrence count
def get_list_dict(num_char):
    list_of_dicts_char = [{"character": key, "count": value} for key, value in num_char.items()]
    return list_of_dicts_char

# prints out a list of char and its value sorted accendedly by the occurence count
def sort_on(dict):
    return dict["count"]

def print_sorted_list(list):
    for item in list:
        if item["character"].isalpha():
            print(f'The letter {item["character"]} appeared {item["count"]} times in the book') 

    
if __name__ == "__main__":
    main()
