#!/usr/bin/env python3 

from indexextract import *
import sys
import os
import pandas as pd
import io
import argparse

#从file1和file2两个文件提取数据，写入newfile，抛弃注释
def index_merge(file1:str, file2:str, newfile:str):
    #提取两个index文件的数据
    commentlines1, lines1 = remove_comment(file1)
    commentlines2, lines2 = remove_comment(file2)
    #向新文件写入
    with open(newfile, 'w') as nf:
        nf.write("".join(lines1))
        nf.write("".join(lines2))
        nf.close()
    #print("merge finished\n")














if '__main__' == __name__:
    #解析命令
    dir, pyfile = os.path.split(sys.argv[0])
    parser = argparse.ArgumentParser(description="usage: "+pyfile+" file1 file2 newfile")
    parser.add_argument("file1", help="first index file")
    parser.add_argument("file2", help="second index file")
    parser.add_argument("newfile", help="new index file")
    args = parser.parse_args()
    
    #工作路径移动至.py文件所在目录
    if dir!="":
        os.chdir(dir)
    # if dir != "":
    #     #第一个参数使用绝对路径
    #     if os.path.isabs(dir):
    #         os.chdir(dir)
    #     #相对路径
    #     else:
    #         os.chdir(os.path.join(os.getcwd(),dir[2:]))
    index_merge(args.file1, args.file2, args.newfile)

