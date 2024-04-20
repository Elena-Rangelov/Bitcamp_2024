import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import os


################################################################# reading + tf-idf

def extract_text_from_folder(folder_path):
    try:
        text = ''
        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(folder_path, filename)
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading documents: {e}")
        return None

# Example folder path
folder_path = 'test/'

# Example usage
pdf_text = extract_text_from_folder(folder_path)

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

if pdf_text:

    # Tokenize the text into words
    words = word_tokenize(pdf_text.lower())
    
    # Remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))
    filtered_words = [word for word in words if word not in stopwords and word != ',']
    
    # Join the filtered words back into a single string
    preprocessed_text = ' '.join(filtered_words)
    
    # Calculate TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([preprocessed_text])
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the top TF-IDF terms
    top_tfidf_indices = tfidf_matrix[0].toarray().argsort()[0][::-1][:10]
    top_tfidf_terms = [feature_names[idx] for idx in top_tfidf_indices]
    
    print("Top TF-IDF terms:")
    print(top_tfidf_terms)

    print(filtered_words)

    	
################################################### tf-idf

# Calculate TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([preprocessed_text])
feature_names = vectorizer.get_feature_names_out()

# Get the top TF-IDF terms
top_tfidf_indices = tfidf_matrix[0].toarray().argsort()[0][::-1][:10]
top_tfidf_terms = [feature_names[idx] for idx in top_tfidf_indices]

print("Top TF-IDF terms:")
print(top_tfidf_terms)

print(filtered_words)


################################################### synonyms

synonyms = []
word = 'mother'
for synonym in wordnet.synsets(word):
   for item in synonym.lemmas():
      if word != synonym.name() and len(synonym.lemma_names()) > 1:
        synonyms.append(item.name())

print(synonyms)


################################################### multi-word tokenization

if pdf_text:
    	# Tokenize the text into words
	words = word_tokenize(pdf_text.lower())
	
	# Define multi-word expressions
	mwe_list = [("machine", "learning"), ("data", "science"), ("natural", "language", "processing") ,("artificial", "intelligence"), ("web", "development"), ("website", "development"),\
				("web", "dev"), ("app", "development"), ("application", "development"), ("app", "dev") ]
	
	# initialize MWETokenizer with multi-word expressions
	mwe_tokenizer = MWETokenizer(mwe_list)
	
	# tokenize multi-word expressions
	multi_word_tokens = mwe_tokenizer.tokenize(words)
	
	# remove duplicates
	unique_multi_word_tokens = list(set(multi_word_tokens))
