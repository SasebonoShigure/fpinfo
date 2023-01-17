#!/usr/bin/env python3 

import sys
import pandas as pd
import io
import argparse

headnames = ["person","finger","common","type","attempt","image_file_name","retry_cnt"]
reserve_headnames = ["person","finger","attempt","image_file_name"]

#从filename提取注释和数据行
# remove_comment -> (commentlines, data)
def remove_comment(filename:str)-> tuple[list,list]:
    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()
    #提取注释
    commentlines = list(filter(lambda s: s.startswith('#'), lines))  
    #非注释部分
    lines = list(filter(lambda s: not s.startswith('#'), lines))  
    return commentlines,lines

# 从data(strstream)提取reserve_headnames对应的列的DataFrame
def parse_raw_index(lines: list[str], headnames: list[str], reserve_headnames: list[str]) -> pd.DataFrame:
    # 整合成一个str
    data = "\n".join(lines)
    # 将str作为文件传给read_csv
    with io.StringIO(data) as f:
        df = pd.read_csv(f, delim_whitespace=True, names=headnames)
    newdf = df[reserve_headnames]
    return newdf



#从file提取subset并写入newfile，返回finger数
def readwrite(file:str,newfile:str,restore_comment=False):
    commentlines,lines = remove_comment(file)
    newdf = parse_raw_index(lines, headnames, reserve_headnames)
    if restore_comment == False:
        newdf.to_csv(newfile,index=False, sep="\t")
    else:
        with open(newfile, 'w') as nf:
            nf.write("".join(commentlines))
            nf.write("#\t")
            nf.close()
        newdf.to_csv(newfile,index=False,sep="\t",mode="a")
    return len(newdf.groupby(["person", "finger"]).count().reset_index())



if '__main__' == __name__:
    file = sys.argv[1]
    newfile = sys.argv[2]
    readwrite(file,newfile,True)