import spacy
from spacy.tokenizer import Tokenizer
import json

def remove_punctuations(normalized_tokens):
    punctuations=['?',':','!',',','.',';','|','(',')','--']
    new_tokens = []
    for word in normalized_tokens:
        if word not in punctuations:
            new_tokens.append(word)
    return new_tokens

stop_words = ['определение', 'термин', 'метод', 'применять', 'стандарт', 'устанавливать', 'форма', 'размер', 'порядок', 'применение', 'знак', 'соответствие', 'применяемого', 'оценка', 'качество', 'сертификация']

nlp = spacy.load("ru_core_news_lg")

# sentence = "Настоящий стандарт устанавливает форму, размеры и порядок применения знака соответствия, применяемого в Системе оценки качества и сертификации взаимопоставляемой продукции"
file_other = open('details.json', 'r')
other_normalized_list = []
tokens = []
iter = 0
for line in file_other:
    line = json.loads(line)
    print(iter)
    iter +=1
    
    sentence = line['USAGE']
    other_normalized = line
    doc = nlp(sentence)
    lemma_list = []
    for token in doc:
        lemma_list.append(token.lemma_)

    normalized_tokens = [] 
    for word in lemma_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False and word not in stop_words:
            normalized_tokens.append(word) 
    normalized_tokens = remove_punctuations(normalized_tokens)
    # print("\nText after removing stopwords & punctuations:\n")
    # print(normalized_tokens)
    other_normalized['USAGE'] = ' '.join(normalized_tokens)
    other_normalized_list.append(other_normalized)
    tokens += normalized_tokens
    
with open('details_norm.json', 'w') as filer:
    for line in other_normalized_list:
        filer.write(json.dumps(line, ensure_ascii=False) + '\n')
        
with open('tokens_norm.json', 'w') as filer:
    for line in tokens:
        filer.write(line + '\n')
    


