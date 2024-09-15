# from collections import Counter

def main():
    # Reads the content of the book and stores it as a value
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    char_list_of_dict = get_list_dict(num_char)


    #num_char_sorted = sort_char_count(num_char)



    print (f"=== Begin report of {book_path} ===")
    # print(text)
    print(f"{num_words} words found in the document")
    print("Character appearance in the document:")
    print(num_char)
    print (char_list_of_dict)
    print("=== End report ===")

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

def get_list_dict(dict):
    list_of_dict = [{key:value} for key, value in dict.items()}
    return list_of_dict




    
if __name__ == "__main__":
    main()