from stats import get_word_count, text_to_num, sort_letters
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    text = get_book_text(sys.argv[1])
    word_count = get_word_count(text)
    letter_count = text_to_num(text)
    #sorted = sort_letters(letter_count)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    #print(sorted)
    sort_letters(letter_count)
    print("============= END ===============")

def get_book_text(book):
    with open(book) as f:
        return f.read()

main()