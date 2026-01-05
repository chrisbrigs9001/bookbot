#print("greetings boots")
import sys
from stats import get_word_count, character_counts, sorted_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    if len(sys.argv)==2:
        # print(get_book_text("./books/frankenstein.txt"))
        #frank_file_path = "./books/frankenstein.txt"
        my_file_path=sys.argv[1]
        word_count = get_word_count(get_book_text(my_file_path))
        #print(f"Found {word_count} total words")
        c_count = character_counts(get_book_text(my_file_path))
        sorted_counts = sorted_character_count(c_count)
        #print(sorted_counts)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {my_file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_counts:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
        
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()