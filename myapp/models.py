# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class TestTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class ServiceUnitRecord(models.Model):
    id = models.BigIntegerField(primary_key=True, help_text='主键')
    system_name = models.CharField(max_length=64, help_text='系统标识')
    service_name = models.CharField(max_length=64, help_text='服务标识')
    service_interface = models.CharField(max_length=64, help_text='服务接口标识')
    total_num = models.IntegerField(help_text='调用总数')
    slow_num = models.IntegerField(help_text='慢调用数')
    slow_proportion = models.FloatField(help_text='慢调用占比')
    fail_num = models.IntegerField(help_text='异常调用数')
    fail_proportion = models.FloatField(help_text='异常调用占比')
    avg_delay_sec = models.FloatField(help_text='平均耗时')
    longest_delay_sec = models.FloatField(help_text='最长耗时')
    shortest_delay_sec = models.FloatField(help_text='最短耗时')
    strategy_id = models.IntegerField(default=1, help_text='统计策略id，默认1')
    start_time = models.DateTimeField(auto_now_add=True, help_text='统计开始时间')
    end_time = models.DateTimeField(auto_now_add=True, help_text='统计结束时间')
    created_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    total_delay = 0.0


class Service(models.Model):
    id = models.BigIntegerField(primary_key=True, help_text='主键')
    system_name = models.CharField(max_length=64, help_text='系统标识')
    service_name = models.CharField(max_length=64, help_text='服务标识')
    service_interface = models.CharField(max_length=64, help_text='服务接口标识')
    created_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')


class ServiceNameMapper(models.Model):
    id = models.BigIntegerField(primary_key=True, help_text='主键')
    original_name = models.CharField(max_length=64, help_text='原始标识')
    show_name = models.CharField(max_length=64, help_text='展示标识')
    created_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')
