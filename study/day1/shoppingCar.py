#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-16 22:57:48
# @Author  : xuzhen (azhen@azhen.xin)
# @Link    : http://www.azhen.xin/
# @Version : $Id$

money = input("请输入工资：")
cargos = (("苹果手机", 5000), ("车", 200000), ("咖啡", 31), ("书", 80))

shopping_car_list = []

if money.isdigit():
    money = int(money)
    while True:
        for p_itme in cargos:
            print(cargos.index(p_itme),p_itme)
        index = input("请选择购买物品:")
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(cargos):
                item = cargos[index]    #商品信息
                if money > item[1]:
                    money = money - item[1]    #剩余钱的数量
                    shopping_car_list.append(item)
                    print(f"成功加入购物车{item} 剩余工资{money}")
                else:
                    print(f"余额为{money},就剩这点钱还买东西？")
            else:
                print(f"请输入争取的物质序号0-{len(cargos)}")
        elif index == "q":

            print(f"完成购物，已购买的商品{shopping_car_list}, 剩余{money}的钱")

            break

            exit()
        else:
            print("输入有误 请重新输入")

else:
    print("请输入数字！")


