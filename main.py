def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(len(text.split()))
    print(countLetters(text.split()))
    createReport(countLetters(text.split()))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def countLetters(text):
    letters = {}
    for word in text:
        arr = [*word.lower()]
        for letter in arr:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def createReport(letters):
    for letter in letters:
        print(f'The "{letter}" character was found {letters[letter]} times')

main()