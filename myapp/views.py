# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json

from myapp.models import ServiceUnitRecord, TestTable, Service, ServiceNameMapper


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
        system_name = get_show_name(params['system_name'])
        service_name = get_show_name(params['service_name'])
        record.__setattr__('system_name', system_name)
        record.__setattr__('service_name', service_name)
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

        service = Service.objects.filter(system_name=params['system_name'],
                                         service_name=params['service_name'],
                                         service_interface=params['service_interface'])
        if not service:
            service = Service(system_name=params['system_name'],
                              service_name=params['service_name'],
                              service_interface=params['service_interface'])
            service.save()
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
        record = ServiceUnitRecord.objects.filter(system_name=request.GET.get('system_name'),
                                                  service_name=request.GET.get('service_name'))
        response['list'] = json.loads(serializers.serialize("json", record))
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)


@require_http_methods(["POST"])
def modify_mapper(request):
    response = {}
    try:
        params = json.loads(request.body)
        mapper_list = ServiceNameMapper.objects.filter(original_name=params['original_name'])
        if mapper_list is not None and mapper_list.__len__() > 0:
            mapper = mapper_list[0]
            mapper.__setattr__('show_name', params['show_name'])
        else:
            mapper = ServiceNameMapper(original_name=params['original_name'],
                                       show_name=params['show_name'])
        mapper.save()
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_mapper(request):
    response = {}
    try:
        mapper = ServiceNameMapper.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", mapper))
        response['msg'] = "success"
        response['error_code'] = 0
    except Exception as e:
        print(e)
        response['msg'] = "请求异常"
        response['error_code'] = 1001

    return JsonResponse(response)


def get_show_name(original_name):
    mapper = ServiceNameMapper.objects.filter(original_name=original_name)
    if mapper is not None and mapper.__len__() > 0:
        return mapper[0].__getattribute__('show_name')
    else:
        return original_name
