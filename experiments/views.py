from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt

from experiments.models import SensorRecord


def sensor_records(request):
    records = SensorRecord.objects.order_by('-id')
    context = {'records': records}
    return render(request, 'experiments/sensorrecords.html', context)


@csrf_exempt
def add_record(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        record = SensorRecord()
        record.value = value
        today = datetime.now()
        record.date_recorded = today.strftime("%Y-%m-%d %H:%M:%S")
        record.save()
        return JsonResponse({'status': 'Success'})
    else:
        return JsonResponse({'status': 'Failure'})

