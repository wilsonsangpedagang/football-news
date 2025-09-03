from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406365244',
        'name': 'Davin Muhammad Hijran',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)
