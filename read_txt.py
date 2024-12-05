
# 定义一个函数读取文件并解析数据
def read_emg_data(file_path):
    time = []
    value = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:  # 确保每行有两个值
                try:
                    time.append(float(parts[0]))
                    value.append(float(parts[1]))
                except ValueError:
                    if len(time) > len(value):
                        time.pop()
                    if len(time) < len(value):
                        value.pop()
                    continue
        return time, value