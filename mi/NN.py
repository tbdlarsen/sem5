import math


def sig(x):
    return 1/(1+math.exp(-x))


layers = [
    [1,5],
    [],
    []

]
weights = [
   [[1.3,1.7],[-0.3,1.0]],
   [[0.6,-1.4]]
]



for layer in range(1, len(layers)):
    prev_layer = layers[layer-1]
    layer_weights = weights[layer-1]
    current_layer_outputs = []

    num_nodes_this_layer = len(layer_weights)

    for node in range(num_nodes_this_layer):
        node_weights = layer_weights[node]
        node_input = 0
        for prev_node in range(len(prev_layer)):
            node_input += prev_layer[prev_node]*node_weights[prev_node]
        node_output = sig(node_input)
        current_layer_outputs.append(node_output)
    layers[layer] = current_layer_outputs


print(layers)





