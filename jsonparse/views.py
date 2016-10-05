from django.shortcuts import render_to_response, HttpResponse
from .models import Group, Countries
import json
from collections import OrderedDict
#
#
# def data_processing(request):
#
#     with open('/home/ivan/parseenv/bin/parse/jsonparse/eFw3Cefj.json', 'r') as data_file:
#         data = json.load(data_file, object_pairs_hook=OrderedDict)
#
#     data1 = data['data']
#     for i in range(len(data1)):
#         Group.objects.get_or_create(region=data1[i]['Регион'],
#                                      country=data1[i]['Страна'],
#                                      value=data1[i]['Значение'])
#
#     group_list = Group.objects.all().values_list('region', flat=True).distinct()
#     ctr_val = []
#     for item in list(group_list):
#         ctr_val.append(list(Group.objects.filter(region=item).values_list('country', 'value')))
#
#     country_val = []
#     for i in ctr_val:
#         country_val.append(list(map(list, i)))
#
#     return render_to_response('main.html', {'groups': Group.objects.all()})


def data_processing(request):
    with open('/home/ivan/parseenv/bin/parse/jsonparse/eFw3Cefj.json', 'r') as data_file:
        data = json.load(data_file, object_pairs_hook=OrderedDict)

    data1 = data['data']
    for i in range(len(data1)):
        Group.objects.get_or_create(group_region=data1[i]['Регион'])
        Countries.objects.get_or_create(country_name=data1[i]['Страна'],
                                        country_value=data1[i]['Значение'],
                                        country_from_id=Group.objects.get(group_region=data1[i]['Регион']).id)
    return render_to_response('output.html', {'groups': Group.objects.all()})


def data_container(request, group_id):
    countries = Countries.objects.filter(country_from=group_id).values_list('country_name', 'country_value')
    country_val = (list(map(list, countries)))
    return render_to_response('output.html', {'country': country_val, 'group_id': group_id, 'groups': Group.objects.all()})
