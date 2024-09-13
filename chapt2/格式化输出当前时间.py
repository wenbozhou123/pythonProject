import time

current_time = time.time()
print(f"current_time is {current_time}")


local_time = time.localtime()
print(f"local_time is {local_time}")

utc_time = time.gmtime()

print(f"utc_time is {utc_time}")

format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"format_time is {format_time}")

parse_time = time.strptime("2024-07-09 13:30:00", "%Y-%m-%d %H:%M:%S")
print(f"parse_time is {parse_time}")


start_time = time.time()
# 模拟耗时操作
time.sleep(2)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.0f} seconds")

print("-"*50)
# time.perf_counter() 更适合精确测量时间间隔，因为它具有更高的精度
start_time = time.perf_counter()
# 模拟耗时操作
time.sleep(2)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

print("-"*50)

start_time = time.process_time()

# 模拟耗时操作
for i in range(1000000):
    pass

end_time = time.process_time()
elapsed_time = end_time - start_time
print(f"Process time: {elapsed_time} seconds")

print("time.ctime() 返回当前时间的字符串表示形式", "-"*50)

current_time_str = time.ctime()
print(f"Current time: {current_time_str}")

