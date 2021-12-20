import logging
import os
import subprocess


def check_dirs(cur_dir):
    """
    检查当前目录是否存在cur_dir，返回bool类型
    :param cur_dir:
    :return:
    """
    if not os.path.exists(cur_dir):
        return False
    return True


def copy_file(src_dir, tar_dir):
    cmd = "cp %s %s".format(src_dir, tar_dir)
    subprocess.check_call(cmd, shell=True)


def find_file(cur_dir, suffix=".ini"):
    for file in os.listdir(cur_dir):
        if file.endswith(suffix):
            return cur_dir + "/" + file
    logging.error("Cannot find %s file" % suffix)
    return None


def init_dir(base_dir, pathes=["log", "data", "model"]):
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    dirs = {}
    for path in pathes:
        cur_dir = base_dir + "/%s/" % path
        if not os.path.exists(cur_dir):
            os.mkdir(cur_dir)
        dirs[path] = cur_dir
    return dirs


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
