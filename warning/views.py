from django.http import JsonResponse
from django.views import View
from warning import tasks
from location.models import EWSMainTable


# region celery demo
# def deme_view(request):
#     # 用delay方法运行函数，这里两个函数可以同时被调用，也就是并行
#     result_one = tasks.send_sms.delay()
#     result_two = tasks.send_sms2.delay()
#
#     # 用get方法拿到返回的结果
#     print(result_one.get())
#     print(result_two.get())
#     final_result = result_one.get() + result_two.get()
#
#     return JsonResponse(
#         {
#             'code': 200,
#             'message': 'success',
#             'data': {
#                 'result': final_result
#             }
#         }
#     )
# endregion


def cycle_warning_check():
    result = EWSMainTable.objects.all()
    for item in result:
        with open("/mnt/d/Study/2020/EWS/tmp.log", "a") as f:
            f.write(item.SN)
            f.write(r"\n")


class WarningInfo(View):
    def get(self, request):
        pass
