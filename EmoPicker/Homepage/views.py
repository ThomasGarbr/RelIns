from django.shortcuts import render
from .models import DataSetText
import random
# Create your views here.
def hello(request):
    return render(request, 'hello.html', {'text': DataSetText.objects.get(pk=1)})
def home(request):
    size = DataSetText.objects.count()
    factor = float(request.GET.get("selector"))
    text = (request.GET.get("textBack", random.randint(1, size)))
    text = DataSetText.objects.get(pk=text)
    number = float(request.GET.get("buttonEmo", 0)) * factor
    text.rating += float(number)
    text.save()
    b = random.randint(1, size)
    a = DataSetText.objects.get(pk=b)
    

    return render(request, 'index.html', {'text':a, 'selector':factor})
