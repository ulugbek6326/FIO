from django.shortcuts import render
from .models import Fio

# Create your views here.




def fio(request):
    if request.method == 'POST':
        format = request.POST.get('fio')
        a = ''
        li = []
        for i in str(format) + ' ':
            if ' ' == i:
                if a != '':
                    li.append(a)
                    a = ''
            else:
                a += i
        result = Fio(first_name=li[1], last_name=li[0], middle_name=li[2])
        result.save()
    results = Fio.objects.all().order_by('-id').first()
    return render(request,'index.html', {'results':results})







# def fio(request):
#     if request.method == 'POST':
#         format = request.POST.get('fio')
#         a = ''
#         li = []
#         for i in str(format) + ' ':
#             if ' ' == i:
#                 if a != '':
#                     li.append(a)
#                     a = ''
#             else:
#                 a += i
#         result = Fio(first_name=li[1], last_name=li[0], middle_name=li[2])
#         result.save()
#         return HttpResponse(str(result))
#     return render(request,'index.html')







