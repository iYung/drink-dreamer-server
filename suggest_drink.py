import cPickle
import os

with open('ingredients', 'r') as fi:
    ingredients = cPickle.load(fi)

with open('matrix', 'r') as fi:
    matrix = cPickle.load(fi)

drink = [17, 21, 123]

scores = [0 for _ in range(len(ingredients))]

for ingredient in drink:
    row = matrix[ingredient]
    for idx in range(len(row)):
        if row[idx]:
            scores[idx] += row[idx]

indexedScores = enumerate(scores)
indexedScores = filter(lambda x: x[0] not in drink, indexedScores)
indexedScores = sorted(indexedScores, key=lambda x: x[1], reverse=True)

print "For an input of:"
for item in drink:
    print ingredients[item]

print "\nWe recommend:"
for idx in range(5):
    print ingredients[indexedScores[idx][0]], indexedScores[idx][1]