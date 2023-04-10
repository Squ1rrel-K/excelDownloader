import requests
import pandas as pd
import numpy as np

excel_path = 'GSE部分未下载链接.xlsx'


def download():
    gene_less_than_20 = pd.read_excel(excel_path, sheet_name='GSE小于20未下载')
    url_list = pd.DataFrame(gene_less_than_20, columns=['未下载文件地址'])
    print(url_list.dtypes)


# file = requests.get(url_list[i])
# print(file)

# gene_more_than_20 = pd.read_excel(excel_path, sheet_name='GSE大于20未下载', index_col=3)

if __name__ == '__main__':
    download()
