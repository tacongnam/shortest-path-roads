import heapq
from structure import Graph, PartOfRoad

class ShortestPath:
    def query(graph: Graph, start_id: int, target_id: int):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start_id))  # (current_distance, node_id)
        distances = {node_id: float('inf') for node_id in graph.nodes}
        distances[start_id] = 0  # Distance starts from 0
        visited = set()
        previous_nodes = {start_id: None}  # Lưu node trước đó

        while priority_queue:
            current_distance, current_id = heapq.heappop(priority_queue)

            if current_id in visited:
                continue

            visited.add(current_id)

            if current_id == target_id:
                # Trả về đoạn đường ngắn nhất
                path = []
                while current_id is not None:
                    path.append(current_id)
                    current_id = previous_nodes[current_id]
                path.reverse()  # Đảo lại để có đường đi từ start_id đến target_id
                return distances[target_id] + graph.nodes[start_id].weight, path

            current_node = graph.get_node(current_id)

            for neighbor in current_node.edges:
                if neighbor.id not in visited:
                    travel_time = neighbor.weight
                    new_distance = current_distance + travel_time

                    if new_distance < distances[neighbor.id]:
                        distances[neighbor.id] = new_distance
                        previous_nodes[neighbor.id] = current_id  # Lưu lại node trước đó
                        heapq.heappush(priority_queue, (new_distance, neighbor.id))

        return float('inf'), []  # Nếu không tìm thấy đường đi, trả về vô cùng và đường đi rỗng
