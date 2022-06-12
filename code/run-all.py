import os
import runpy

path = '.'
allflst = os.listdir(path)
#print(allflst)

pyflst = [file for file in allflst if file.endswith(".py") and file not in 'run-all.py']
#print(pyflst)

# 현재 폴더의 모든 파일(자신 파일 run-all.py 제외) 실행
for f in pyflst:
    print('======> 실행: ' + f + '\n')
    runpy.run_path(f)
    print('\n' + '======> 완료: ' + f + '\n')

