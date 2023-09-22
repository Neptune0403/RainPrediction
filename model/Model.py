from torch import nn

from model.resnet import resnet50


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # encoder (Resnet) 3 branches
        resnet = resnet50(pretrained=False)re
        rene