def get_word_count(text):
    words = text.split()
    return len(words)

def text_to_num(text):
    lower_text = text.lower()
    start_count = 1
    letter_dict = {}
    for char in lower_text:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = start_count
    return letter_dict

def sort_letters(letter_dict):
    sorted_list = sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)
    print("--------- Character Count -------")
    for item in sorted_list:
        if item[0].isalpha() == True:
            print(f'{item[0]}: {item[1]}')
        else:
            pass
        
    return