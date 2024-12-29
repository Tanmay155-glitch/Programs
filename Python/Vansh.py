from googletrans import Translator

def translate():
    translator = Translator()
    print("\nWelcome to Translator App")

    while True:
        check = int(input("\nPress '1' for English \nPress '2' for German\n"))

        if check == 1:
            eng = input("\npress 'q' to exit\nEnter text in English:\n").strip()

            if eng == 'q':
                break
            else:
                germ_trans = translator.translate(eng, dest='de')
                print(f"\nText in German:\n{germ_trans.text}")

        elif check == 2:
            ger = input("\npress 'q' to exit\nEnter text in German:\n").strip()

            if ger == 'q':
                break
            else:
                eng_trans = translator.translate(ger, dest='en')
                print(f"\nText in English:\n{eng_trans.text}")  
        else:
            print("Enter valid Number!!")
            continue

def main():
    start = int(input("\nEnter '1' to Begin: "))
    if start == 1:
        translate()

if __name__ == '__main__':
    main()
