def get_book_text(book_path):
    with open(book_path) as file:
        file_text = file.read()
        return file_text

def get_num_words(book_path):
    text = get_book_text(book_path)
    words = text.split()
    return len(words)

def count_letters(book_path):
    text = get_book_text(book_path)
    letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def print_sorted_letters(book_path):
    letters = count_letters(book_path)
    sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")

def print_report(book_path):
    num_words = get_num_words(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    print_sorted_letters(book_path)
    print("============= END ===============")