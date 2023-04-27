import cv2
import numpy as np
import torch
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_boxes
from utils.plots import Annotator, colors, save_one_box
from models.common import DetectMultiBackend


def detect(img0):
    weights = 'yolov5s.pt'
    w = str(weights[0] if isinstance(weights, list) else weights)
    model = DetectMultiBackend(weights)
    names = model.names
    height, width = 640, 640

    img = cv2.resize(img0, (height, width))    # 尺寸变换
    img = img / 255
    img = img[:, :, ::-1].transpose((2, 0, 1))   # HWC转CHW
    img = np.expand_dims(img, axis=0)    # 扩展维度至[1,3,640,640]
    
    img = torch.from_numpy(img.copy())   # numpy转tensor
    img = img.to(torch.float32)          # float64转换float32
    

    pred = model(img, augment='store_true', visualize='store_true')[0]
    pred = non_max_suppression(pred, 0.25, 0.45, None, False, max_det=1000)  # 非极大值抑制
    
    annotator = Annotator(img0, line_width=3, example=str(names))
    for i, det in enumerate(pred):
        if len(det):
            det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], img0.shape).round()
            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                label = None if False else (names[c] if False else f'{names[c]} {conf:.2f}')
                annotator.box_label(xyxy, label, color=colors(c, True))
                   

    # print(img0.shape)
    # 存储im0
    cv2.imwrite('im0.jpg', img0)
    return img0

if __name__ == "__main__":
    # 读取摄像头
    cap = cv2.VideoCapture(0)
    while True:
        ret, img0 = cap.read()
        img = detect(img0)
        cv2.imshow('img', img)
        cv2.waitKey(1)

# if __name__ == "__main__":
#     weights = 'yolov5s.pt'
#     w = str(weights[0] if isinstance(weights, list) else weights)
#     model = torch.jit.load(w) if 'torchscript' in w else attempt_load(weights, device='cpu')   #加载模型
#     height, width = 640, 640
#     # 读取摄像头
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, img0 = cap.read()
#         img = cv2.resize(img0, (height, width))    #尺寸变换
#         img = img / 255.
#         img = img[:, :, ::-1].transpose((2, 0, 1))   #HWC转CHW
#         img = np.expand_dims(img, axis=0)    #扩展维度至[1,3,640,640]
#         img = torch.from_numpy(img.copy())   #numpy转tensor
#         img = img.to(torch.float32)          #float64转换float32
#         pred = model(img, augment='store_true', visualize='store_true')[0]
#         pred.clone().detach()
#         pred = non_max_suppression(pred, 0.25, 0.45, None, False, max_det=1000)  #非极大值抑制
#         for i, det in enumerate(pred):
#             if len(det):
#                 det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], img0.shape).round()
#                 for *xyxy, conf, cls in reversed(det):
#                     print('{},{},{}'.format(xyxy, conf.numpy(), cls.numpy())) #输出结果：xyxy检测框左上角和右下角坐标，conf置信度，cls分类结果
#                     img0 = cv2.rectangle(img0, (int(xyxy[0].numpy()), int(xyxy[1].numpy())), (int(xyxy[2].numpy()), int(xyxy[3].numpy())), (0, 255, 0), 2)
#                     # img0.imshow()
#                     cv2.imshow('img', img0)
#                     cv2.waitKey(1)