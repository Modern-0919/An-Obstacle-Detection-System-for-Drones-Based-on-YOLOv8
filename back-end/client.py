# 学习者：苗娃旦
# 最是人间留不住 朱颜辞镜花辞树
# 开发时间：2023/7/16 9:59
import requests
import glob

url = 'http://127.0.0.1:5003/remote_upload'  # 替换为服务器的实际地址
image_folder = './images'  # 替换为存储图像文件的文件夹路径

# 获取文件夹中所有图像文件的路径
image_files = glob.glob(image_folder + '/*.jpg')  # 可根据实际情况修改文件类型和路径

for file_path in image_files:
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)

    print(response.json())

