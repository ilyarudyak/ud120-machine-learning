from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

corpus = ['This is the first document.', 'This is the second second document.',
          'And the third one.', 'Is this the first document?']


def build_vectorizer():
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X


def transform(X):
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    return tfidf.toarray()

if __name__ == '__main__':
    vectorizer, X = build_vectorizer()
    print(transform(X))
