from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306213003',
        'name': 'Daffa Naufal Rahadian',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
