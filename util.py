import os


def set_cwd():
    cwd = __file__.split("AoC2019")[0] + "AoC2019/"
    os.chdir(cwd)

def load_txt_data(path: str):
    """
    Reads in a txt file line by line and returns that as an array.
    :param path:
    :return:
    """
    with open(path, 'r', encoding="utf-8") as f:
        data = [line.replace("\n", "") for line in f.readlines()]
    return data

set_cwd()