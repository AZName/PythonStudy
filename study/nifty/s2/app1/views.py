from django.shortcuts import render

# Create your views here.

from django.views import View


class Home(View):

    Base_db = {
        "1": {"name": "root1", "host": "8081", "path": r"/a/s/s/d"},
        "2": {"name": "root2", "host": "8082", "path": r"/a/s/s/d"},
        "3": {"name": "root3", "host": "8083", "path": r"/a/s/s/d"},
        "4": {"name": "root4", "host": "8084", "path": r"/a/s/s/d"},
        "5": {"name": "root5", "host": "8085", "path": r"/a/s/s/d"},

    }

    def get(self, request):

        return render(request, "Home.html", {"base": self.Base_db})

    def post(self, request):

        return render(request, "Home.html")

# class Home(View):
#
#     def dispatch(self, request, *args, **kwargs):
#
#         return super(Home, self).dispatch(self, request, *args, **kwargs)
#
#     def get(self, request):
#
#         return render(request, "Home.html")
#         # return HttpResponse("home")
#
#     def post(self, request):
#
#         return render(request, "Home.html")
Base_db = {
        "1": {"name": "root1", "host": "8081", "path": r"/a/s/s/d"},
        "2": {"name": "root2", "host": "8082", "path": r"/a/s/s/d"},
        "3": {"name": "root3", "host": "8083", "path": r"/a/s/s/d"},
        "4": {"name": "root4", "host": "8084", "path": r"/a/s/s/d"},
        "5": {"name": "root5", "host": "8085", "path": r"/a/s/s/d"},

    }


def home(request):

    return render(request, "Home.html", {"base": Base_db})


# def detail(request):
#     nid = request.GET.get('id')
#
#     return render(request, "Detail.html", {"data": Base_db[nid]})
def detail(request, uid):
    return render(request, "Detail.html", {"data": Base_db[uid]})


def login(request):

    return render(request, "Login.html")