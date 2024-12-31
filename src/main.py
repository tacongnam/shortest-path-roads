from ch import ShortestPath as SP
from structure import Graph, Node, PartOfRoad
import pandas as pd

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo đồ thị mẫu
    graph = Graph()

    df = pd.read_csv('data/node.csv')

    for index, row in df.iterrows():
        road = PartOfRoad(index, row['length'], row['avg_speed'], row['begin'], row['end'])
        graph.add_node(index, road)
    
    df = pd.read_csv('data/connection.csv')

    for _, row in df.iterrows():
        graph.add_edge(row['begin'], row['end'])

    i_begin = int(input())
    i_end = int(input())

    value, path = SP.query(graph, i_begin, i_end)
    print(f'Quãng đường ngắn nhất từ {graph.nodes[i_begin].road.begin} đến {graph.nodes[i_end].road.end} là: {round(value * 60, 2)} phút')
    for node in path:
        print(f'{graph.nodes[node].road.begin} => {graph.nodes[node].road.end} ({round(graph.nodes[node].road.length / graph.nodes[node].road.avg_speed * 60, 2)})')