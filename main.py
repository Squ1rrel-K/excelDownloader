import os.path
import re
import shutil
import time
import requests
import pandas as pd
import numpy as np
import tqdm
EXCEL_PATH = 'GSE部分未下载链接.xlsx'
URl_COLUMN_NAME = '未下载文件地址'


def download():
    excel_path = input('Please config excel path: (default: GSE部分未下载链接.xlsx)')
    if excel_path == '':
        excel_path = EXCEL_PATH

    url_column_name = input('Please config url column name: (default: 未下载文件地址)')
    if url_column_name == '':
        url_column_name = URl_COLUMN_NAME

    sheets = pd.read_excel(excel_path, sheet_name=None)
    # iterate each sheet
    for key in sheets:
        # get url list
        url_list = pd.Series(sheets[key].loc[:, url_column_name])
        # download files from each sheet list
        for url in url_list:
            with requests.get(url, stream=True) as r:
                # use regex to get file name from http response
                file_name = re.findall(r"filename=\"([\w,.]*)\"", r.headers['content-disposition'])[0]
                size = float(r.headers['content-length'])
                pbar = tqdm.tqdm(total=size,
                                 unit_scale=True,
                                 desc=file_name,
                                 ncols=120)
                with open(file_name, 'wb') as f:

                    for chunk in r.iter_content(chunk_size=512):
                        if chunk:
                            f.write(chunk)
                            pbar.update(512)
                            time.sleep(0.01)


if __name__ == '__main__':
    download()
