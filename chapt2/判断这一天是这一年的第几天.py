# 判断这一天是这一年的第几天
year = 2024
month = 3
day = 1

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

totalDays = 0


def judgeYear(year1):
    if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
        return True
    return False


for i in range(month):
    totalDays += days[i]
    if i == 1 and judgeYear(year):
        totalDays += 1

print(f"{year}年{month}月{day}日，是{year}年中的第{totalDays}天")
