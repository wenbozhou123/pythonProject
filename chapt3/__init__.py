import pandas as pd

def calculate_kdj(data, n=9):
    """
    计算KDJ指标

    参数:
    data -- 包含收盘价、最高价和最低价的DataFrame，列名分别为'close', 'high', 'low'
    n -- 计算RSV的周期，默认是9

    返回:
    DataFrame，包含K值、D值和J值
    """
    data['low_n'] = data['low'].rolling(window=n, min_periods=1).min()
    data['high_n'] = data['high'].rolling(window=n, min_periods=1).max()
    data['rsv'] = (data['close'] - data['low_n']) / (data['high_n'] - data['low_n']) * 100

    data['k'] = data['rsv'].ewm(alpha=1/3).mean()
    data['d'] = data['k'].ewm(alpha=1/3).mean()
    data['j'] = 3 * data['k'] - 2 * data['d']

    print('type(data)---', type(data))

    return data[['k', 'd', 'j']]

# 示例数据
data = {
    'close': [10, 11, 12, 13, 14, 13, 12, 11, 10, 11, 12],
    'high': [10, 11, 12, 13, 14, 13, 12, 11, 10, 11, 12],
    'low': [9, 10, 11, 12, 13, 12, 11, 10, 9, 10, 11]
}
print(type(data))
df = pd.DataFrame(data)

# 计算KDJ
kdj = calculate_kdj(df)
print(kdj)
