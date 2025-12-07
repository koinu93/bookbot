from stats import get_book_text, get_word_count, character_repeat_count, dictionary_pairs, sort_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    
    word_total = get_word_count(book_path)
    #print(f"Found {word_total} total words")
    
    character_count = character_repeat_count(book_path)
    #print(character_count)

    pairs = dictionary_pairs(book_path)

    sort = sort_list(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")
    print("--------- Character Count -------")
    for value in sort:
        print(f"{value["char"]}: {value["num"]}")

    
main()