def count_vowels(text):
    vowels = "aeiou"
    count = sum(1 for char in text.lower() if char in vowels)
    return count

def main():
    text = input("Enter text: ")
    vowel_count = count_vowels(text)
    print(f"Number of vowels: {vowel_count}")

if __name__ == "__main__":
    main()
