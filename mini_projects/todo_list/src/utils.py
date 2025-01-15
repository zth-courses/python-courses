#工具函数，文件读写、日期格式化等

def read_file(file_path):
   try:
      with open(file_path, "a+", encoding='utf-8') as file:
          file.seek(0)
          content = file.readlines()
          if not content:
              print("文件为空")
              # file.write('hello world')
              return None
          else:
              print(content)
              return content
   except FileNotFoundError as e:
       print(f"文件操作失败: {e}")

def write_file(file_path, content):
    try:
        with open(file_path, "a+", encoding='utf-8') as file:
            file.write(content)
    except FileNotFoundError as e:
        print(f"文件操作失败: {e}")

"""
open() 函数的模式参数可以控制文件的行为：

"r"：只读模式（文件必须存在）。

"w"：写入模式（如果文件不存在则创建，如果文件存在则清空内容）。

"a"：追加模式（如果文件不存在则创建，如果文件存在则在末尾追加内容）。

"x"：独占创建模式（如果文件不存在则创建，如果文件存在则抛出异常）。

"r+"：读写模式（文件必须存在）。

"w+"：读写模式（如果文件不存在则创建，如果文件存在则清空内容）。

"a+"：读写模式（如果文件不存在则创建，如果文件存在则在末尾追加内容）。
"""