## Giới thiệu
- Thuật toán sử dụng Dijkstra tìm kiếm quãng đường đi ngắn nhất từ **đoạn đường A** đến **đoạn đường B**.
- Mỗi đỉnh là một đoạn đường, mỗi cạnh thể hiện tính kết nối giữa hai đoạn đường.
- Ví dụ quãng đường đi A -> B -> C -> D thì quy về (A, B) -> (B, C) -> (C, D).
- Lưu ý, trọng số của đỉnh (chiều dài, tốc độ trung bình) **không thể thay đổi** trong quá trình chạy thuật toán (tức chỉ được cập nhật trước / sau khi chạy).

## Hướng dẫn sử dụng
- Chạy file ./src/main.py
- File data/node.csv lưu thông tin node (đoạn đường) gồm vị trí bắt đầu, vị trí kết thúc, chiều dài quãng đường, tốc độ trung bình
- File data/connection.csv lưu thông tin kết nối (đoạn đường nào nối với đoạn đường nào) gồm hai chỉ số đoạn đường liên kết theo node.csv
- Mặc định vị trí lưu (savefile) là savefile/path.csv

## Hướng dẫn trường hợp chỉ muốn lấy kết quả:
+ Bước 1: Xuất node.csv và connection.csv ở thư mục data
+ Bước 2: Chạy lệnh
```java
python ./src/main.py
```
+ Bước 3: Lấy kết quả từ savefile/path.csv