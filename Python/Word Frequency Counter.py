from collections import Counter

def word_frequency(text):
    words = text.split()
    return Counter(words)

def main():
    text = input("Enter text: ")
    frequencies = word_frequency(text)
    print(frequencies)

if __name__ == "__main__":
    main()
