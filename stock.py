from importlib import reload

import requests
import StockConfig
from bs4 import BeautifulSoup
import pandas as pd
import sys

reload(sys)


# 根据生成的链接下载
def get_html(time_list=StockConfig.time_list):
    url = StockConfig.detail_stock_url.format(time_list, filters)
    print(url)
    respose = requests.get(url, headers=StockConfig.headers, verify=False)
    with open(time_list[0] + ".csv", "wb") as code:
        code.write(respose.content)
    sort_csv(time_list[0] + ".csv")
    print('完成')


# 获取时间
def get_time_param(code=StockConfig.stock_code):
    list_time = list()
    list_time.append(code)
    url = StockConfig.get_time_url.format(code)
    respose = requests.get(url, headers=StockConfig.headers)
    print(respose.status_code)
    soup = BeautifulSoup(respose.text, 'lxml')
    start_time = soup.select("input[name='date_start_type']")[0]['value']
    start_time = start_time.replace("-", "")
    list_time.append(start_time)
    end_time = soup.select("input[name='date_end_type']")[0]['value']
    end_time = end_time.replace("-", "")
    list_time.append(end_time)
    print(list_time)
    return list_time


# 获取需要下载的数据列表
filters = ''


def get_filter_list(dict=StockConfig.dict):
    global filters
    for i in range(len(dict)):
        if i == len(dict) - 1:
            filters = filters + StockConfig.param_dict[dict[i]]
        else:
            filters = filters + StockConfig.param_dict[dict[i]] + ';'


# 根据时间将数据按照时间顺序排列。
def sort_csv(file_name):
    #当没有交易信息时这些参数的值都为0
    list_column=['收盘价','开盘价','最高价','最低价','换手率','成交量','成交金额']
    try:
        df = pd.read_csv(file_name, encoding='gb2312')
        result = df.sort_values('日期', ascending=True)
        for item in list_column:
            if item in result.columns:
             result = result[~result[item].isin([0])]
             result.to_csv(file_name)
             break
        print(result)
    except:
        print('没有可判断数据清洗失败')


if __name__ == '__main__':
    get_filter_list(StockConfig.dict)
    time_list = get_time_param(StockConfig.stock_code)
    get_html(time_list)
