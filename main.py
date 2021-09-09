import cv2
import torchvision
from telegram import bot_preparation, send_mes
from scripts import boxes_cor, get_glasses_boxes, get_glasses
import time
import argparse


def main():

    parser = argparse.ArgumentParser(description='code run params')
    parser.add_argument('--start_time', type=int, default=10,
                        help='the hour when program will start searching cups')
    parser.add_argument('--finish_time', type=int, default=23,
                        help='the hour when program will finish searching cups')
    parser.add_argument('--video_path', type=str, default='0',
                        help='path to the video. 0 - web camera')
    parser.add_argument('--time_freq', type=int, default=15,
                        help='The frequency with which the program will search for cups and send notifications if they are found. Default 15 minutes')
    parser.add_argument('--frame_amount', type=int, default=5,
                        help='The number of frames that must be processed at a time to predict the number of cups')
    parser.add_argument('--show', type=bool, default=False, help ='If it is True, the image from the camera will be displayed on the screen')

    parser.add_argument('--trashhold', type=float, default=0.25, help ='images with a probability below this threshold will not be considered')

    args = parser.parse_args()

    struct_time = time.localtime()

    bot, _, id = bot_preparation()
    print('bot is ready!')
    if args.video_path.isdigit():
        camera = int(args.video_path)
        cap = cv2.VideoCapture(camera)
    else:
        cap = cv2.VideoCapture(args.video_path)
    print('get camera/video succesfull!')
    model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_320_fpn(pretrained=True)

    print('model is ready!')
    while True:
        if (struct_time.tm_hour < args.finish_time) and (struct_time.tm_hour > args.start_time) and (struct_time.tm_min % args.time_freq == 0):
            mean_amount_of_cups = 0
            for i in range(args.frame_amount):

                _, image = cap.read()
                key = cv2.waitKey(10)
                if key == 27:
                    break

                boxes = get_glasses(model, image, args.trashhold)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                fontColor = (0, 255, 0)
                lineType = 1

                for box in boxes:
                    cv2.rectangle(image, box[0][0], box[0][1],
                                  (0, 255, 0), 3)  # draw box on image

                    bottomLeftCornerOfText = (box[0][0][0], box[0][1][1])

                    cv2.putText(image, 'proba: {:.3f}'.format(box[1]), bottomLeftCornerOfText, font,
                                fontScale, fontColor, lineType)  # add proba on image
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (0, 20)
                fontScale = 1
                fontColor = (0, 255, 0)
                lineType = 2

                cv2.putText(image, 'amount of cups: ' + str(len(boxes)),
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            lineType)

                if args.show:
                    cv2.imshow('image', image)

                mean_amount_of_cups += len(boxes)
            mean_amount_of_cups = mean_amount_of_cups / args.frame_amount

            if mean_amount_of_cups > 1.5:
            	send_mes(bot, id, image)


if __name__ == '__main__':
    main()
