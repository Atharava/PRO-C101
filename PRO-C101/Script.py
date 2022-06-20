#Setup
from CloudStorage import TranferData
import os

def main(accToken):
    access_token = accToken
    trnfr = TranferData(access_token)

    srcList = input("Enter Folder (Folder1): ")
    
    for file in os.listdir(srcList):
        src = srcList+'/'+file
        dst = '/Atharva\'s Files/'+file
        trnfr.upload_file(src, dst)
        print(f'File {file} has moved')
    print('All files have been moved!')

#Display
for i in range(1, 2):
    print("\n")
    
    try:
        main() #Add access token here in single quotes
    except:
        print('Access token not entered (in Script.py)')

for i in range(1, 2):
    print("\n")