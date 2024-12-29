print("Hello! I'm a simple chatbot.")
question = input("Ask me anything: ").lower()

if "how are you" in question:
    print("I'm just a bunch of code, but thanks for asking!")
elif "name" in question:
    print("I'm called SimpleBot!")
elif "weather" in question:
    print("I don't have access to real-time weather info, but it's always a good day to code!")
else:
    print("I'm not sure how to answer that.")
