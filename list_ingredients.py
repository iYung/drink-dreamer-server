import cPickle
import os
import sys

with open('ingredients', 'r') as fi:
    ingredients = cPickle.load(fi)

indexedIngredients = enumerate(ingredients)

if len(sys.argv) != 1:
    indexedIngredients = filter(lambda x: (' '.join(sys.argv[1:])).lower() in x[1].lower(), indexedIngredients)

for idx, ingredient in indexedIngredients:
    print idx, ingredient