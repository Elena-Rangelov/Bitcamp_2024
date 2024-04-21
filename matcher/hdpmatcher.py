import numpy as np
import sklearn.neighbors
from sklearn.neighbors import NearestNeighbors

from gensim.models import HdpModel, TfidfModel
from gensim.test.utils import common_corpus, common_dictionary
from gensim.corpora.dictionary import Dictionary

student_data = [
    {"preferences": {"work_type": "full-time"}, "resume": ["machine", "learning", "artificial", "intelligence", "python"]},
    {"preferences": {"work_type": "part-time"}, "resume": ["data", "analysis", "statistics", "finance"]},
    {"preferences": {"work_type": "internship"}, "resume": ["natural", "language", "processing", "deep", "learning", "algorithms"]},
    {"preferences": {"work_type": "full-time"}, "resume": ["software", "engineering", "computer", "vision", "c++"]},
    {"preferences": {"work_type": "part-time"}, "resume": ["web", "development", "javascript", "html", "css"]},
    {"preferences": {"work_type": "full-time"}, "resume": ["database", "management", "sql", "nosql", "bioinformatics"]},
    {"preferences": {"work_type": "part-time"}, "resume": ["user", "experience", "design", "ux", "research"]},
    {"preferences": {"work_type": "internship"}, "resume": ["cybersecurity", "network", "security", "penetration", "testing"]},
    {"preferences": {"work_type": "full-time"}, "resume": ["embedded", "systems", "robotics", "control", "systems", "quantum"]},
    {"preferences": {"work_type": "part-time"}, "resume": ["cloud", "computing", "aws", "azure", "gcp"]},
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
    dist = np.array(list(zip(*model[x]))[1])
    dist.resize(n)
    return dist / np.linalg.norm(dist)

  def fit(self, student_data, job_data):
    self.student_tokens = student_data
    self.job_tokens = job_data

    self.student_dict.add_documents(self.student_tokens)
    self.job_dict.add_documents(self.job_tokens)
    
    self.full_dict.add_documents(self.student_tokens)
    self.full_dict.add_documents(self.job_tokens)

    self.student_corpus = [self.student_dict.doc2bow(tokens) for tokens in self.student_tokens]
    self.job_corpus = [self.job_dict.doc2bow(tokens) for tokens in self.job_tokens]

    # FULL DATA!
    self.student_model = HdpModel(self.student_corpus, self.full_dict)
    self.num_topics = max([len(self.student_model[corpus]) for corpus in self.student_corpus])
    self.X = np.zeros((len(self.job_corpus), self.num_topics))
    for i, job in enumerate(self.job_corpus):
      self.X[i] = Matcher.to_vec(self.student_model, job, self.num_topics)
    self.knn = NearestNeighbors(n_neighbors=5, metric="cosine").fit(self.X)

  def predict(self, student_tokens):
    corpus = self.student_dict.doc2bow(student_tokens)
    return self.knn.kneighbors(Matcher.to_vec(self.student_model, corpus, self.num_topics).reshape(1,-1))
  

# matcher = Matcher()
# matcher.fit(student_data, job_data)
# print(matcher.predict(matcher.student_corpus[0]))