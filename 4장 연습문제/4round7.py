f=open("test.txt",'r')
body=f.read()
f.close()

body= body.replace('java','python')

f=open("test2.txt",'w')
f.write(body)
f.close()