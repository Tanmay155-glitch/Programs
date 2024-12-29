from flask import Flask, request, render_template
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai

app = Flask(__name__)
openai.api_key = "your_openai_api_key"

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

corpus = [
    "This is a sample programming concept and solution.",
    "Another example of a programming concept and solution.",]


tfidf = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words=stop_words)
tfidf_matrix = tfidf.fit_transform(corpus)

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Student: {user_input}\nAI: ",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        bot_response = response.choices[0].text.strip()

        user_tfidf = tfidf.transform([user_input])
        similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix)

        most_relevant_index = similarity_scores.argsort()[0][-1]
        most_relevant_concept = corpus[most_relevant_index]

        return render_template('index.html', bot_response=bot_response, most_relevant_concept=most_relevant_concept)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
