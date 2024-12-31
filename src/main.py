from ShortestPath import ShortestPath as SP
from structure import Graph, Node, PartOfRoad
import pandas as pd
import argparse
import os

def save_path(path, graph, filename):
    edges = []

    columns = ['id', 'begin', 'end', 'length', 'avg_speed', 'time']

    for node in path:
        edges.append([node, graph.nodes[node].road.begin, graph.nodes[node].road.end, round(graph.nodes[node].road.length, 2), round(graph.nodes[node].road.avg_speed, 2), round(graph.nodes[node].road.length / graph.nodes[node].road.avg_speed, 2)])
    
    df = pd.DataFrame(edges, columns=columns)

    if not os.path.exists('savefile'):
        # If it doesn't exist, create it
        os.makedirs('savefile')
        print(f"Directory 'savefile' created.")

    df.to_csv(f'savefile/{filename}', index=False, encoding='utf-8')
    
def query(begin, end, graph = None, node='node.csv', connection='connection.csv', savefile='path.csv'):
    # Nếu không có thì tạo đồ thị từ các file:
    if graph == None:
        graph = Graph()

        df = pd.read_csv(f'data/{node}')
    
        for index, row in df.iterrows():
            road = PartOfRoad(index, row['length'], row['avg_speed'], row['begin'], row['end'])
            graph.add_node(index, road)
        
        df = pd.read_csv(f'data/{connection}')
        
        for _, row in df.iterrows():
            graph.add_edge(row['begin'], row['end'])
    else:
        graph = graph

    i_begin = begin
    i_end = end

    value, path = SP.query(graph, i_begin, i_end)
    print(f'Quãng đường ngắn nhất từ {graph.nodes[i_begin].road.begin} đến {graph.nodes[i_end].road.end} là: {round(value * 60, 2)} phút')

    for node in path:
        print(f'{graph.nodes[node].road.begin} => {graph.nodes[node].road.end} ({round(graph.nodes[node].road.length / graph.nodes[node].road.avg_speed * 60, 2)} phút ; {round(graph.nodes[node].road.length)} km)')

    save_path(path, graph, savefile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process graph nodes and connections along with a range.")

    parser.add_argument("--begin", type=int, required=True, help="The starting integer (required)")
    parser.add_argument("--end", type=int, required=True, help="The ending integer (required)")
    
    args = parser.parse_args()

    query(args.begin, args.end)
