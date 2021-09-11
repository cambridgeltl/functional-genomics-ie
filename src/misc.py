import numpy as np
import random

import torch

from util.core import printv

from src.custom_datasets import TensorDictDataset
from torch.utils.data import DataLoader, SequentialSampler


# TODO: Move to utils
def txt_str_to_md(string, bullet_consecutive_lines=False):

    # Make things titles based on newlines
    string = '\n\n\n## '.join(string.split('\n\n\n'))

    # If applicable, make lists out of consective, non-empty lines
    if bullet_consecutive_lines:
        s_split = string.split('\n')
        new_string = [s_split[0], s_split[1]]

        # We want to bullet when the previous line is not empty and neither is the current
        # If we're at the top of the bullets we need to insert a newline
        for l1, l2, l3 in zip(s_split, s_split[1:], s_split[2:]):
            if l2 != '' and l3 != '':
                if l1 == '':
                    new_string.append("\n* " + l3)
                else:
                    new_string.append("* " + l3)
            else:
                new_string.append(l3)

        string = '\n'.join(new_string)

    # Insert header and make first line title
    string = "---\ngeometry: margin=2.5cm\n---\n\n# " + string

    return string


# TODO: Move to utils
def dict_dget(_dict, key, default_key):
    return _dict[key] if key in _dict.keys() else _dict[default_key]


def get_cuda_info(verbose=True):
    using_gpu = torch.cuda.is_available()
    device = torch.device("cuda" if using_gpu else "cpu")
    n_gpu = torch.cuda.device_count()

    if using_gpu:
        printv("Found CUDA devices:", verbose_flag=verbose)
        for i in range(n_gpu):
            printv(torch.cuda.get_device_name(i), verbose_flag=verbose)
    else:
        printv("Using CPU", verbose_flag=verbose)

    return using_gpu, device


# Supports normal tensors but also dicts of tensors
def dataloader(*inputs, batch_size=1, sampler=None):
    sampler = sampler if sampler is not None else SequentialSampler

    def get_teD(x):
        if isinstance(x, dict):
            return {k: get_teD(v) for k, v in x.items()}
        elif isinstance(x, torch.Tensor):
            return x
        elif x is None:
            return {}
        else:
            return torch.tensor(x)

    data_tuple = tuple([get_teD(x) for x in inputs])
    data = TensorDictDataset(*data_tuple)
    return DataLoader(data, sampler=sampler(data), batch_size=batch_size)


# This is a partial reimplemntation of tf.keras.preprocessing.sequence.pad_sequence
def pad_sequences(sequences, value, maxlen=None, dtype=None):
    maxlen = max(len(s) for s in sequences) if maxlen is None else maxlen
    new_seqs = [[s[i] if i < len(s) else value for i in range(maxlen)] for s in sequences]
    return np.array(new_seqs, dtype=dtype)


def get_prf1a(tp, fp, fn, total_negative):
    precision = tp / (tp + fp) if tp != 0 else 0
    recall = tp / (tp + fn) if tp != 0 else 0
    f1 = 2 * recall * precision / (recall + precision) if tp != 0 else 0
    accuracy = tp / (tp + total_negative) if tp != 0 else 0
    return {"precision": precision, "recall": recall, "f1": f1, "accuracy": accuracy}


def check_tag_list(current, new, exception_on_new_tags=True, exception_on_missing_tags=False,
                   print_warnings=True, print_full_lists_on_error=False):
    current_copy = current[:]
    lb = "\n\t"
    full_list_str = f"""Current list:{lb}{lb.join(current)}

New list:{lb}{lb.join(new)}"""

    # Check each new tag
    for n_tag in new:

        # It exists in current list
        if n_tag in current_copy:
            current_copy.remove(n_tag)

        # It does not - take appropriate action
        else:
            txt = f"The following tag is not present in the orginal tag list: {n_tag}"
            if exception_on_new_tags:
                err_txt = txt if not print_full_lists_on_error else f"{txt}\n{full_list_str}"
                raise Exception(err_txt)
            elif print_warnings:
                print(f"[W] {txt}")

    # Now check if any tags were left
    if current_copy != []:
        txt = f"The following tags were not found in the new tag list:{lb}{lb.join(current_copy)}"
        if exception_on_missing_tags:
            err_txt = txt if not print_full_lists_on_error else f"{txt}\n{full_list_str}"
            raise Exception(err_txt)
        elif print_warnings:
            print(f"[W] {txt}")


def get_size(x, allow_dicts=False, error_on_empty_dicts=False):
    if isinstance(x, dict):
        if allow_dicts:
            if x == {}:
                if error_on_empty_dicts:
                    raise Exception("[E] Dict was empty")
                return None
            x_vals = list(x.values())
            return check_get_iterables_size(*x_vals, allow_dicts=allow_dicts,
                                            error_on_empty_dicts=error_on_empty_dicts)
        else:
            raise Exception("Found a dict but allow_dicts is False")
    elif x is None:
        return None
    else:
        return len(x)


def check_get_iterables_size(*iterables, allow_dicts=False, error_on_empty_dicts=False):
    sizes = [get_size(x, allow_dicts=allow_dicts, error_on_empty_dicts=error_on_empty_dicts)
             for x in iterables]
    sizes = [x for x in sizes if x is not None]
    size = None if sizes == [] else sizes[0]
    assert all(size == x for x in sizes)
    return size


