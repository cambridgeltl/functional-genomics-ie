# 14/05/2020
# Jason Brown
# Core util functions


import numpy as np
from multiprocessing import Process
import string
from datetime import datetime


# region Useful miscellaneous functions
def ensure_file_ext(path, ext):
    return path + "." + ext if path.split('.')[-1] != ext else path

def ensure_folder(path):
    return path if path[-1] == "/" else path + "/"

def convert_base(number, parent_base=10, target_base=10, parent_zero=None, target_zero=None):
    """
    Converts a number into a different base via a provided definition of that base
    WARNING Doesn't seem to quite work past the first ~14+ digits, no problem if number is shorter than that

    :param number: int or string; Number to convert
    :param parent_base: string, list or int; Contains all characters in base number is already in
    :param target_base: string, list or int; Contains all characters in base that we are converting to
    :param parent_zero: bool; Whether parent base contains a 0, if None is set to true if first digit of base is 0
    :param target_zero: bool; Whether target base contains a 0, if None is set to true if first digit of base is 0
    :return: string or int; The number represented in the provided base, int if target is base 10
    """

    # Check everything is in an appropriate data type
    for k, v in {"number": number, "parent_base": parent_base, "target_base": target_base}.items():
        if not isinstance(v, (int, str, list, tuple)):
            raise Exception(f"Error in convert_base, {k} has to be an int, str, list or tuple. Value passed was {v} of type {type(v)}")

    if isinstance(parent_base, int):
        if parent_base > 10 or parent_base < 1:
            raise Exception("Error in convert_base, parent base not 1-10 without explicit definition"
                            f"\nParent base = {parent_base}")

    if isinstance(target_base, int):
        if target_base > 10 or target_base < 1:
            raise Exception("Error in convert_base, target base not 1-10 without explicit definition"
                            f"\nTarget base = {target_base}")

    # If a base is passed as either a string or integer this converts it to a list
    def convert_int_and_str_bases(base, zero):

        if isinstance(base, (list, tuple)):
            pass
        elif isinstance(base, str):
            base = list(base)
        elif isinstance(base, int):
            base = [str(x) for x in range(0, base)]
        else:
            raise Exception(f"Error - Check on bases has failed")

        zero = (base[0] == "0") if zero is None else zero

        return base, zero


    if parent_base != 10:  # Convert to base 10 if not in base 10 so our algorithm for converting to target base works
        parent_base, parent_zero = convert_int_and_str_bases(parent_base, parent_zero)

        # Makes sure number is correct format
        if isinstance(number, int):
            number = str(number)
        number = list(number)

        number_base10 = 0
        for power, digit in enumerate(number[::-1]):

            try:
                digit_value = parent_base.index(str(digit))
            except ValueError:
                raise Exception(f"Digit {digit} was invalid for parent base. Parent base has digits: {''.join(parent_base)}")

            if not parent_zero:
                digit_value += 1
            number_base10 += digit_value * (len(parent_base) ** int(power))

        number = number_base10

    if target_base != 10:  # Convert base 10 number into target base
        target_base, target_zero = convert_int_and_str_bases(target_base, target_zero)

        if not isinstance(number, int):
            raise Exception(f"Error in convert_base, number given to target_base was not a number. {number}, type was {type(number)}")

        if number < 0:
            raise Exception(f"Error, only supports positive numbers, number = {number}")

        # Offsetting allows non-zeroed bases i.e. a, b, ... z, aa, ab ... compared to a, b, ... z, ba, bb ...
        offset = int(not target_zero)

        new_string_list = []
        base_size = len(target_base)

        while number > 0:
            index = (number - offset) % base_size
            new_string_list.insert(0, target_base[index])
            number = (number - index - offset) // base_size

        number = ''.join(new_string_list)

    return number  # Note, returns as a integer for target_base=10


def dict_swap(dictionary):
    """
    Swaps the keys and values of a given dictionary

    :param dictionary: Dictionary to use
    :return: Dictionary that has keys and values switched
    """
    return dict((v, k) for k, v in dictionary.items())


def merge_dicts(*args):
    _dict = dict()
    for arg in args:
        _dict = {**_dict, **arg}
    return _dict


