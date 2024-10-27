def count_words(string):
    words = string.split()
    return len(words)

def character_counter(string):
    count_dict = {}
    lower_string = string.lower()

    for i in lower_string:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    return count_dict

def sort_on(dict):
    return dict["count"]

def sort_alpha_characters(dict):
    char_list = []
    for char in dict:
        alpha_chars = {}
        if char.isalpha():
            alpha_chars["char"] = char
            alpha_chars["count"] = dict[char]
            char_list.append(alpha_chars)
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

def main():
    file_path = "books/frankenstein.txt"
    print(f"--- Begin report of {file_path} ---")
    with open(file_path) as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    print(f"{total_words} words found in the document")
    print("")
    char_count = character_counter(file_contents)
    alpha_chars = sort_alpha_characters(char_count)
    for item in alpha_chars:
        print(f"The {item["char"]} character was found {item["count"]} times")
    print("--- End report ---")


main()
