from ch import ShortestPath as SP
from structure import Graph, Node, PartOfRoad
import pandas as pd
import argparse

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo đồ thị mẫu
    graph = Graph()

    parser = argparse.ArgumentParser(description="Process graph nodes and connections along with a range.")

    parser.add_argument("--begin", type=int, required=True, help="The starting integer (required)")
    parser.add_argument("--end", type=int, required=True, help="The ending integer (required)")
    parser.add_argument("--node", nargs="?", default=None, help="Optional node information (can be empty)")
    parser.add_argument("--connection", nargs="?", default=None, help="Optional connection information (can be empty)")

    args = parser.parse_args()

    if args.node != None:
        df = pd.read_csv(f'data/{args.node}')
    else:
        df = pd.read_csv('data/node.csv')

    for index, row in df.iterrows():
        road = PartOfRoad(index, row['length'], row['avg_speed'], row['begin'], row['end'])
        graph.add_node(index, road)
    
    if args.connection != None:
        df = pd.read_csv(f'data/{args.connection}')
    else:
        df = pd.read_csv('data/connection.csv')

    for _, row in df.iterrows():
        graph.add_edge(row['begin'], row['end'])

    i_begin = args.begin
    i_end = args.end

    value, path = SP.query(graph, i_begin, i_end)
    print(f'Quãng đường ngắn nhất từ {graph.nodes[i_begin].road.begin} đến {graph.nodes[i_end].road.end} là: {round(value * 60, 2)} phút')
    
    for node in path:
        print(f'{graph.nodes[node].road.begin} => {graph.nodes[node].road.end} ({round(graph.nodes[node].road.length / graph.nodes[node].road.avg_speed * 60, 2)} phút ; {round(graph.nodes[node].road.length)} km)')