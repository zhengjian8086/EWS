from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from .models import EWSMainTable
from tools.location_decorators import check_SN_repeat


# Create your views here.
class Info(View):
    @method_decorator(check_SN_repeat)
    def deal_post_from_IT(self, request):
        req_dict = {
            "SN": request.POST.get("SN"),
            "Model": request.POST.get("Model"),
            "MAC": request.POST.get("MAC"),
        }
        try:
            EWSMainTable.objects.create(
                SN=req_dict["SN"],
                modelName=req_dict["Model"],
                MAC=req_dict["MAC"]
            )
            resp = {"code": 200}
        except Exception as e:
            print("***MyError:", e)
            resp = {"code": 1001}
        return resp

    def post(self, request):
        # 0:From IT 1:From TE
        choice_method = {
            "0": self.deal_post_from_IT,
        }
        flag = request.POST.get("Flag")
        if flag:
            resp = choice_method[flag](request)
        else:
            resp = {}
        return JsonResponse(resp)

    def get(self, request):
        return JsonResponse({"code": 200})
