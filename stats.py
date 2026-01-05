def get_word_count(the_book):
    words = the_book.split()
    num_words=len(words)
    return num_words

def character_counts(the_book):
    chars = {}
    for c in the_book:
        ch = c.lower()
        if ch in chars:
            #if the character exists in the dictionary already
            chars[ch]+=1
        else:
            #if the chraracter isn't yet in dictionary, add it to dictionary
            chars[ch]=1
    return chars


def sort_on(item):
    return item["num"]

def sorted_character_count(chars):
    #temp_dictionary = {}
    temp_list = []
    #for c in chars:
    #    print(f"{chars[c]} "+c) */
    for c in chars:
        temp_list.append({"char": c, "num": chars[c]})
    #print(temp_list)
    #print(type(temp_list))
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list