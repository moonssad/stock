# 爬虫的一些配置信息

stock_code = '002739'  # 配置股票代码
time_list = ['002739', '20150114', '20200103'] #默认值，股票代码，起始时间，截止时间
# 下载股票数据的URL
detail_stock_url = 'http://quotes.money.163.com/service/chddata.html?code=1{0[0]}&start={0[1]}&end={0[2]}&fields={1}'
# 获取股票数据起始和截止时间
get_time_url = 'http://quotes.money.163.com/trade/lsjysj_{}.html#06f01'
# 伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# 写一个字典由用户可配置需要的数据
# 然后想要什么数据就可以自己配了
param_dict = {
    '收盘价': 'TCLOSE',
    '最高价': 'HIGH',
    '最低价': 'LOW',
    '开盘价': 'TOPEN',
    '前收盘': 'LCLOSE',
    '涨跌额': 'CHG',
    '涨跌幅': 'PCHG',
    '换手率': 'TURNOVER',
    '成交量': 'VOTURNOVER',
    '成交金额': 'VATURNOVER',
    '总市值': 'TCAP',
    '流通市值': 'MCAP'
}
# 配置需要获取的数据
dict = ['收盘价', '最高价', '最低价','开盘价','前收盘','涨跌额','涨跌幅','换手率','成交量','成交金额','总市值','流通市值']


