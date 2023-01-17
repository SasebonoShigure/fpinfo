#!/usr/bin/env python3 

from indexextract import *
import sys
import pandas as pd
import io
import argparse

def index_merge(file1:str, file2:str, newfile:str):
    commentlines1, lines1 = remove_comment(file1)
    commentlines2, lines2 = remove_comment(file2)
    with open(newfile, 'w') as nf:
        nf.write("".join(lines1))
        nf.write("".join(lines2))
        nf.close()
    print("merge finished\n")














if '__main__' == __name__:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    newfile = sys.argv[3]
    index_merge(file1, file2, newfile)