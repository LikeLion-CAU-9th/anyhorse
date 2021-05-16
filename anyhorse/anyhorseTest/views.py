from django.shortcuts import render
def anyhorseTest1(request):
    return render(request, 'test.html')
    
def anyhorseTest2(request):
    return render(request, 'result.html')