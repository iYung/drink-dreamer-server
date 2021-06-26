import _pickle as cPickle
import os

#loading the ingredients and matrix
with open('ingredients', 'rb') as fi:
    ingredients = cPickle.load(fi)
with open('matrix', 'rb') as fi:
    matrix = cPickle.load(fi)

#input drinks
drink = [17, 21, 98]

#set a scores array for each ingredient, all set to 0
scores = [0 for _ in range(len(ingredients))]

#for each input drink, add up its scores to the score array
for ingredient in drink:
    row = matrix[ingredient]
    for idx in range(len(row)):
        if row[idx]:
            scores[idx] += row[idx]

#filtering and sorting scores to find the best ingredients
indexedScores = enumerate(scores)
indexedScores = filter(lambda x: x[0] not in drink, indexedScores)
indexedScores = sorted(indexedScores, key=lambda x: x[1], reverse=True)

print("For an input of:")
for item in drink:
    print(ingredients[item])

print("\nWe recommend:")
for idx in range(5):
    print(ingredients[indexedScores[idx][0]], indexedScores[idx][1])