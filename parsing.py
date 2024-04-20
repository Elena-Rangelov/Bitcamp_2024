import pdfplumber
import nltk
from nltk.tokenize import word_tokenize, MWETokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from nltk.corpus import wordnet
import regex as re
import string
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt')



# extracts hard skills from a list of strings

def extract_hard_skills(words):
    	
	file_path = 'hardskills.txt'

	with open(file_path, 'r') as file:
		file_content = file.read()

	skills = word_tokenize(file_content)
	skills = [word.lower() for word in skills]
	skills = lemmatize(skills)

	return [word for word in words if word in skills]



# extracts text from a pdf at the given file path and returns the text as a long string

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



# lemmatizes list of words with wordnet
# NOTE: does not change words ending in -ing

def lemmatize(words):
	wordnet_lemmatizer = WordNetLemmatizer()
	return([wordnet_lemmatizer.lemmatize(word) for word in words])


############### USEFUL FUNCTIONS

# returns a list of hard skills from the given resume file location
# eg ['skill1', 'skill2', ...]

def get_hard_skills(filepath):
    	
	pdf_text = extract_text_from_pdf(filepath)

	if pdf_text:
			# Tokenize the text into words
		words = word_tokenize(pdf_text.lower())
			
		# remove stopwords
		stopwords = set(nltk.corpus.stopwords.words('english'))
		filtered_words = [word for word in words if word not in stopwords]
		
		# remove punctuation
		filtered_words = [''.join([char for char in word if char not in string.punctuation + '“']) for word in filtered_words]
		filtered_words = [word for word in filtered_words if word != '']

		# lemmatize
		filtered_words = lemmatize(filtered_words)


		return extract_hard_skills(filtered_words)




# returns a list of lists of the hard skills of each resume in the folder path given
# eg: [['student1_skill1', 'student1_skill2', ...], ['student2_skill1', 'student2_skill2', ...], ...]

def get_hard_skills_all_files(folder_path='resumes/INFORMATION-TECHNOLOGY/'):

	# Get a list of all files in the folder
	file_list = os.listdir(folder_path)

	# Filter out only PDF files
	pdf_files = [file for file in file_list if file.lower().endswith('.pdf')]

	# Cycle through each PDF file
	all_files = []

	for pdf_file in pdf_files:
		all_files.append(get_hard_skills(folder_path+pdf_file))

	return(all_files)
		
print(get_hard_skills_all_files())