def list_of_dicts_to_dict_of_lists(dict_list):
    new_dict = {k: [] for k in dict_list[0].keys()}
    for d in dict_list:

        # Check keys match
        if new_dict.keys() != d.keys():
            raise Exception(f"Inconsistent dictionary keys in list_of_dicts_to_dict_of_lists\n\
{new_dict.keys()} vs {d.keys()}")

        # Add entries
        for k, v in d.items():
            new_dict[k].append(v)

    return new_dict


def dict_of_lists_to_list_of_dicts(list_dict):
    # Check sizes
    ldvs = list(list_dict.values())
    l_length = len(ldvs[0])
    assert all(l_length == len(ldv) for ldv in ldvs)

    # Create data structure to populate
    dict_list = [{k: None for k in list_dict.keys()} for _ in range(l_length)]

    # Iterate through and populate structure
    for k, vs in list_dict.items():
        for i, v in enumerate(vs):
            dict_list[i][k] = v

    return dict_list


def pairs(iterable):
    if len(iterable) <= 1:
        return []
    else:
        return [(iterable[0], x) for x in iterable[1:]] + pairs(iterable[1:])


def execute_in_parallel(function, *args, **kwargs):
    """
    Execute a function in parallel to code where it was executed from. Doesn't yet join or end process so be careful
    Mainly used for putting up graphs and images whilst code is still executing
    Function MUST be accessible from main scope i.e. is not nested in another function. It can be a method from a class

    :param function: Function to execute
    :param args: Arguments for that function
    :param kwargs: Keyword arguments for that function
    """
    process = Process(target=function, args=args, kwargs=kwargs)
    process.start()


def get_time_stamp():
    date = datetime.now().date().__str__()
    time = datetime.now().time().__str__()
    time = '-'.join(time.split(':')[:2])
    return f"{date}_{time}"


class LogUsage:
    # This class is to be used as a function decorator (@LogUsage) that when activated (LogUsage.active = True) will log
    # whenever a tagged function is called, the amount of times it's been called and when the function is finished
    active = False

    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1

        # Check whether to print debug statement
        if self.active:
            print(f"{self.func.__name__} has been called, total: {self.counter}")

        # Execute function
        self.func(*args, **kwargs)

        # Check whether to print debug statement
        if self.active:
            print(f"{self.func.__name__} has finished")


def printv(*args, verbose_flag: bool):
    """
    Prints a string only if the flag is true. Can be used as a debug printer

    :param args: Args to print
    :param verbose_flag: Flag to decide if to print or not
    """
    if verbose_flag:
        print(*args)
# endregion


# List related functions
def limit_seq_sum(seq, max_sum):
        new_seq = []
        t_len = 0
        for n in seq:
            if (t_len + n) >= max_sum:
                new_seq.append(max_sum-t_len)
                break
            else:
                new_seq.append(n)
                t_len += n
        return new_seq


def ensure_list(item, preserve_none=True):
    if isinstance(item, list):
        return item
    elif item is not None or not preserve_none:
        return [item]
    else:
        return None


def flatten(x):
    result = []
    for item in x:
        if hasattr(item, "__iter__") and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def iterable_shape(x, count_strings=False):
    shape = []
    def check_length(y):
        if hasattr(y, "__iter__") and (not isinstance(y, str) or count_strings):
            shape.append(len(y))
            if len(y) > 0 and not isinstance(y, str):
                check_length(y[0])
    check_length(x)
    return shape
# endregion


# region List choice functions
def norm_list_probabilities(_list, print_new_list=False):
    """
    Takes _list destined for choose_from_list and normalises their probs to equal 1

    :param _list: list; Target list
    :param print_new_list: bool; Whether to print new list or not
    :return: dict; List with probs summing to 1
    """
    values = [x[1] for x in _list]

    if np.sum(values) == 0:
        raise ValueError(f"Values in the list sent to norm_list_probabilities summed to 0: {_list}")

    magnitude = np.linalg.norm(np.array(values), ord=1)
    new_list = [[item, probability/magnitude] for item, probability in _list]

    if print_new_list:
        print(f"New list: {new_list}")

    return new_list


