from numbers import Number
from torch import tensor

# Helpful functions
def eD(_dict):
    return EnhancedDict(_dict)

def deep_eD(_dict):
    def proccess_elem(v):
        if isinstance(v, dict):
            return deep_eD(v)
        elif isinstance(v, list):
            return [proccess_elem(x) for x in v]
        else:
            return v
    return eD({k: proccess_elem(v) for k, v in _dict.items()})

def check(d1, d2):
    if d1.keys() != d2.keys():
        raise TypeError(f"EnhancedDicts have different keys {d1.keys()} vs {d2.keys()}")

def coarse_type_check(v1, v2):
    if isinstance(v1, Number) and isinstance(v2, Number):
        return True
    if isinstance(v1, dict) and isinstance(v2, dict):
        return True
    if isinstance(v1, list) and isinstance(v2, list):
        return True
    return type(v1) == type(v2)


class EnhancedDict(dict):

    # Specific functionality

    def combine(self, other):
        check(self, other)
        def proccess_elems(v1, v2):
            if not coarse_type_check(v1, v2):
                raise Exception(f"Types of {v1} and {v2} are different, {type(v1)} vs {type(v2)}")
            if isinstance(v1, EnhancedDict):
                return v1.combine(v2)
            elif isinstance(v1, list):
                if len(v1) != len(v2):
                    raise Exception(f"Lengths of {v1} and {v2} are different, {len(v1)} vs {len(v2)}")
                return [proccess_elems(v1x, v2x) for v1x, v2x in zip(v1, v2)]
            else:
                return v1 + v2
        return eD({k: proccess_elems(v, other[k]) for k, v in self.items()})

    def mult(self, m):
        def proccess_elem(v):
            if isinstance(v, EnhancedDict):
                return v.mult(m)
            elif isinstance(v, list):
                return [proccess_elem(x) for x in v]
            else:
                return v * m
        return eD({k: proccess_elem(v) for k, v in self.items()})

    def add(self, a):
        def proccess_elem(v):
            if isinstance(v, EnhancedDict):
                return v.add(a)
            elif isinstance(v, list):
                return [proccess_elem(x) for x in v]
            else:
                return v + a
        return eD({k: proccess_elem(v) for k, v in self.items()})

    def neg(self, n):
        return self.add(-n)

    def div(self, d):
        return self.mult(1/d)


    # NUMERIC METHODS

    def __add__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__add__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__add__(other) for k, v in self.items()})

    def __sub__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__sub__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__sub__(other) for k, v in self.items()})

    def __mul__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__mul__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__mul__(other) for k, v in self.items()})

    def __truediv__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__truediv__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__truediv__(other) for k, v in self.items()})

    def __floordiv__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__floordiv__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__floordiv__(other) for k, v in self.items()})

    def __radd__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__radd__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__radd__(other) for k, v in self.items()})

    def __rsub__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__rsub__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__rsub__(other) for k, v in self.items()})

    def __rmul__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__rmul__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__rmul__(other) for k, v in self.items()})

    def __rtruediv__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__rtruediv__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__rtruediv__(other) for k, v in self.items()})

    def __rfloordiv__(self, other):
        if isinstance(other, EnhancedDict):
            check(self, other)
            return eD({k: v.__rfloordiv__(other[k]) for k, v in self.items()})
        else:
            return eD({k: v.__rfloordiv__(other) for k, v in self.items()})


    # PYTORCH METHODS

    def backward(self, retain_graph=None):
        rg = True if retain_graph is None else retain_graph
        for v in self.values():
            v.backward(retain_graph=rg)

    def item(self):
        return eD({k: v.item() for k, v in self.items()})

    def mean(self):
        return eD({k: v.mean() for k, v in self.items()})

    def tensor(self):
        return eD({k: v.tensor() if isinstance(v, EnhancedDict) else tensor(v)
                   for k, v in self.items()})

    def to(self, *args, **kwargs):
        return eD({k: v.to(*args, **kwargs) for k, v in self.items()})

    def numpy(self, *args, **kwargs):
        return eD({k: v.numpy(*args, **kwargs) for k, v in self.items()})

    def detach(self, *args, **kwargs):
        return eD({k: v.detach(*args, **kwargs) for k, v in self.items()})

