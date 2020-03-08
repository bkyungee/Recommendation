import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

rating_data = pd.read_csv('ratings.csv')
movie_data = pd.read_csv('movies.csv')

# timestamp 데이터 삭제
rating_data.drop('timestamp', axis=1, inplace=True)
#rating_data.head(2)

# movieId 기준으로 movies.csv와 ratings.csv 데이터 merge
movie_rating_data = pd.merge(rating_data, movie_data, on='movieId')
#movie_rating_data.head(2)

# userId*title이며 data값은 rating으로 하는 pivot table로 변형
movie_rating_pivot = movie_rating_data.pivot_table('rating', index='title', columns='userId')

# rating값이 null인 데이터들을 0으로 채워줌
movie_rating_pivot.fillna(0, inplace=True)
#movie_rating_pivot.head(10)

# 영화 평점(rating)으로 영화 간의 cosine similarity 계산
cf_itembased = cosine_similarity(movie_rating_pivot)

itembased_table = pd.DataFrame(data=cf_itembased, index=movie_rating_pivot.index, columns=movie_rating_pivot.index)
#itembased_table.head(5)

def recommend_movie(title):
    return itembased_table[title].sort_values(ascending=False)[1:6]

print(recommend_movie('Toy Story (1995)'))