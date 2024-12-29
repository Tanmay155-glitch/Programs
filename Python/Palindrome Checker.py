def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def main():
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

if __name__ == "__main__":
    main()
