from torchvision import transforms


def boxes_cor(i, predicition):  # return left bottom point (x1, y1) and right top point (x2, y2)

    return (int(predicition[0]['boxes'][i][0].item()), int(predicition[0]['boxes'][i][1].item())), \
           (int(predicition[0]['boxes'][i][2].item()),
            int(predicition[0]['boxes'][i][3].item()))


# return the list of boxes in format: [(coord, proba), ..., ]
def get_glasses_boxes(predicition):
    boxes = []
    for i in range(len(predicition[0]['boxes'])):
        if predicition[0]['labels'][i] == 47 and predicition[0]['scores'][i].item() > 0.5:
            boxes.append((boxes_cor(i, predicition),
                         predicition[0]['scores'][i].item()))
    return boxes


def get_glasses(model, img):
    trans = transforms.ToTensor()
    img = trans(img)
    model.eval()
    x = [img]
    prediction = model(x)
    return get_glasses_boxes(prediction)
