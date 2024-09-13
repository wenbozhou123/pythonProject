import pysnowball as ball
import json

ball.set_token("xq_a_token=7c5bf7cc46e57c9ccb49eb0de7a6c2278cd76cf3;u=1169061266")

# 指数基本信息
# index_basic_info = ball.index_basic_info("399967") #中证军工指数
# print(index_basic_info)

# 指数详细信息
# ball.index_details_data("399967") # 中证军工指数
# index_details_data = ball.index_details_data("399967") #中证军工指数
# print(index_details_data)

res = ball.index_weight_top10("399967") #中证军工指数
print(res)
