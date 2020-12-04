import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F


class La3net(nn.Module):
    """ TODO
    """
    def __init__(self):
        super(La3net, self).__init__()
        vgg16 = models.vgg16(pretrained=True)
        self.features = vgg16.features
        self.cos_similarity = nn.CosineSimilarity(dim=1, eps=1e-6)

    def forward(self, inputs, target):
        # Extract input features
        input_features = self.features(inputs)
        b, c, h, w = input_features.size()
        input_features = input_features.view(-1, c*h*w)

        # Extract target features
        target_features = self.features(target)
        b, c, h, w = target_features.size()
        target_features = target_features.view(-1, c*h*w)

        x = self.cos_similarity(input_features, target_features)
        return x


class AE(nn.Module):
    """ TODO
    """
    def __init__(self):
        super(AE, self).__init__()
        # Input size: [batch, 3, 64, 64]
        # Input size: [batch, 3, 64, 64]
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, 3, stride=2, padding=1),  # b, 64, 32, 32
            nn.ReLU(True),
            nn.Conv2d(64, 128, 3, stride=2, padding=1),  # b, 128, 16, 16
            nn.ReLU(True),
            nn.Conv2d(128, 256, 3, stride=2, padding=1),  # b, 256, 8, 8
            nn.ReLU(True),
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(256, 128, 3, stride=2, padding=1, output_padding=1),  # b, 128, 16, 16
            nn.ReLU(True),
            nn.ConvTranspose2d(128, 64, 3, stride=2, padding=1, output_padding=1),  # b, 64, 32, 32 
            nn.ReLU(True),
            nn.ConvTranspose2d(64, 3, 3, stride=2, padding=1, output_padding=1),  # b, 3, 64, 64
            nn.Sigmoid()
        )
    

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x