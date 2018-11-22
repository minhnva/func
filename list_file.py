#!/usr/bin/python3
import os


# 1 .lấy đường dẫn của file trong thư mục
# kt đường dẫn  tuyệt đối
# 2. lấy hết file trong thư mục bỏ vào list
# thư mục không có file thì bỏ qua
# 3 : add từng file vào list



def get_all_file(dir_file_name):
    all_file_path = []
    if os.path.isdir(os.path.abspath(dir_file_name)):  # 1
        for root, dirs, files in os.walk(dir_file_name):  # 2
            for name in files:
                path_file = os.path.join(root, name)
                all_file_path.append(path_file)
        return all_file_path
    else:  # 3
        all_file_path.append(dir_file_name)
        return all_file_path


if __name__ == '__main__':
    print(get_all_file('min'))
