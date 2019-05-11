import cPickle
import os
import flask
from flask import request

with open('ingredients', 'r') as fi:
    ingredients = cPickle.load(fi)

with open('matrix', 'r') as fi:
    matrix = cPickle.load(fi)

app = flask.Flask(__name__)

@app.route('/ingredients', methods=['GET'])
def get_ingedients():
    response = {}
    response["ingredients"] = ingredients
    return flask.jsonify(response)

@app.route('/suggest', methods=['POST'])
def suggest():

    drink = request.get_json()['ingredients']
    response = {}
    scores = [0 for _ in range(len(ingredients))]

    for ingredient in drink:
        row = matrix[ingredient]
        for idx in range(len(row)):
            if row[idx]:
                scores[idx] += row[idx]

    indexedScores = enumerate(scores)
    indexedScores = filter(lambda x: x[0] not in drink, indexedScores)
    indexedScores = sorted(indexedScores, key=lambda x: x[1], reverse=True)

    bestIngredients = []
    for idx in range(min(5,len(indexedScores))):
        suggestion = {}
        suggestion["id"] = indexedScores[idx][0]
        suggestion["name"] = ingredients[indexedScores[idx][0]]
        bestIngredients.append(suggestion)
    
    return flask.jsonify(bestIngredients)