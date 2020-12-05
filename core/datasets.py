import torch
from torch.utils.data import Dataset
import cv2
from PIL import Image
from pathlib import Path
import pandas as pd
import numpy as np
from typing import Optional, Callable, Tuple, Any

class LA3Duplicate(Dataset):
    """ `FER13 <https://www.kaggle.com/deadskull7/fer2013>` Dataset.
    Parameters
    ----------
    root: string
        Root directory of dataset where directory fer2013.csv exists.
    transform: callable (optional)
        A function/transform that takes in an PIL image and returns a
        transformed version.
    """
    _repr_indent = 4

    def __init__(
        self,
        root: str,
        transform: Optional[Callable] = None,
    ) -> None:
        self.root = Path(root).resolve()
        self.transform = transform

        self.data = pd.DataFrame({
            "file": [path for path in self.root.iterdir()]
        })

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> Any:
        """
        Parameter
        ---------
        index: int
        Returns
        -------
        tuple: (image, target) where target is index of the target class.
        """
        path = self.data.file.iloc[index]
        print(path)
        input = cv2.imread(str(path))
        if len(input.shape)==2:
            input = np.repeat(input[..., np.newaxis], 3, -1)
        color = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(color)

        if self.transform is not None:
            img = self.transform(img)

        return img

    def __repr__(self) -> str:
        head = "Dataset " + self.__class__.__name__
        body = [f"Number of datapoints: {self.__len__()}"]
        if self.root is not None:
            body.append(f"Root location: {self.root}")
        # body += [f"Split: {'Train' if self.train is True else 'Test'}"]
        if self.transform is not None:
            body += [repr(self.transform)]
        lines = [head] + [" " * self._repr_indent + line for line in body]
        return "\n".join(lines)