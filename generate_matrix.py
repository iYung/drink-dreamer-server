import requests
import sys
import cPickle
import os

ingredients = []
ingredientSets = []
startAt = 0

if os.path.isfile('ingredients'):
    with open('ingredients', 'r') as fi:
        ingredients = cPickle.load(fi)
    with open('ingredientSets', 'r') as fi:
        ingredientSets = cPickle.load(fi)
    startAt = len(ingredientSets) + 1
else:
    ingredientRequest = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list')

    for datum in ingredientRequest.json()['drinks']:
        ingredients.append(datum['strIngredient1'])
    with open('ingredients', 'wb') as fo:
        cPickle.dump(ingredients, fo)

for idx in range(startAt, len(ingredients)):

    print "getting " + str(idx)
    sys.stdout.flush()

    drinkRequest = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + ingredients[idx])

    newSet = set()
    for datum in drinkRequest.json()['drinks']:
        newSet.add(datum['idDrink'])
    ingredientSets.append(newSet)
    with open('ingredientSets', 'wb') as fo:
        cPickle.dump(ingredientSets, fo)
    print "added set " + str(idx)
    sys.stdout.flush()

matrix = []
for _ in range(len(ingredients)):
    matrix.append([0 for _ in range(len(ingredients))])

for start in range(len(ingredients) - 1):
    for idx in range(start + 1, len(ingredientSets)):
        matrix[start][idx] = len( ingredientSets[start].intersection(ingredientSets[idx]) )
        matrix[idx][start] = matrix[start][idx]

with open('matrix', 'wb') as fo:
    cPickle.dump(matrix, fo)