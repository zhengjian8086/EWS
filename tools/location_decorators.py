from location.models import EWSMainTable
from django.http import JsonResponse


def check_SN_repeat(func):
    def wapper(*args, **kwargs):
        sn = args[0].POST.get("SN")
        flag = EWSMainTable.objects.filter(SN=sn)
        print("========", not flag)
        if not flag:
            result = func(*args, **kwargs)
        else:
            result = {
                "code": 1002,
                "note": "SN repeat",
            }
        return result

    return wapper
