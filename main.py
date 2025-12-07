import sys
from stats import get_book_text, get_word_count, character_repeat_count, dictionary_pairs, sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
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