from torchvision import models, transforms
import torch
from PIL import Image

def image_class(img1):
    resnet = models.resnet50(pretrained=True)
    transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

    img = Image.open(img1)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    resnet.eval()
    out = resnet(batch_t)

    with open('util/imagenet_classes.txt') as f:
        classes = [line.strip().split(',')[1] for line in f.readlines()]

    _, index = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0]*100

    return classes[index], round(percentage[index].item(), 2)