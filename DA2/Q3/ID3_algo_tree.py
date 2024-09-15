import pandas as pd
import math
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

df = pd.read_csv(r"DA2\Q3\road_transport_records.csv")

def calculate_entropy(data, target_column):
    total_rows = len(data)
    target_values = data[target_column].unique()
    entropy = 0
    for value in target_values:
        value_count = len(data[data[target_column] == value])
        proportion = value_count / total_rows
        entropy -= proportion * math.log2(proportion) if proportion != 0 else 0
    return entropy

def calculate_information_gain(data, feature, target_column, entropy_outcome):
    unique_values = data[feature].unique()
    weighted_entropy = 0
    for value in unique_values:
        subset = data[data[feature] == value]
        proportion = len(subset) / len(data)
        weighted_entropy += proportion * calculate_entropy(subset, target_column)
    information_gain = entropy_outcome - weighted_entropy
    return information_gain

def id3(data, target_column, features):
    if len(data[target_column].unique()) == 1:
        return data[target_column].iloc[0]
    if len(features) == 0:
        return data[target_column].mode().iloc[0]
    entropy_outcome = calculate_entropy(data, target_column)
    best_feature = max(features, key=lambda x: calculate_information_gain(data, x, target_column, entropy_outcome))
    tree = {best_feature: {}}
    features = [f for f in features if f != best_feature]
    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        subtree = id3(subset, target_column, features)
        tree[best_feature][value] = subtree
    return tree

def plot_tree(tree, parent_name, graph, depth, max_depth):
    if depth > max_depth:
        return
    if isinstance(tree, dict):
        feature = list(tree.keys())[0]
        for value, subtree in tree[feature].items():
            node_name = f"{feature} = {value}"
            graph.add_node(node_name)
            graph.add_edge(parent_name, node_name)
            plot_tree(subtree, node_name, graph, depth + 1, max_depth)
    else:
        leaf_name = f"Accident Risk: {tree}"
        graph.add_node(leaf_name)
        graph.add_edge(parent_name, leaf_name)

def visualize_decision_tree(decision_tree, max_depth=3):
    graph = nx.DiGraph()
    root_name = list(decision_tree.keys())[0]
    graph.add_node(root_name)
    plot_tree(decision_tree, root_name, graph, 0, max_depth)
    plt.figure(figsize=(20, 15))
    pos = nx.spring_layout(graph, seed=42, k=0.5, iterations=50)
    nx.draw(graph, pos, with_labels=True, node_size=3500, node_color="lightblue", font_size=12, font_weight="bold", arrows=True, connectionstyle='arc3,rad=0.1')
    plt.title("Decision Tree Visualization")
    plt.show()

features = ['Length (km)', 'Number of Bends', 'Traffic Volume']
decision_tree = id3(df, 'Accident Risk', features)

print("\nGenerated Decision Tree using ID3 algorithm:")
print(decision_tree)

print("\n\nNow printing it-")
visualize_decision_tree(decision_tree)
