# 读取文件，并返回文件内容，如果文件不存在，就先创建 
file_path = 'files.txt'

# 使用 "a+" 模式打开文件（如果文件不存在则创建）
def read_file(file_path):
   try:
      with open(file_path, "a+", encoding='utf-8') as file:
          file.seek(0)
          content = file.readlines()
          if not content:
              print("文件为空")
              file.write('hello world')
              return 'hello world'
          else:
              print(content)
              return content
   except FileNotFoundError as e:
       print(f"文件操作失败: {e}")
read_file(file_path)
