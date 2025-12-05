def main():
    from stats import get_book_text, get_word_count, character_repeat_count

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_total = get_word_count(book_path)
    print(f"Found {word_total} total words")
    character_count = character_repeat_count(book_path)
    print(character_count)
    
main()