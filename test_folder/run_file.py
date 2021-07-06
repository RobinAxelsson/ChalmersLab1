import os 

filepath = ''
folder = os.getcwd().split('\\')[-1]
print(folder)

if folder == 'test_folder':
    filepath = '../eng_stopwords.txt'
elif folder == 'lab1':
    filepath = 'eng_stopwords.txt'

# filepath = 'eng_stopwords.txt'
with open(filepath, 'r', encoding="utf-8") as f:
        print(f.read())