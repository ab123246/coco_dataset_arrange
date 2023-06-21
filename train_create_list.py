import os
current_path = os.path.abspath(os.getcwd())
arr = os.listdir(current_path+'/extracted_train_dataset/images')
f=open(current_path+'/trainlist.txt','w')
for ann in arr:
    f.write(ann.split('.')[0]+'\n')
f.close()

