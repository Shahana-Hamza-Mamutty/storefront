from django.shortcuts import render


def say_hello(request):
    test_variable = "dsadas"
    return render(request, 'hello.html', {'name': 'Mosh'})
