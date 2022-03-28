from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api.serialize import *
import datetime
# from rest_framework import serializers
import json
from django.core import serializers
# class loginview(APIView):
#     def post(self,request,*args,**kwargs):
#         print(request.data)
#         return responses('123')
# # Create your views here.

class showview(APIView):
    def get(self,request,*args,**kwargs):
        查询信息=request.query_params

        date1=dict(查询信息)['日期']
        部门=dict(查询信息)['部门'][0]
        print(部门)
        day=''.join(date1)
        日期= datetime.datetime.strptime(day, '%Y-%m-%d')

        result = models.bingyuan.objects.all()
        if len(部门)>0:
            s = models.bingyuan.objects.filter(日期=日期,部门=部门)
        else:
            s = models.bingyuan.objects.filter(日期=日期)
        s=json.loads(serializers.serialize('json',s))
        s1={'fields':[]}
        for i in s :
            s1['fields'].append(i['fields'])
            # print(i['fields'])
        # print(s[0])
        # 结果 = {'日期':[],'部门':[],'检测样本信息':[],'结果':[],'FAM值':[]}
        # for i in s:
        #     结果['日期'].append(i.日期)
        #     结果['部门'].append(i.部门)
        #     结果['检测样本信息'].append(i.检测样本信息)
        #     结果['结果'].append(i.结果)
        #     结果['FAM值'].append(i.fam值)



        # print(type(s1['fields']))
        # return Response(结果)
        return Response(s1)
        # return Response(日期)

class bingyuan(APIView):
    def get(self,request,*args,**kwargs):
        result=models.bingyuan.objects.all()
        日期=datetime.datetime(2021,10,1,0,0)
        # start = datetime.timedelta(hours=23, minutes=59, seconds=59)
        s=models.bingyuan.objects.filter(日期=日期)
        print(s)
        部门=[]
        for i in s:
            部门.append(i.部门)

        print(部门)
        return Response(部门)