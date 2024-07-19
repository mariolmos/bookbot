def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    amount_of_words = count_words(text)
    lowered_text = lower_strings(text)
    character_count = count_characters(lowered_text)
    converted_dict = convert_dict_to_list(character_count)
    sorted_dict = sort_dict(converted_dict)
    report(book_path,amount_of_words,sorted_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text) :
    words = text.split()
    list_of_words = words
    # print(list_of_words)
    word_count = 0
    for word in list_of_words :
        word_count += 1
    # print(word_count)
    return word_count
    
def lower_strings(text) :
    lowered_text = text.lower()
    # print(lowered_text)
    return lowered_text

def count_characters(lowered_text) :
    characters = {'a':0,'b':0,'c':0,'d':0,'e':0,
                  'f':0,'g':0,'h':0,'i':0,'j':0,
                  'k':0,'l':0,'m':0,'n':0,'o':0,
                  'p':0,'q':0,'r':0,'s':0,'t':0,
                  'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for character in lowered_text :
        if character in characters :
            characters[character] += 1
            
    # print(characters)
    return characters

def convert_dict_to_list(character_count) :
    list_of_dicts = []
    for char, num in character_count.items() :
        char_num = {'char': char, 'num' : num}
        list_of_dicts.append(char_num)
    return list_of_dicts
    
def sort_on(dictionary_entry):
    # print(f"Accessing 'num' in dictionary entry: {dictionary_entry}")  # Debugging statement
    return dictionary_entry['num']

def sort_dict(converted_dict):
    converted_dict.sort(reverse=True, key=sort_on)
    return converted_dict


def report(book_path, amount_of_words, converted_dict):
    print(
        f"--- Begin report of {book_path} ---\n{amount_of_words} words found in the document."
    )
    
    for character_entry in converted_dict:
        char = character_entry["char"]
        num = character_entry["num"]
        print(f"The character '{char}' was found {num} times")
    
    print("--- End report ---")

        
main()