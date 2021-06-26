import _pickle as cPickle
import os
import sys

#loading ingredients
with open('ingredients', 'rb') as fi:
    ingredients = cPickle.load(fi)

#added the id to each ingredient
indexedIngredients = enumerate(ingredients)

#looks for a command line argument to filter by
if len(sys.argv) != 1:
    indexedIngredients = filter(lambda x: (' '.join(sys.argv[1:])).lower() in x[1].lower(), indexedIngredients)

#prints all ingredients that pass the filter
for idx, ingredient in indexedIngredients:
    print(idx, ingredient)