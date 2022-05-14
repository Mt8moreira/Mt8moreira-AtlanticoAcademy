# Import Dictionary
from genesim.corpora.dictionary import Dictionary
from NLP.src.nlp_utils import get_pre_process_wiki_articles

# Create a Dictionary from the articles: dictionary
articles = get_pre_process_wiki_articles()
dictionary = Dictionary(article)

# Select the id for "computer": computer_id
computer_id = Dictionar.tokens2id.get ("computer")

# Use computer_id with the dictionary to print the word
print('the word', dictionary.get(computer_id), 'has index', computer_id, 'in dictionary')

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in article]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[5][:10])