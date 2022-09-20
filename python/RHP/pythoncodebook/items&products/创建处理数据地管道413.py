# 想要以流水线地形式对数据进行迭代处理，类似unix的管道。exp:有海量的数据，无法一次加载到内存
import bz2
import fnmatch
import gzip
import os


# 文件拆解
import re


def gen_find(filepat,top):
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)
def gen_opener(filenames):
    for filename in filenames:
        if filename.endwith('.gz'):
            f=gzip.open(filename,'rt')
        elif filename.endwith('.bz2'):
            f=bz2.open(filename,'rt')
        else:
            f=open(filename,'rt')
            yield f
            f.close()
def gen_grep(pattern,lines):
    pat=re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield  line

