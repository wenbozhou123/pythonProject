import json

# JSON格式的字符串
json_string = '''
{
    "name": "Alice",
    "age": 30,
    "is_student": false,
    "hobbies": ["reading", "traveling"],
    "details": {"city": "Beijing", "country": "China"}
}
'''

# 将JSON字符串解析成Python对象
data = json.loads(json_string)
print(data)
print(data['hobbies'][0])


#Python 字典
data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'hobbies': ['reading', 'traveling'],
    'details': {'city': 'Beijing', 'country': 'China'}
}

# 将Python对象转换为JSON字符串
# ensure_ascii=False 参数使得非ASCII字符能够正确显示，indent=4 则让输出的 JSON 字符串更具有可读性。
json_string = json.dumps(data, ensure_ascii=False, indent=4)
print(json_string)