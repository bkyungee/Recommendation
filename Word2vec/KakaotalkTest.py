from gensim.models import word2vec


model = word2vec.Word2Vec.load("Kakaotalk.model")
print(model.most_similar('준면'))
print(model.most_similar('백현'))
print(model.most_similar('찬열'))
print(model.most_similar('엑소'))
print(model.most_similar('하트'))