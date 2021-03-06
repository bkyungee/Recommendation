import csv
from konlpy.tag import Okt
from gensim.models import word2vec

File_Path = "./Kakaotalktext.txt"
f = open(File_Path, 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter=':')
rdw = list(rdr)
#print(r)
#print("Name=%s : Contents=%s" % (rdw[11][1], rdw[11][2]))
#print("Name=%s : Contents=%s" % (rdw[12][0], rdw[12][2]))
#print("Name=%s : Contents=%s" % (rdw[13][0], rdw[13][2]))

f.close()

#트위터 형태소 분석기를 로드한다. Twiter가 KoNLPy v0.4.5 부터 Okt로 변경 되었다.
twitter = Okt()

#텍스트를 한줄씩 처리합니다.
result = []
for line in rdw:
    #print(line[2])
    #형태소 분석하기, 단어 기본형 사용
    malist = twitter.pos(line[2], norm=True, stem=True)
    r = []
    for word in malist:
        #Josa”, “Eomi”, “'Punctuation” 는 제외하고 처리
        if not word[1] in ["Josa","Eomi","Punctuation"]:
            r.append(word[0])
    #형태소 사이에 공백 " "  을 넣습니다. 그리고 양쪽 공백을 지웁니다.
    rl = (" ".join(r)).strip()
    result.append(rl)
    #print(rl)

#형태소들을 별도의 파일로 저장 합니다.
with open("Kakaotalk.nlp",'w', encoding='utf-8') as fp:
    fp.write("\n".join(result))

#Word2Vec 모델 만들기
wData = word2vec.LineSentence("Kakaotalk.nlp")
wModel =word2vec.Word2Vec(wData, size=200, window=4, hs=1, min_count=2, sg=1)
wModel.save("Kakaotalk.model")
print("Word2Vec Modeling finished")

# size -> n차원벡터로 변경
# window -> 주변 단어는 앞뒤로 n개 
# min_count -> 출현 빈도는 n개 미만은 제외 
# sg -> CBOW와 Skip-Gram 중 Skip-Gram 선택
# hs -> hs가 1이면 softmax를 트레이닝할때 사용. 0이면 0이 아닌경우 음수로 샘플링