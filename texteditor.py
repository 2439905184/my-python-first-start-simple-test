#coding=utf-8
while(True):
  print("��ӭʹ�ñ��༭����������ģʽ��rΪ��ֻ��,a+Ϊ׷�ӱ༭ģʽ,�ļ��������,����exit���˳�")
  text_in=raw_input()
  if('r' in text_in):
    print("�������ļ�·��")
    url=raw_input()
    file=open(url)
    print(file.read())
    file.close()
    print("�����������в���,����exit���˳�")
    url=raw_input()
    if('exit' in url):
      print("��ӭ�ٴ�ʹ�ñ�ϵͳ")
      break
    else:
	  continue
  if('exit' in text_in):
	break
  elif('a+' in text_in):
    print("�������ļ�·��")
    url=raw_input()
    file=open(url,'a+')
    print("����I��ʽ��ʼ�༭����ʱֻ֧��׷�ӣ���֧��ɾ�����֣�")
    text_in=raw_input()
    if('i' in text_in):
        text_in=raw_input()
        if(text_in):
          file.write(text_in)
          file.close()
          print("������ϣ������Զ�����")
          print("��ӭ�ٴ�ʹ�ñ�ϵͳ")