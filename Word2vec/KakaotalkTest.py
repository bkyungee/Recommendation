from gensim.models import word2vec


model = word2vec.Word2Vec.load("Kakaotalk.model")
print(model.most_similar('하트'))
print(model.most_similar('프렌즈'))
