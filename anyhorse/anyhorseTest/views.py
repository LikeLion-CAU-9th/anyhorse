from django.shortcuts import render

def anyhorseTest(request):
    return render(request, 'horseTest.html')