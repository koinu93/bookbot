def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_word_count(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
        words = content.split()
        word_total = len(words)
    return word_total