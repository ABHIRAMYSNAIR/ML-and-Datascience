import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import brown
from nltk.chunk import RegexpChunkParser
sen = "The quick brown fox jumps over lazy dog"
tokens=word_tokenize(sen)
print(tokens)
pos_tags=nltk.pos_tag(tokens)
print(pos_tags)
text=brown.words(categories='news')[:1000]
bigrams=list(ngrams(text,2))
fre_dist=nltk.FreqDist(bigrams)
for i in bigrams:
    print(f"{i}:{fre_dist[i]}")
tag=nltk.pos_tag(word_tokenize("The quick brown fox jumps over the lazy dog"))
grammar=r"NP:{<DT>?<JJ>*<NN>}"
cp=RegexpChunkParser(grammar)
res=cp.parse(tag)
print(res)