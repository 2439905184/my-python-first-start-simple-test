#coding=utf-8
print("��ӭʹ��python�����б༭��")
print("����r����ֻ��ģʽ,����w���븲�Ǳ༭ģʽ")
text_in=raw_input()
if('r' in text_in):
  print('��ѡ����rģʽ')
  print('������Ҫ��ȡ���ı��ļ�·��')
  url=raw_input()
  file=open(url)
  print(file.read())