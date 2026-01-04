#print("greetings boots")
from stats import get_word_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    word_count = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(f"Found {word_count} total words")
    
    
main()