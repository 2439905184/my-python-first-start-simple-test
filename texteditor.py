#coding=utf-8
while(True):
  print("欢迎使用本编辑器，请输入模式：r为打开只读,a+为追加编辑模式,文件必须存在,输入exit来退出")
  text_in=raw_input()
  if('r' in text_in):
    print("请输入文件路径")
    url=raw_input()
    file=open(url)
    print(file.read())
    file.close()
    print("请继续输入进行操作,输入exit来退出")
    url=raw_input()
    if('exit' in url):
      print("欢迎再次使用本系统")
      break
    else:
	  continue
  if('exit' in text_in):
	break
  elif('a+' in text_in):
    print("请输入文件路径")
    url=raw_input()
    file=open(url,'a+')
    print("输入I正式开始编辑（暂时只支持追加，不支持删除文字）")
    text_in=raw_input()
    if('i' in text_in):
        text_in=raw_input()
        if(text_in):
          file.write(text_in)
          file.close()
          print("输入完毕，现已自动保存")
          print("欢迎再次使用本系统")