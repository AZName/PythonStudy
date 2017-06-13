from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):

    return render(request, "Home.html")


def login(request):

    return render(request, "Login.html")

from app2 import models


def orm(request):
    # 增加
    # models.UserInfo.objects.create(username="azhen", password='123456')
    # 查询
    # result = models.UserInfo.objects.all()
    # for item in result:
    #     print(item.username)
    # result = models.UserInfo.objects.filter(username="azhen")
    # for item in result:
    #     print(item.id, item.username, item.password)
    # 改
    # models.UserInfo.objects.filter(username="azhen").update(password="123")

    # 删除
    models.UserInfo.objects.filter(username='azhen').delete()
    return HttpResponse("删除")

