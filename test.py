import os
print("请输入文件路径,必须要加上双引号,暂时只支持文本文件!")
s=raw_input()
file=open(s,r)
#r只读模式
file.read()
file.close()
