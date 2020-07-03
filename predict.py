from mobilenet_v2 import mobilenet_v2, MobileNetV2
from PIL import Image
from torchvision import transforms
import torch
import torch.nn.functional as F
import cv2
from imutils.video import VideoStream
import time
import imutils
import datetime


def preprocess_image(pil_image):
    val_tfms = transforms.Compose([
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


if __name__ == "__main__":
    ########################### Magic code line #################################
    vs = VideoStream(src=0).start()

    convert = {0: 'la', 1: 'dam', 2: 'keo'}
    checkpoint = torch.load('MBN_epoch_1_loss_0.10.pth',
                            map_location=torch.device('cpu'))
    # print(checkpoint)
    model = MobileNetV2(num_classes=3)
    model.load_state_dict(checkpoint)
    # print(model)
    model.eval()
    # Your image here
    while True:
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale, and blur it
        time.sleep(200)
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        # grab the current timestamp and draw it on the frame
        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        image1 = preprocess_image(frame)
        # print(image.shape)
        output = model(image1)
        # print(output)
        _, predicted = torch.max(output.data, 1)
        print(convert[int(predicted)])
