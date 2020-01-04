import requests
import StockConfig
from bs4 import BeautifulSoup


# 根据生成的链接下载
def get_html(time_list=StockConfig.time_list):
    url = StockConfig.detail_stock_url.format(time_list, filters)
    print(url)
    respose = requests.get(url, headers=StockConfig.headers, verify=False)
    with open(StockConfig.stock_code + ".csv", "wb") as code:
        code.write(respose.content)
    print('完成')


# 获取时间
def get_time_param(code=StockConfig.stock_code):
    list_time = list()
    list_time.append(code)
    url = StockConfig.get_time_url.format(code)
    respose = requests.get(url, headers=StockConfig.headers)
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


if __name__ == '__main__':
    get_filter_list(StockConfig.dict)
    time_list = get_time_param(StockConfig.stock_code)
    get_html(time_list)
