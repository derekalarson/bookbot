def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

def get_num_words(text):
    return len(text.split())

def character_counts(text):
    ret_dict = {}
    for char in text:
        if char.lower() in ret_dict:
            ret_dict[char.lower()] += 1
        else:
            ret_dict[char.lower()] = 1
    return ret_dict

def dict_split(dict):
    list_of_dicts = []
    for key, value in dict.items():
        list_of_dicts.append({"char": key, "num": value})
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    unsorted = dict_split(dict)
    unsorted.sort(reverse=True, key=sort_on)
    return unsorted

def print_report(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = character_counts(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted = sorted_list(char_dict)
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