def choose_from_list(_list, npr=None, verbose=False, print_list_and_roll=False):
    """
    Picks an item from a list where the list items are 2 element lists of item and probability

    :param _list: list; Target list
    :param npr: numpy.random obj; Random number generator to use, allows seeding from where it's called
    :param verbose: bool; Whether to print out warning info
    :return: dictionary key; The chosen key
    """

    if npr is None:
        npr = np.random

    # List items that are not tuples / lists of (item, probability) are given a relative probability of 1
    _list = [x if isinstance(x, (list, tuple)) and len(x) == 2 else (x, 1)
             for x in _list]
    """
    if not isinstance(_list[0], (list, tuple)):
        _list = list(zip(_list, np.ones(len(_list))))
    """

    # This loop is to catch and correct sum of probs != 1
    while True:
        if round(float(np.sum([x[1] for x in _list])), 5) != 1.00000:  # List comprehension returns list of probs
            if verbose:
                print("Warning in choose_from_list, values did not add to 1, normalising")
                print(f"Old list: {_list}")
            _list = norm_list_probabilities(_list, print_new_list=verbose)
            verbose = True  # We should never come back here so we'll go verbose to make it obvious we looped infinitely
        else:
            break  # Free to carry on to rest of function

    roll = npr.random()

    if print_list_and_roll:
        print(f'Roll: {roll:.5f} for list: {[[x, round(y, 5)] for x,y in _list]}')

    for item, probability in _list:
        roll -= probability
        if roll < 0:  # Item was chosen
            return item
    else:
        raise Exception(f"An item was not chosen in the list {_list} where the roll was {roll} from npr {npr}")
# endregion


# region String conversions and operations
def dict_to_string(_dict, cap_and_space_key=False, cap_and_space_value=False, all_on_one_line=False):
    """
    Converts a dictionary into a string of all its properties. Each property is separated by "\n" or ", " depending on
    all_on_one_line parameter

    Example:
    >> a = {"property_1": value_1, "property_2": value_2}
    >> print(dict_to_string(a, cap_and_space=True))
    Property 1: value_1
    Property 2: value_2

    :param _dict: Dictionary to use
    :param cap_and_space_key: Whether to capitalise and space the dictionary keys (see capitalise_and_space)
    :param cap_and_space_value: Whether to capitalise and space the dictionary values
    :param all_on_one_line: Whether to have all properties on one line or on newlines
    :return: The created string
    """
    _string = ""

    for k, v in _dict.items():
        k = capitalise_and_space(k) if cap_and_space_key else k
        v = capitalise_and_space(v) if cap_and_space_value else v
        end = ", " if all_on_one_line else "\n"
        _string += f"{k}: {v}{end}"

    _string = _string[:-1] if _string[-1] == "\n" else _string[:-2]  # Removes final "\n" or ", "

    return _string


def dict_to_list_of_strings(_dict, separator=": "):
    """
    Converts a dictionary into a list of string with the keys and values

    :param _dict: Dictionary to use
    :param separator: How to separate the key and value
    :return: The list
    """
    return [f"{k}{separator}{v}" for k, v in _dict.items()]


def capitalise_and_space(_string, splitter="_", joiner=" "):
    """
    Takes "a_string_like_this" and makes it "A String Like This"

    :param _string: String to capitalise and space
    :return: Capitalised and spaced string
    """
    # Converts stuff_like_this to Stuff Like This
    return string.capwords(joiner.join(_string.split(splitter)))


def comma_number(number):
    """
    Takes numbers like this 1000000 and makes a string like this 1,000,000

    :param number: Number to apply commas to
    :return: String that is number with commas
    """
    dig_list = list(str(number))
    comma_num_list = []

    for i, dig in enumerate(dig_list[::-1]):  # Go from LSD to MSD as we want to count 3 digits from LSD
        if i % 3 == 0:  # This ends up putting a comma in on first iter, we remove this later
            comma_num_list.append(',')
        comma_num_list.append(dig)

    comma_num = ''.join(comma_num_list[::-1][:-1])  # We need to reverse back and remove comma that was put at end
    return comma_num
# endregion
