import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [ps.stem(word) for word in tokens if word.lower() not in stop_words]
    return ' '.join(tokens)

if __name__ == "__main__":
    sample_text = "This is a sample sentence for preprocessing."
    preprocessed_text = preprocess_text(sample_text)
    print(f"Original: {sample_text}")
    print(f"Preprocessed: {preprocessed_text}")
