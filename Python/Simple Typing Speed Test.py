import time

def typing_speed_test():
    input("Press Enter to start the typing test...")
    start_time = time.time()
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    user_input = input()
    end_time = time.time()

    if user_input == text:
        elapsed_time = end_time - start_time
        print(f"Well done! Your typing speed is {len(text)/elapsed_time:.2f} characters per second.")
    else:
        print("Text did not match. Please try again.")

if __name__ == "__main__":
    typing_speed_test()
