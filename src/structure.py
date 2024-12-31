class PartOfRoad:
    def __init__(self, id: int, length: float, avg_speed: float, begin="", end=""):
        """
        Thông tin đoạn đường đang được thêm vào
        :param int id: Chỉ số của đoạn đường
        :param float length: Độ dài đoạn đường (km)
        :param float avg_speed: Tốc độ trung bình đoạn đường (km/h)
        :param str begin: Điểm đầu đoạn đường
        :param str end: Điểm cuối đoạn đường
        """
        self.id = id
        self.length = length
        self.avg_speed = avg_speed
        self.begin = begin
        self.end = end

class Node:
    def __init__(self, id: int, part_of_road: PartOfRoad):
        """
            Thông tin node
            :param int id: ID nút
            :param PartOfRoad: Đoạn đường ứng với nút
        """

        self.id = id
        self.road = part_of_road
        self.weight = self.get_weight()

        self.edges = []  # List of connected nodes (edges)
    
    def get_weight(self):
        if self.road.avg_speed == 0:
            raise ValueError("Tốc độ trung bình nhỏ hơn 0!")
        else:
            self.weight = self.road.length / self.road.avg_speed
            return self.weight
    
    def update_road(self, part_of_road: PartOfRoad):
        if self.road.id != part_of_road.id:
            raise ValueError("Đoạn đường đang sửa đổi không phù hợp với đoạn đường đang gán bởi node!")
        else:
            self.road = part_of_road
            self.weight = self.get_weight()

    def add_edge(self, neighbor):
        self.edges.append(neighbor)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id: int, part_of_road: PartOfRoad):
        if id not in self.nodes:
            self.nodes[id] = Node(id, part_of_road)

    def add_edge(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            self.nodes[id1].add_edge(self.nodes[id2])
        # Đồ thị là 1 chiều!

    def get_node(self, id):
        return self.nodes.get(id)