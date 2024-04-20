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
    ["looking", "for", "data", "analysts", "statistics"],
    ["seeking", "web", "developer", "javascript", "html", "css"],
    ["need", "cybersecurity", "analyst", "experience", "penetration", "testing"],
    ["hiring", "user", "experience", "designer", "research", "skills"],
    ["looking", "for", "natural", "language", "processing", "engineer"],
    ["cloud", "architect", "aws", "azure", "gcp", "experience", "required"],
    ["embedded", "systems", "engineer", "robotics", "control", "systems"],
    ["database", "administrator", "sql", "nosql", "experience", "a plus"],
    ["financial", "analyst", "data", "analysis", "finance"],
]

student_dict = Dictionary()
job_dict = Dictionary()

student_tokens = [doc["resume"] for doc in student_data]
job_tokens = job_data

student_dict.add_documents(student_tokens)
job_dict.add_documents(job_tokens)

student_corpus = [student_dict.doc2bow(tokens) for tokens in student_tokens]
job_corpus = [job_dict.doc2bow(tokens) for tokens in job_tokens]

def to_vec(model, x, n):
  dist = np.array(list(zip(*model[x]))[1])
  dist.resize(n)
  return dist / np.linalg.norm(dist)

student_model = HdpModel(student_corpus, student_dict)
num_topics = max([len(student_model[corpus]) for corpus in student_corpus])
X = np.zeros((len(job_corpus), num_topics))
for i, job in enumerate(job_corpus):
  X[i] = to_vec(student_model, job, num_topics)
knn = NearestNeighbors(n_neighbors=5, metric="cosine").fit(X)

