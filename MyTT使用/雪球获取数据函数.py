import pysnowball as ball
import json

ball.set_token("xq_a_token=7c5bf7cc46e57c9ccb49eb0de7a6c2278cd76cf3;u=1169061266")

# 获取某支股票的行情数据
res = ball.quotec('SH600104')
print(res)

# 获取某支股票的行情数据-详细
detail_res = ball.quote_detail("SH600104")
print(detail_res)

# 实时分笔
pankou_res = ball.pankou('SZ002027')
print(pankou_res)

# K线
# 获取K线数据。第二参数可制定从现在到N天前，默认100.
kline = ball.kline('SZ002027')
kline300 = ball.kline('SZ002027', 300)
print(kline300)

# 按年度获取业绩预告数据
earningforecast = ball.earningforecast('SZ002027')
print(earningforecast)

# 获取机构评级数据
report = ball.report('SZ002027')
print(report)

# 获取当日资金流如流出数据，每分钟数据
capital_flow = ball.capital_flow('SZ002027')
print(capital_flow)

# 获取历史资金流如流出数据，每日数据
capital_history = ball.capital_history('SZ002027')
print(capital_history)

# 获取资金成交分布数据
capital_assort = ball.capital_assort('SZ002027')
print(capital_assort)

# 大宗交易数据
blocktrans = ball.blocktrans('SZ002027')
print(blocktrans)

# 融资融券数据
margin = ball.margin('SZ002027')
print(margin)

# 按年度、季度获取业绩报表数据。
ball.indicator('SZ002027')

'''
输入参数：
symbol -> 股票代码
is_annals -> 只获取年报,默认为1
count -> 返回数据数量,默认5条
'''
ball.indicator(symbol='SZ002027', is_annals=1, count=10)

# 利润表
ball.income('SZ300251')

'''
输入参数：
symbol -> 股票代码
is_annals -> 只获取年报,默认为1
count -> 返回数据数量,默认5条
'''
ball.income(symbol='SZ300251',is_annals=1,count=10)


# 现金流量表
ball.cash_flow('SZ300251')
'''
输入参数：
symbol -> 股票代码
is_annals -> 只获取年报,默认为1
count -> 返回数据数量,默认5条
'''
ball.cash_flow(symbol='SZ300251',is_annals=1,count=10)


# 主营业务构成
ball.business('SZ300251')

'''
输入参数：
symbol -> 股票代码
count -> 返回数据数量,默认5条
'''
ball.business(symbol='SZ300251',count=10)

# F10 十大股东
ball.top_holders('SZ300251')

'''
输入参数：
symbol -> 股票代码
circula -> 只获取流通股,默认为1
'''
ball.top_holders(symbol='SZ300251',circula=0)

# F10 主要指标
ball.main_indicator('SZ300251')

# F10 股东人数
ball.holders('SZ002027')

# F10 机构持仓
ball.org_holding_change('SZ002027')

# F10 分红融资
'''
输入参数：
symbol -> 股票代码
page -> 第几页 默认1
size -> 每页含有多少数据 默认10
'''
ball.bonus('SZ002027')

# F10 行业对比
ball.industry_compare('SZ002027')


# user 自选列表
ball.watch_list()

# user 自选列表详情
ball.watch_stock(-1)

# cube 组合净值
ball.nav_daily("ZH2567925")

# cube 组合历史交易信息
ball.rebalancing_history("ZH2567925")

# 可转债信息
ball.convertible_bond(page_size=5, page_count=1)

# 指数基本信息
ball.index_basic_info("399967") #中证军工指数

# 指数详细信息--实验失败
ball.index_details_data("399967") #中证军工指数


# 指数权重股前十
ball.index_weight_top10("399967") #中证军工指数

# 指数收益
ball.index_perf_7("399967") #最近7天数据
ball.index_perf_30("399967") #最近30天数据
ball.index_perf_90("399967") #最近90天数据


# 深港通 北向数据 STOCK CONNECT NORTHBOUND SHAREHOLDING SEARCH BY DATE
ball.northbound_shareholding_sh() #默认当天
ball.northbound_shareholding_sh('2022/01/19')

# 沪港通 北向数据 STOCK CONNECT NORTHBOUND SHAREHOLDING SEARCH BY DATE
data = ball.northbound_shareholding_sz() #默认当天 可选填日期-格式：'2022/01/19'
print(data[0])

# fund_detail
ball.fund_detail("008975")

# fund_info
ball.fund_info("008975")

# fund_growth
ball.fund_growth("008975")

# fund_nav_history
ball.fund_nav_history("008975")

# fund_achievement
ball.fund_achievement("008975")

# fund_asset
ball.fund_asset("008975")

# fund_manager
ball.fund_manager("008975")

# fund_trade_date
ball.fund_trade_date("008975")

# fund_derived
ball.fund_derived("008975")


# 关键词搜索股票代码
ball.suggest_stock("tyzn")












































