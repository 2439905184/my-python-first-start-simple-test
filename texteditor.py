#coding=utf-8
print("欢迎使用python命令行编辑器")
print("输入r进入只读模式,输入w进入覆盖编辑模式")
text_in=raw_input()
if('r' in text_in):
  print('你选择了r模式')
  print('请输入要读取的文本文件路径')
  url=raw_input()
  file=open(url)
  print(file.read())