def copy_type(original, new):
    if type(original) == np.ndarray:
        return np.array(new, dtype=original.dtype)
    elif type(original) == torch.Tensor:
        if type(new) == torch.Tensor:
            return new.to(original.device).to(original.dtype)
        elif hasattr(new, '__getitem__') and type(new[0]) == torch.Tensor:
            assert new[0].dtype == original.dtype
            return torch.stack(new)
        return torch.tensor(new, device=original.device, dtype=original.dtype)
    else:
        return type(original)(new)


def shuffle_items(*indexables, allow_dicts=False, error_on_empty_dicts=False):
    iter_length = check_get_iterables_size(*indexables, allow_dicts=allow_dicts,
                                           error_on_empty_dicts=error_on_empty_dicts)
    idxs = []
    available_idxs = list(range(iter_length))

    # Generate a list of random indices
    for _ in range(iter_length):
        idx = available_idxs[random.randint(0,len(available_idxs)-1)]
        idxs.append(idx)
        available_idxs.remove(idx)

    # Func to help with handling dicts
    def get_new_indexable(x, indexes):
        if isinstance(x, dict):
            if allow_dicts:
                return {k: get_new_indexable(v, indexes) for k, v in x.items()}
            else:
                raise Exception("Given a dict to shuffle without allow_dicts=True")
        elif x is None:
            return None
        else:
            return copy_type(x, [x[i] for i in indexes])

    # Now get lists of new shuffled elements, then preserve type
    new_indexables = []
    for indexable in indexables:
        new_indexables.append(get_new_indexable(indexable, idxs))

    return tuple(new_indexables)


def get_slice(x, i, j, allow_dicts=False):
    if isinstance(x, dict):
        if allow_dicts:
            return {k: get_slice(v, i, j, allow_dicts=allow_dicts) for k, v in x.items()}
        else:
            raise Exception("Given a dict to split_n_times without allow_dicts=True")
    elif x is None:
        return None
    else:
        return x[i:j]


def split_n_times(*sliceables, n=1, allow_dicts=False):
    """Split up sliceables (e.g. lists, numpy arrays ...) into n even groups

    If total size doesn't cleanly divide by n the last size will be different to the others

    Args:
        sliceables: Objects which support slicing
        n (int): Number of slices to make
        allow_dicts (bool): If true, will treat dicts as dicts of sliceables and slice
            their values, preserving keys

    Returns:
        tuple: Each element is a list of slices of each sliceable in order they were given
            First element is the first slice etc.

    Example:
        for xi, yi in split_n_times([1,3,5,7], [2,4,6,8], n=2):
            print(xi, yi)

        [1, 3] [2, 4]
        [5, 7] [6, 8]
    """

    # Check and get total size
    iter_length = check_get_iterables_size(*sliceables, allow_dicts=allow_dicts)

    # Get sizes in a way that covers whole length
    sizes = [int(iter_length/n) for _ in range(n-1)]
    sizes.append(iter_length - sum(sizes))

    return_sliceables = []

    idx = 0
    for size in sizes:
        new_idx = idx + size
        return_sliceables.append([get_slice(sliceable, idx, new_idx,allow_dicts=allow_dicts)
                                  for sliceable in sliceables])
        idx = new_idx

    return tuple(return_sliceables)


def asymetric_split(*sliceables, leading_fraction=0.5, allow_dicts=False):
    iter_length = check_get_iterables_size(*sliceables, allow_dicts=allow_dicts)
    l = int(iter_length*leading_fraction)

    return tuple([[get_slice(x,0,l,allow_dicts=allow_dicts) for x in sliceables],
                  [get_slice(x,l,iter_length,allow_dicts=allow_dicts) for x in sliceables]])


def combine_fold_pieces(*fold_pieces, allow_dicts=False):
    check_get_iterables_size(*fold_pieces)
    n_folds = len(fold_pieces)

    # Add each fold of data to all but one of the sets
    folds_in_each_set = [[] for x in range(n_folds)]
    for i, fold in enumerate(fold_pieces):
        for j in range(n_folds):
            if i != j:
                folds_in_each_set[j].append(fold)

    # To handle dicts
    def combine(xss, allow_dicts=False):
        if isinstance(xss[0], dict):
            if allow_dicts:
                return {k: combine([xs[k] for xs in xss], allow_dicts=allow_dicts)
                        for k in xss[0].keys()}
            else:
                raise Exception("Given a dict to combine_fold_pieces without allow_dicts=True")
        elif xss is None or all([xs is None for xs in xss]):
            return None
        else:
            return copy_type(xss[0], [x for xs in xss for x in xs])

    # Now we go through each dataset and recombine the folds
    resultant_tr_datasets = []
    for fold_set in folds_in_each_set:
        dset = []
        for xss in zip(*fold_set):
            dset.append(combine(xss, allow_dicts=allow_dicts))
        resultant_tr_datasets.append(dset)

    # Now we need to add in the removed bit of each fold
    resultant_datasets = []
    for tr, val in zip(resultant_tr_datasets, fold_pieces):
        resultant_datasets.append((tr, val))

    return resultant_datasets


def get_n_folds(*data,n=1,shuffle=False,allow_dicts=False):
    data = shuffle_items(*data, allow_dicts=allow_dicts) if shuffle else data
    return combine_fold_pieces(*split_n_times(*data, n=n, allow_dicts=allow_dicts),
                               allow_dicts=allow_dicts)

