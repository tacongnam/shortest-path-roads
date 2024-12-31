import pandas as pd
import random
from tqdm import tqdm

num_nodes = 100
num_roads = 40

def generate_road_name():
    # List of road name components
    directions = ['North', 'South', 'East', 'West', 'Central', 'Main', 'Park', 'River', 'Oak', 'Hill']
    types = ['Street', 'Avenue', 'Road', 'Boulevard', 'Drive', 'Lane', 'Way', 'Trail', 'Circle', 'Court']
    landmarks = ['Sunset', 'Maple', 'Pine', 'Lakeside', 'Mountain', 'River', 'Valley', 'Hill', 'Bridge', 'Forest']
    
    direction = random.choice(directions)
    type_ = random.choice(types)
    landmark = random.choice(landmarks)
    road_name = f"{landmark} {direction} {type_}"
    return road_name

def generate_map(locations):
    mask = []
    for i in range(num_roads):
        mask.append(i)
    random.shuffle(mask)

    edges = []

    # Tạo đồ thị liên thông bằng cách thêm các cạnh nối các node liên tiếp
    for i in range(num_roads - 1):
        edges.append([mask[i], mask[i + 1]])  # Tạo các cạnh nối từ node i tới node i+1

    # Shuffling edges để chọn ngẫu nhiên các cạnh ngược lại
    random.shuffle(edges)

    l = len(edges)
    
    for i in range(l, num_nodes):
        while True:
            begin_it = random.randrange(0, len(locations))
            end_it = random.randrange(0, len(locations))

            if begin_it != end_it and [mask[begin_it], mask[end_it]] not in edges:
                edges.append([mask[begin_it], mask[end_it]])
                break

    return edges      

def generate_nodes(map, locations):
    nodes = []

    columns = ['begin', 'end', 'length', 'avg_speed']

    for edge in tqdm(map, desc="Đang thêm dữ liệu", unit="dữ liệu"):
        begin_it = edge[0]
        end_it = edge[1]

        location_begin = locations[begin_it]
        location_end = locations[end_it]

        length = round(random.uniform(0.5, 10.0), 2)
        speed = round(random.uniform(20.0, 40.0), 2)

        nodes.append([location_begin, location_end, length, speed])

    df = pd.DataFrame(nodes, columns=columns)

    df.to_csv('data/node.csv', index=False, encoding='utf-8')

    return nodes

def generate_edges(nodes, locations):
    edges = []

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j and nodes[i][1] == nodes[j][0]:
                edges.append([i, j])

    df = pd.DataFrame(edges, columns=["begin", "end"])

    # Lưu file CSV
    df.to_csv('data/connection.csv', index=False, encoding='utf-8')

    print(f"Đồ thị liên thông đã được tạo và lưu vào 'connection.csv'.")


locations = [generate_road_name() for _ in range(num_roads)]
map = generate_map(locations)
nodes = generate_nodes(map, locations)
generate_edges(nodes, locations)