from torch import nn


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # encoder (Resnet) 3 branches
        