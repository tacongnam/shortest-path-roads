```python
pip install -r requirements.txt

python ./src/main.py --begin=<id road 1> --end=<id road 2> --node=<file node> --connection=<file connection> --save=<file save>
```

- begin: id đoạn đường bắt đầu (thứ tự trong file node)
- end: id đoạn đường kết thúc (thứ tự trong file node)
- node (optional): tên file node, hệ thống sẽ load từ: data/{tên file node}. Mặc định nếu không thiết lập là data/node.csv
- connection (optional): tên file connection, hệ thống sẽ load từ: data/{tên file connection}. Mặc định nếu không thiết lập là data/connection.csv
- save (optional): tên file save, hệ thống sẽ save kết quả dưới dạng csv ở: savefile/{tên file save}. Mặc định nếu không thiết lập sẽ in kết quả ra màn hình

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