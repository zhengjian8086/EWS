from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.
class Info(View):
    def deal_post_from_IT(self,request):
        pass

    def post(self, request):
        # 0:From IT 1:From TE
        choice_method={
            "0":self.deal_post_from_IT,
        }
        print("==============",request.POST.get("Flag"))
        return JsonResponse({"code": 200})

    def get(self, request):
        return JsonResponse({"code": 200})
