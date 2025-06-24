# functions for bookbot

def word_count(content):
    return len(content.split())


def char_count(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1 
        else:
            char_dict[char.lower()] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    dict_list = []
    for ch, ct in char_dict.items():
        temp_dict = {"char": ch, "num": ct}
        dict_list.append(temp_dict)

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list 
