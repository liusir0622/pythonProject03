"""
文件解析
读取csv文件中的内容，发送请求，并将服务器返回的结果进行保存
"""
# 导入csv模块
import csv

# 读取csv数据
import json

import requests

testdata=[]

with open('./data.csv',mode='r',encoding='utf8') as file:
    lines = csv.reader(file)
    headers = next(lines)
    # 表头添加新的字段
    headers.append('result')
    # 添加表头
    testdata.append(headers)
    for line in lines:
        print(line)
        # 请求地址
        url = line[0]
        # 请求方法
        method = line[1]
        # 请求数据
        data = line[2]
        print(type(data), data)
        # 字符串转换为 字典
        data_dict = json.loads(data)
        print(data_dict, type(data_dict))
        if method == 'post':
            r = requests.post(url, json=data_dict)
            print(r.json())
            # 将服务器返回结果 保存list 中
            # 将字典转换为字符串类型
            result_str = json.dumps(r.json(), ensure_ascii=False)
            line.append(result_str)
            print(line)
            testdata.append(line)

    # 执行完成之后， 查看 testdata数据
    print(testdata)

    # 将testdata中的数据 写入到csv文件中
    with open('./data_result.csv', mode='w', encoding='utf8', newline='') as f:
        cf = csv.writer(f)
        for data in testdata:
            cf.writerow(data)