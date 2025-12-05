def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_word_count(path_to_file):
    with open(path_to_file) as f:
        content = f.read()
        words = content.split()
        word_total = len(words)
    return word_total

def character_repeat_count(path_to_file):
    character_counts = {}
    with open(path_to_file) as f:
        content = f.read()
        lower_case = content.lower()
        for char in lower_case:
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts
