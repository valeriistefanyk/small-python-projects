import subprocess
calcProc = subprocess.Popen(r'C:\Windows\System32\calc.exe')
res = calcProc.poll() == None
print(res)
calcProc.wait()
calcProc.poll()

subprocess.Popen([r'C:\Windows\System32\notepad.exe', r'C:\hello.txt'])
subprocess.Popen([r'C:\Python38\python.exe', 'hello.py'])


with open('hello.txt', 'w') as fileObj:
    fileObj.write('Привет мир!')
subprocess.Popen(['start', 'hello.txt'], shell=True)
