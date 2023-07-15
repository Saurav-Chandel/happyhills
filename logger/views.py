from django.shortcuts import render
# from db_logger import StatusLogs
# Create your views here.

def Logger(request):
    a=StatusLogs.objects.all()
    print(a)
    return HttpResponse(a)
