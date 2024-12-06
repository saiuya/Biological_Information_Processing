import chardet
from chardet import detect


def convert_to_utf8(input_file, output_file):
    try:
        # 检测文件的编码
        with open(input_file, "rb") as f:
            raw_data = f.read()
        detected_encoding = chardet.detect(raw_data)["encoding"]

        if detected_encoding is None:
            print("无法检测到文件编码，请确认文件是否为文本文件。")
            return

        if detected_encoding == "utf-8":
            print("源文件为utf-8")
            return

        print(f"检测到文件编码为: {detected_encoding}")

        # 使用检测到的编码读取文件
        with open(
            input_file, "r", encoding=detected_encoding, errors="ignore"
        ) as infile:
            content = infile.read()

        # 将内容写入到新文件，编码为 UTF-8
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(content)

        print(f"文件已成功转换为 UTF-8 编码并保存到: {output_file}")
    except Exception as e:
        print(f"转换失败: {e}")


# get file encoding type
def get_encoding_type(file):
    with open(file, "rb") as f:
        rawdata = f.read()
    return detect(rawdata)["encoding"]


# 示例用法
input_file_path = "../data/emg_myopathy_utf8.txt"  # 输入文件路径
output_file_path = "../data/emg_neuropathy_utf8.txt"  # 输出文件路径
convert_to_utf8(input_file_path, output_file_path)
print(f"转换后的文件编码为: {get_encoding_type("../data/emg_myopathy_utf8.txt")}")
