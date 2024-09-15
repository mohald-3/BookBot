# from collections import Counter

def main():
    # Reads the content of the book and stores it as a value
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(text)
    print(num_words)
    print(num_char)

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




    
if __name__ == "__main__":
    main()