import nltk
#nltk.download('punkt')
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import matplotlib.pyplot as plt
import seaborn as sns

stop_words = set(stopwords.words('french'))
liste_supp = ['«','»','’', 'plus', 'a', 'comme', 'cette', 'deux','dun','dune','après','entre','alors','ainsi', 'dont', 'quil', 'aussi',
              'lors', 'également', 'où', 'tout', 'sous', 'sans', 'très', 'trois', 'si', '000', 'cest', 'puis', 'avant', 'depuis',
              'vers','leurs', 'the']
stop_words.update(liste_supp)

with open('train.json') as json_file:
    fsquadDataset = json.load(json_file)

with open('data/json_output/output.json') as json_file:
    annotedDataset = json.load(json_file)

#print(fsquadDataset.keys())

stringContextes = ''
stringAnnot = ''

for text in fsquadDataset['data']:
    for paragraph in text['paragraphs']:
        stringContextes = stringContextes + ' ' + paragraph['context'].lower()

for text in annotedDataset['data']:
    for paragraph in text['paragraphs']:
        stringAnnot = stringAnnot + ' ' + paragraph['context'].lower()


#print(stringContextes)

stringContextes = stringContextes.translate(str.maketrans('', '', string.punctuation))
stringAnnot = stringAnnot.translate(str.maketrans('', '', string.punctuation))
word_tokens_fsquad = word_tokenize(stringContextes)
word_tokens_annot = word_tokenize(stringAnnot)


filtered_sentence_fsquad = [w for w in word_tokens_fsquad if not w in stop_words]
filtered_sentence_annot = [w for w in word_tokens_annot if not w in stop_words]

compteur_fsquad = Counter(filtered_sentence_fsquad).most_common(100)
compteur_annot = Counter(filtered_sentence_annot).most_common(100)

words_fsquad = [word[0] for word in compteur_fsquad]
occurences_fsquad = [word[1] for word in compteur_fsquad]

words_annot = [word[0] for word in compteur_annot]
occurences_annot = [word[1] for word in compteur_annot]

f, (ax1,ax2) = plt.subplots(2,1, figsize = (10,15), sharex = True)
graph_fsquad = sns.barplot(x = words_fsquad, y = occurences_fsquad, ax = ax1)
ax1.set_ylabel('FSquad')

graph_annot = sns.barplot(x = words_annot, y = occurences_annot, ax = ax2)
ax2.set_ylabel('Annotations')

graph_fsquad.set_xticklabels(graph_fsquad.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
graph_annot.set_xticklabels(graph_annot.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
plt.show()

