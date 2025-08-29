import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('path')  #The relative path is: ultralytics-main\ultralytics\cfg\models\RCS-YOLO\RLS-YOLO.yaml
    model.train(data='path',#The relative path is: ultralytics-main\dataset\data.yaml
                cache=False,
                imgsz=640,
                epochs=10,
                batch=8,
                close_mosaic=0,
                workers=0, 
                # device='0',
                # optimizer='SGD', # using SGD
                patience=500, # set 0 to close earlystop.
                # resume=True, 
                # amp=False, # close amp
                # fraction=0.2, 
                project='runs/train',
                name='RLS-YOLOv8',
                )