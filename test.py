#coding=utf-8
import sys
type=sys.getfilesystemencoding()
print("请输入文件路径").decode('utf-8').encode(type)
file_path=raw_input()
file=open(file_path)
#r只读模式
print(file.read())
file.close()
