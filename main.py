def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_word_count(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
        words = content.split()
        word_total = len(words)
    return word_total

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_total = get_word_count(book_path)
    print(f"Found {word_total} total words")
    
main()