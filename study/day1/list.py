#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-16 20:23:23
# @Author  : xuzhen (azhen@azhen.xin)
# @Link    : http://www.azhen.xin/
# @Version : $Id$

names = ["xiaoming","xiaohuang","mobai","xiaolan"]
name2 = ["baidu","tengxun"]
# 增加
names.append("ofo")
# 合并
# names.extend(name2)
# 含有多少个值
# names.count("xiaoming")
# print(names.count("xiaoming"))
# 在那个位子
# names.index("mobai")
# print(names.index("mobai"))
#插入 
# names.insert(1,"ubergogo")
# pop 出一个 元素
# names.pop()
# 删除指定的元素
# names.remove("mobai")
# 反向排序
# names.reverse()
# 排序
# names.sort()
# 复制
import copy
name2 = copy.deepcopy(names)

print(name2)
