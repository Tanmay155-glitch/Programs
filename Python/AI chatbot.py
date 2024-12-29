from transformers import pipeline
import tf_keras as keras


qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

context = """
Artificial Intelligence (AI) is a field of computer science that aims to create machines that can perform tasks 
that would normally require human intelligence. AI is being used in various applications, including healthcare, 
finance, education, and more. Recent advancements in machine learning, deep learning, and natural language processing 
(NLP) have significantly improved the capabilities of AI systems. Many modern AI systems are based on neural networks, 
which are inspired by the structure and functioning of the human brain.
"""

def chatbot():
    print("Welcome to the AI-based Question Answering Chatbot! Ask a question or type 'exit' to quit.")
    
    while True:
        question = input("\nAsk your question: ")
        
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = qa_pipeline(question=question, context=context)
        
        print(f"Answer: {result['answer']}")

chatbot()
