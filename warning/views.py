from django.http import JsonResponse
from django.views import View
from warning import tasks
from location.models import EWSMainTable
from tools.location_method import create_EWS_location_info_json
import datetime


def cycle_warning_check():
    result = []
    query_result = EWSMainTable.objects.filter(expire_time__lt=datetime.datetime.now())
    if query_result:
        for item in query_result:
            result.append(create_EWS_location_info_json(item))
    if result:
        tasks.send_warning_mail.delay(result)


class WarningInfo(View):
    def get(self, request):
        cycle_warning_check()
        query_result = EWSMainTable.objects.filter(expire_time__lt=datetime.datetime.now())
        resp = create_EWS_location_info_json(query_result[0])
        return JsonResponse(resp)
