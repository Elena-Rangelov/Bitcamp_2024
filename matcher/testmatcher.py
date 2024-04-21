import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

class Matcher:
  def __init__(self):
    self.student_vectorizer = TfidfVectorizer()
    self.job_vectorizer = TfidfVectorizer()
    self.student_corpus = None
    self.job_corpus = None
    self.knn = None

  def fit(self, student_data, job_data):
    self.student_tokens = student_data
    self.job_tokens = job_data

    self.student_corpus = self.student_vectorizer.fit_transform([" ".join(tokens) for tokens in self.student_tokens])
    self.job_corpus = self.job_vectorizer.fit_transform([" ".join(tokens) for tokens in self.job_tokens])

    self.knn = NearestNeighbors(n_neighbors=5, metric='cosine').fit(self.job_corpus)

  def predict(self, student_tokens, n=10):
    student_features = self.job_vectorizer.transform(student_tokens)
    distances, indices = self.knn.kneighbors(student_features)
    return indices.flatten()[:n]  # Return top n job indices

