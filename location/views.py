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

    def deal_post_from_TE(self, request):
        req_dict = {
            "SN": request.POST.get("SN"),
            "Model": request.POST.get("Model"),
            "MAC": request.POST.get("MAC"),
            "area": request.POST.get("area"),
            "line": request.POST.get("line"),
            "row": request.POST.get("row"),
            "number": request.POST.get("number"),
        }
        query_result = EWSMainTable.objects.filter(SN=req_dict["SN"])
        if query_result:
            try:
                query_result[0].line = req_dict["line"]
                query_result[0].area = req_dict["area"]
                query_result[0].row = req_dict["row"]
                query_result[0].number = req_dict["number"]
                query_result[0].save()
                resp = {
                    "code": 200,
                    "note": "Success" if len(query_result) == 1 else "SN is not unique"
                }
            except Exception as e:
                resp = {"code": 1003}
        else:
            try:
                EWSMainTable.objects.create(
                    SN=req_dict["SN"],
                    modelName=req_dict["Model"],
                    MAC=req_dict["MAC"],
                    line=req_dict["line"],
                    area=req_dict["area"],
                    row=req_dict["row"],
                    number=req_dict["number"]
                )
                resp = {
                    "code": 200,
                    "note": "SN is not exists"
                }
            except Exception as e:
                print("***MyError:", e)
                resp = {"code": 1001}
        return resp

    def post(self, request):
        # 0:From IT 1:From TE
        choice_method = {
            "0": self.deal_post_from_IT,
            "1": self.deal_post_from_TE,
        }
        flag = request.POST.get("Flag")
        if flag:
            resp = choice_method[flag](request)
        else:
            return JsonResponse({}, status=404)
        return JsonResponse(resp)

    def Search_simple_result(self, request):
        pass

    def get(self, request):
        # 0:Search simple result
        choice_method = {
            "0": self.Search_simple_result,
        }
        flag = request.GET.get("Flag")
        if flag:
            resp = choice_method[flag](request)
        else:
            return JsonResponse({}, status=404)
        return JsonResponse(resp)
