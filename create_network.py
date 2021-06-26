import _pickle as cPickle
import os
from pyvis.network import Network

#loading the ingredients and matrix
with open('ingredients', 'rb') as fi:
    ingredients = cPickle.load(fi)
with open('matrix', 'rb') as fi:
    matrix = cPickle.load(fi)

net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')
net.barnes_hut(gravity=-120000)

#create all nodes
for idx, ingredient in enumerate(ingredients):
    net.add_node(idx, label=ingredient)

#create set to prevent duplicate edges
existingEdges = set()

#create all edges
for sourceIdx, ingredient in enumerate(ingredients):
    for targetIdx in range(len(matrix[sourceIdx])):
        score = matrix[sourceIdx][targetIdx]
        if score > 0:
            pairing = (min(sourceIdx,targetIdx),max(sourceIdx,targetIdx))
            if pairing in existingEdges:
                pass
            else:
                existingEdges.add(pairing)
                net.add_edge(sourceIdx, targetIdx, value=score, title=score)

net.set_options('''var options = {
  "nodes": {
    "font": {
      "size": 30
    }
  },
  "edges": {
    "color": {
      "color": "rgba(32,115,233,1)",
      "highlight": "rgba(255,24,13,1)",
      "inherit": false
    },
    "smooth": false,
    "width": 1
  },
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -120000,
      "springLength": 250,
      "springConstant": 0.001,
      "avoidOverlap": 1
    },
    "minVelocity": 0.75
  }
}''')

# net.show_buttons(filter_=['nodes','edges', 'physics'])

net.show('drinks.html')