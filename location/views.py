from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from .models import EWSMainTable
from tools.location_decorators import check_SN_repeat
from tools.location_method import create_EWS_location_info_json


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

    def search_sort(self, req_dict):
        if req_dict["type"] == "SN":
            result = EWSMainTable.objects.filter(SN=req_dict["data"])
        elif req_dict["type"] == "MAC":
            result = EWSMainTable.objects.filter(MAC=req_dict["data"])
        elif req_dict["type"] == "location":
            result = EWSMainTable.objects.filter(
                area=req_dict["data"].split("-")[0],
                line=req_dict["data"].split("-")[1],
                row=req_dict["data"].split("-")[2],
                number=req_dict["data"].split("-")[3],
            )
        return result

    def search_simple_result(self, request):
        req_dict = {
            "type": request.GET.get("type"),
            "data": request.GET.get("data")
        }
        try:
            query_result = self.search_sort(req_dict)
            resp = create_EWS_location_info_json(query_result[0])
        except Exception as e:
            print("***MyError:", e)
            resp = {"code": 1005}
        return resp

    def get(self, request):
        # 0:Search simple result
        choice_method = {
            "0": self.search_simple_result,
        }
        flag = request.GET.get("Flag")
        if flag:
            resp = choice_method[flag](request)
        else:
            return JsonResponse({}, status=404)
        return JsonResponse(resp)
