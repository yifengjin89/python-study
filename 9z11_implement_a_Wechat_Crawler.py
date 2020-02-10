# 2/7/2020
# implement a Wechat crawler
# coding=utf-8
import requests  # python 发送网络请求的模块

response = requests.get('http://www.jiuzhang.com')

print(response)  # output: <Response [200]>
print(type(response))  # output: <class 'requests.models.Response'>  # Class 类型
print(response.status_code)  # output: 200  # 200 就是请求成功； 302 就是网页跳转； 500 就是serve crash
print(response.encoding)  # output: utf-8  # 编码
# print(response.text)  # output: <!DOCTYPE html> <html> <head> ....... # 查看到未登录情况下的源码
