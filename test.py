import re
import math


print('Type A Movie')
users_input=input()

def euclidian_distance(dataset, user1, user2):
    sum_euclidian = sum([math.pow(dataset[user1][item]-dataset[user2][item],2) for item in dataset[user1] if item in dataset[user2]])
    return 1/ (1+ math.sqrt(sum_euclidian))


def get_similarities(dataset,user):
    similarity = [(euclidian_distance(dataset,user,other),other) for other in dataset if other != user]
    similarity.sort()
    similarity.reverse()
    return similarity

def calculate_items_similarities(dataset):
    similarities = {}
    for item in dataset:
        similarity = get_similarities(dataset,item)
        similarities[item] = similarity
    return similarities


def load_movielens():
    movies = {}
    for row in open('/Users/michaelmaske/Desktop/Projects/chick-fil-a/python/movie_recommender/u.item',encoding = 'ISO-8859-1'):
        (id, name) = row.split('|')[0:2]
        title = re.sub(r" ?\([^)]+\)", "", name)
        movies[id] = title


    dataset = {}
    for row in open('/Users/michaelmaske/Desktop/Projects/chick-fil-a/python/movie_recommender/u.data'):
        (user, movie_id, score, time) = row.split('\t')
        dataset.setdefault(movies[movie_id], {})
        dataset[movies[movie_id]][user] = float(score)
    return dataset

movie_lens_dataset_item = load_movielens()

item_similarities = calculate_items_similarities(movie_lens_dataset_item)


print(item_similarities[users_input][0:10])




