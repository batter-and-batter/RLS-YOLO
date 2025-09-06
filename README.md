# RLS-YOLO
RLS-YOLO is a lightweight braille block damage detection algorithm based on an improved YOLOv8n architecture, designed for high-precision, low-power real-time detection on embedded devices.


## Model
The project files is modified based on the [YOLOv8](https://github.com/ultralytics/ultralytics) project. The model configuration file [RLS-YOLO.yaml](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/ultralytics/cfg/models/RCS-YOLO/RLS-YOLO.yaml) is located in the directory [./ultralytics-main/ultralytics/cfg/models](https://github.com/batter-and-batter/RLS-YOLO/tree/master/ultralytics-main/ultralytics/cfg/models).

### Recommended Configuration
- Python: 3.8
- Torch: 1.13.1
- Torchvision: 0.14.1

## Training
Run the [train.py](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/train.py) file. The default hyperparameters are located in the [./ultralytics/cfg/default.yaml](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/ultralytics/cfg/default.yaml) file.
**Note**: Please modify the model path and [data.yaml](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/dataset/data.yaml) file path in [train.py](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/train.py) as needed. The default location for [data.yaml](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/dataset/data.yaml) is [./dataset](https://github.com/batter-and-batter/RLS-YOLO/tree/master/ultralytics-main/dataset). The dataset format is the same as that used in the YOLOv8 project, so be sure to modify [data.yaml](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/dataset/data.yaml) to point to your dataset location.

## Validation
Run the [val.py](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/val.py) file. The modification method is consistent with training.

## Inference on Images
Run the [detect.py](https://github.com/batter-and-batter/RLS-YOLO/blob/master/ultralytics-main/detect.py) file. The modification method is consistent with training.

## Evaluation
We have trained and evaluated RLS-YOLO on the [self built dataset](https://github.com/batter-and-batter/RLS-YOLO/tree/master/ultralytics-main/dataset), which is included in the project. The trained model weights file is located at [./weight/RLS-YOLO](https://github.com/batter-and-batter/RLS-YOLO/tree/master/ultralytics-main/weight/RLS-YOLO).

## Ablation Experiments
For the ablation experiments described in the paper, the model weights files are located in the [./weight/ablation](https://github.com/batter-and-batter/RLS-YOLO/tree/master/ultralytics-main/weight/ablation) folder.

## Copyright Notice
Many utility codes of our project are based on the codes from the [ultralytics](https://github.com/ultralytics/ultralytics), [Large Separable Kernel Attention](https://github.com/StevenLauHKHK/Large-Separable-Kernel-Attention), [Shape-IoU](https://github.com/malagoutou/Shape-IoU) and [RCS-YOLO](https://github.com/mkang315/RCS-YOLO) repositories.

