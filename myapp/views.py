# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json

from myapp.models import ServiceUnitRecord, TestTable


@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = TestTable(name=request.GET.get('name'))
        user.save()
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        user = TestTable.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", user))
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_record(request):
    response = {}
    try:
        params = json.loads(request.body)
        record = ServiceUnitRecord()
        record.__setattr__('system_name', params['system_name'])
        record.__setattr__('service_name', params['service_name'])
        record.__setattr__('service_interface', params['service_interface'])
        record.__setattr__('total_num', params['total_num'])
        record.__setattr__('slow_num', params['slow_num'])
        record.__setattr__('slow_proportion', params['slow_proportion'])
        record.__setattr__('fail_num', params['fail_num'])
        record.__setattr__('fail_proportion', params['fail_proportion'])
        record.__setattr__('avg_delay_sec', params['avg_delay_sec'])
        record.__setattr__('longest_delay_sec', params['longest_delay_sec'])
        record.__setattr__('shortest_delay_sec', params['shortest_delay_sec'])
        record.__setattr__('start_time', params['start_time'])
        record.__setattr__('end_time', params['end_time'])
        record.save()
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_record(request):
    response = {}
    try:
        record = ServiceUnitRecord.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", record))
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)
