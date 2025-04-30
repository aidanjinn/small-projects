import math
import re
from PyPDF2 import PdfReader
from collections import defaultdict

def tokenize(doc):
    return re.findall(r'\w+', doc.lower())

def compute_freq(tokens):
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq

def compute_doc_freq(doc_tokens_dict):
    doc_freq = defaultdict(int)
    for tokens in doc_tokens_dict.values():
        unique_terms = set(tokens)
        for term in unique_terms:
            doc_freq[term] += 1
    return doc_freq

def compute_tfidf(term_freqs, doc_freqs, total_docs, doc_length):
    tfidf_vect = {}
    for term, tf in term_freqs.items():
        norm_tf = min(tf / doc_length, 0.2)  
        idf = math.log(total_docs / (doc_freqs.get(term, 0) + 1))
        tfidf_vect[term] = norm_tf * idf
    return tfidf_vect

class VectorComparator:
    def magnitude(self, concordance):
        return math.sqrt(sum(count ** 2 for count in concordance.values()))

    def relation(self, concordance1, concordance2):
        all_words = set(concordance1) | set(concordance2)
        topvalue = sum(concordance1.get(word, 0) * concordance2.get(word, 0) for word in all_words)
        mag1 = self.magnitude(concordance1)
        mag2 = self.magnitude(concordance2)
        return topvalue / (mag1 * mag2) if mag1 * mag2 != 0 else 0

def read_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


compare = VectorComparator()

doc_tokens = {}
term_freqs = {}
doc_lengths = {}


for x in range(1, 13):
    doc_id = f"text{x}.pdf"
    doc_text = read_pdf(doc_id)
    tokens = tokenize(doc_text)
    term_freq = compute_freq(tokens)

    doc_tokens[doc_id] = tokens
    term_freqs[doc_id] = term_freq
    doc_lengths[doc_id] = len(tokens)


doc_freqs = compute_doc_freq(doc_tokens)

# Compute TF-IDF vectors
tfidf_vectors = {}
total_docs = len(doc_tokens)

for doc_id in doc_tokens:
    tfidf_vectors[doc_id] = compute_tfidf(term_freqs[doc_id], doc_freqs, total_docs, doc_lengths[doc_id])

query = "cake recipe"
query_tokens = tokenize(query)
query_tf = compute_freq(query_tokens)
query_length = len(query_tokens)

query_vector = compute_tfidf(query_tf,doc_freqs,total_docs,query_length)

similarities = {}

for doc_id, doc_vector in tfidf_vectors.items():
    similarity = compare.relation(query_vector, doc_vector)
 
    matched_terms = set(query_tf) & set(doc_vector)
    term_coverage = ( len(matched_terms) / len(query_tf) )
    similarity *= term_coverage  

    similarities[doc_id] = similarity

ranked = sorted(similarities.items(), key=lambda x: x[1], reverse = True)

for doc_id, sim in ranked:
    print(doc_id, sim)



    
