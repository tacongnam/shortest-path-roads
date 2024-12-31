```python
pip install -r requirements.txt

python ./src/main.py <id road 1> <id road 2>
```

## Yêu cầu file input
- File input cho thuật toán bao gồm data/node.csv và data/connection.csv

- File data/node.csv chứa thông tin các đoạn đường, bao gồm:
```csv
begin,end,length,avg_speed
Hill Main Court,River Oak Road,7.71,26.26
Lakeside Central Road,Mountain South Lane,1.36,33.79
...
```

- File data/connection.csv chứa thông tin các kết nối, bao gồm:
```csv
begin,end
0,29
0,47
...
```

- Giá trị của begin và end tương ứng với chỉ số hai đoạn đường kết nối từ file node.csv.

- Để fake data, chạy file
```python
python ./src/generate.py
```