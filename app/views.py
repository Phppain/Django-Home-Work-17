from django.shortcuts import render, redirect

def is_login(request):
    if not request.user.is_authenticated:
        return redirect('/other_page')
    else:
        return render(request, 'auth_page.html')

def other_page(request):
    return render(request, 'other_page.html')