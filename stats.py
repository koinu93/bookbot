def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_word_count(path_to_file):
    content = get_book_text(path_to_file)
    words = content.split()
    word_total = len(words)
    return word_total

def character_repeat_count(path_to_file):
    character_counts = {}
    content = get_book_text(path_to_file)
    lower_case = content.lower()
    for char in lower_case:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def dictionary_pairs(path_to_file):
    character_counts = character_repeat_count(path_to_file)
    pairs = []
    for char, num in character_counts.items():
        {"char": char, "num": num},
        if char.isalpha() == True:
            pairs.append({"char": char, "num": num})
    return pairs

def sort_on(items):
    return items['num']

def sort_list(path_to_file):
    word_count = dictionary_pairs(path_to_file)
    word_count.sort(reverse=True, key=sort_on)
    return word_count