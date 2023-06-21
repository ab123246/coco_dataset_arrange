#### 警語 內含大量免洗code
## 1.到coco dataset的網站下載自己需要的資料
https://cocodataset.org/#download

記得要下載annotations

## 2.確認1train_extract_object.py裡的 annotations和image的位置

```
COCO_ANNOTATIONS_PATH = current_path + "/annotations/instances_train2017.json"
COCO_IMAGES_DIRECTORY = current_path + "/train2017/"
EXTRACTED_SAVING_PATH = current_path + "/extracted_train_dataset/"
SAVE_FOLDER = EXTRACTED_SAVING_PATH.split('/')[len(EXTRACTED_SAVING_PATH.split('/'))-2]
```


```
touch classes.txt
```
在classes裡面加入自己需要的物件名稱
例如
```
person
car
```
執行
```
python train_extract_object.py
```

```
cd extracted_train_dataset && ls
```


執行完成之後會出現extracted_train_dataset的資料夾
資料就會被分離出來了
注意：不要用gui打開extracted_train_dataset的資料夾 很有可能會當掉

建立資料夾把資料分類
```
mkdir images && mv *.jpg images/ && mkdir annotations && mv *.xml annotations/ 
```
## 3. 回到根目錄 執行train_create_list.py
```
python train_create_list.py
```
## 4. 執行train_create_txt.py
```
python train_create_txt.py
```

