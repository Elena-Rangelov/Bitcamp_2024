import numpy as np
import sklearn.neighbors
from sklearn.neighbors import NearestNeighbors

from gensim.models import HdpModel, TfidfModel
from gensim.test.utils import common_corpus, common_dictionary
from gensim.corpora.dictionary import Dictionary

student_data = [
    ["machine", "learning", "artificial", "intelligence", "python"],
    ["data", "analysis", "statistics", "finance"],
    ["natural", "language", "processing", "deep", "learning", "algorithms"],
    ["software", "engineering", "computer", "vision", "c++"],
    ["web", "development", "javascript", "html", "css"],
    ["database", "management", "sql", "nosql", "bioinformatics"],
    ["user", "experience", "design", "ux", "research"],
    ["cybersecurity", "network", "security", "penetration", "testing"],
    ["embedded", "systems", "robotics", "control", "systems", "quantum"],
    ["cloud", "computing", "aws", "azure", "gcp"],
]

# Sample company data (preprocessed job descriptions)
job_data = [
    ["software", "engineer", "machine", "learning"],
    ["data", "analysts", "statistics"],
    ["web", "developer", "javascript", "html", "css"],
    ["cybersecurity", "analyst", "experience", "penetration", "testing"],
    ["user", "experience", "designer", "research", "skills"],
    ["natural", "language", "processing", "engineer"],
    ["cloud", "architect", "aws", "azure", "gcp", "experience", "required"],
    ["embedded", "systems", "engineer", "robotics", "control", "systems"],
    ["database", "administrator", "sql", "nosql", "experience", "a plus"],
    ["financial", "analyst", "data", "analysis", "finance"],
]

class Matcher:
  def __init__(self):
    self.student_dict = Dictionary()
    self.job_dict = Dictionary()
    self.full_dict = Dictionary()
  
  def to_vec(model, x, n):
    nums = list(zip(*model[x]))
    dist = np.zeros(n)
    dist[list(nums[0])] = nums[1]
    return dist

  def normalize(x):
    return (np.array(x) > 0).astype(np.float16)

  def fit(self, student_data, job_data):
    self.student_tokens = student_data
    self.job_tokens = job_data

    self.student_dict.add_documents(self.student_tokens)
    self.job_dict.add_documents(self.job_tokens)
    self.full_dict.add_documents(self.student_tokens)
    self.full_dict.add_documents(self.job_tokens)

    self.student_corpus = [self.student_dict.doc2bow(tokens) for tokens in self.student_tokens]
    self.job_corpus = [self.job_dict.doc2bow(tokens) for tokens in self.job_tokens]

    self.num_words = len(self.student_dict.token2id)

    self.student_model = TfidfModel(self.student_corpus, self.full_dict)
    self.X = np.zeros((len(self.job_corpus), self.num_words))
    for i, job in enumerate(self.job_corpus):
      self.X[i] = Matcher.to_vec(self.student_model, job, self.num_words)
    self.knn = NearestNeighbors(n_neighbors=5, metric="jaccard").fit(self.X)

  def predict(self, student_tokens, n=10):
    return (-self.predict_raw(student_tokens)).argsort()[:n]
  
  def predict_raw(self, student_tokens):
    corpus = self.student_dict.doc2bow(student_tokens)
    m = self.X @ Matcher.to_vec(self.student_model, corpus, self.num_words).reshape(-1)
    d, i = self.knn.kneighbors(Matcher.to_vec(self.student_model, corpus, self.num_words).reshape(1,-1))
    m[i] = m[i] + d + [.04, .03, .02, .01, .00]
    return m
  
# matcher = Matcher()
# matcher.fit(student_data, job_data)
# print(matcher.predict(student_data[5]))