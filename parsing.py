import pdfplumber
import nltk
from nltk.tokenize import word_tokenize, MWETokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from nltk.corpus import wordnet
import regex as re
import string
from nltk.stem import PorterStemmer, WordNetLemmatizer
# nltk.download('wordnet')


def extract_text_from_pdf(file_path):
	try:
		with pdfplumber.open(file_path) as pdf:
			text = ''
			for page in pdf.pages:
				text += page.extract_text()
		return text
	except Exception as e:
		print(f"Error reading PDF: {e}")
		return None

# Example usage
pdf_file_path = 'resumes/INFORMATION-TECHNOLOGY/10089434.pdf'
pdf_text = extract_text_from_pdf(pdf_file_path)

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

if pdf_text:
    	# Tokenize the text into words
	words = word_tokenize(pdf_text.lower())
	
	# remove duplicates
	unique_word_tokens = list(set(words))

	words = [word for word in unique_word_tokens]
	
	# remove stopwords
	stopwords = set(nltk.corpus.stopwords.words('english'))
	filtered_words = [word for word in words if word not in stopwords]
	
	# remove punctuation
	filtered_words = [''.join([char for char in word if char not in string.punctuation + '“']) for word in filtered_words]
	filtered_words = [word for word in filtered_words if word != '']

	# lemmatizing with wordnet - 
	# NOTE: does not change words ending in -ing
	wordnet_lemmatizer = WordNetLemmatizer()
	filtered_words = [wordnet_lemmatizer.lemmatize(word) for word in filtered_words]

	print(filtered_words)
	


