from django.shortcuts import render_to_response, HttpResponse
from .models import Group, Countries
import json
from collections import OrderedDict


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
    return render_to_response('output.html', {'country': country_val,
                                              'group_id': group_id,
                                              'groups': Group.objects.all(),
                                              'region': Group.objects.get(pk=group_id)
                                              })
