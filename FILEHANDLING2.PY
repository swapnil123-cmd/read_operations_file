file=open('code.txt','r')
print("1 lines: ")
print(file.readline())
file.close()

file=open('code.txt','r')
print("3 lines: ")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('code.txt','r')
print("ALL lines: ")
for line in file:
  print(line)
file.close

print("*"*100)
file1=open('code.txt','r')
file2=open('codingupdated.txt','w')

for line in file1.readlines():
  if not(line.startswith('Coding')):
    
    print(line)
    
    file2.write(line)

file2.close()
file1.close()
print("*"*100)

fn=open('code.txt','r')
fn1=open('newfile.txt','w')

cont=fn.readlines()
type(cont)

for i in range(1, len(cont)+1):
  if not(i % 2 == 0):
    fn1.write(cont[i-1])
  else:
    pass
  
fn1.close()
fn1=open('newfile.txt','r')
print(fn1.read())
fn1.close()
fn.close()