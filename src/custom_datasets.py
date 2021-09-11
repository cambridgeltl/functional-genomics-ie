import torch
from torch.utils.data import Dataset


class TensorDictDataset(Dataset):
    r"""Dataset wrapping tensors or dicts of tensors.

    Each sample from tensors will be retrieved by indexing tensors along the first dimension.
    Each sample from the dict of tensors will return a dict with the indexes along the first dimension of the contained tensors

    Dicts can be nested but not put inside tensors i.e. Dict[Dict[Tensor]] is valid but Dict[Tensor[Dict]] is not

    Dict values can be tensors or dicts themselves

    ALL tensors must have the same length (first dimension), there are no other restrictions
    """

    @staticmethod
    def _get_size(tensorDict):

        if isinstance(tensorDict, torch.Tensor):
            return tensorDict.size(0)

        elif isinstance(tensorDict, dict):
            sizes = [TensorDictDataset._get_size(t) for t in tensorDict.values()]
            sizes = [x for x in sizes if x is not None]
            size = None if sizes == [] else sizes[0]
            assert all(size == x for x in sizes)
            return size

        else:
            raise Exception(f"Element was not a tensor or dict, it was {type(tensorDict)}")

    def __init__(self, *tensorDicts) -> None:
        sizes = [self._get_size(tD) for tD in tensorDicts]
        sizes = [x for x in sizes if x is not None]
        size = None if sizes == [] else sizes[0]
        assert all(size == x for x in sizes)
        self.tensorDicts = tensorDicts

    @staticmethod
    def _tD_get_item(tensorDict, index):

        if isinstance(tensorDict, torch.Tensor):
            return tensorDict[index]

        else:
            return {k: TensorDictDataset._tD_get_item(t, index) for k, t in tensorDict.items()}

    def __getitem__(self, index):
        return tuple(self._tD_get_item(tD, index) for tD in self.tensorDicts)

    def __len__(self):
        return self._get_size(self.tensorDicts[0])

