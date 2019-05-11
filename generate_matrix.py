import requests
import sys
import cPickle
import os

#variables to store the name of each ingredient and each set
#each set is a set of all drink ids that use that ingredient
ingredients = []
ingredientSets = []
#variable to keep track which ingredient was last used to call the database
startAt = 0

#checks if script has been called before
#if so, loads the files
if os.path.isfile('ingredients'):
    with open('ingredients', 'r') as fi:
        ingredients = cPickle.load(fi)
    with open('ingredientSets', 'r') as fi:
        ingredientSets = cPickle.load(fi)
    startAt = len(ingredientSets) + 1
else:
    ingredientRequest = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list')
    #gets the name of each ingredient
    for datum in ingredientRequest.json()['drinks']:
        ingredients.append(datum['strIngredient1'])
    with open('ingredients', 'wb') as fo:
        cPickle.dump(ingredients, fo)

#creates a set for each ingredient and fills the set with drink ids
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

#variable to store the scores
#is a 2d matrix
matrix = []

#intializes the matrix to 0
for _ in range(len(ingredients)):
    matrix.append([0 for _ in range(len(ingredients))])

#compares each set to each other set
#the common elements between each set is used as the score for that relationship
for start in range(len(ingredients) - 1):
    for idx in range(start + 1, len(ingredientSets)):
        matrix[start][idx] = len( ingredientSets[start].intersection(ingredientSets[idx]) )
        matrix[idx][start] = matrix[start][idx]
        
#saves the matrix
with open('matrix', 'wb') as fo:
    cPickle.dump(matrix, fo)