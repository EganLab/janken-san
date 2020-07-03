import numpy as np
import os
from PIL import Image
from mobilenet_v2 import mobilenet_v2, MobileNetV2
from torchvision import transforms
import torch
import torch.nn.functional as F
import cv2
import imutils


def preprocess_image(pil_image):
    val_tfms = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = val_tfms(pil_image)
    image = image.unsqueeze_(0).cpu()
    # image /= 255.00
    image = F.interpolate(image, size=256)
    return image


# Playing video from file:
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_POS_MSEC, 200)

currentFrame = 0

convert = {0: 'la', 1: 'dam', 2: 'keo'}
checkpoint = torch.load('MBN_epoch_1_loss_0.10.pth',
                        map_location=torch.device('cpu'))
# print(checkpoint)
model = MobileNetV2(num_classes=3)
model.load_state_dict(checkpoint)
# print(model)
model.eval()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)

        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        image1 = preprocess_image(frame)
        # print(image.shape)
        output = model(image1)
        # print(output)
        _, predicted = torch.max(output.data, 1)
        print(convert[int(predicted)])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # To stop duplicate images
        currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
