from django.shortcuts import render

def no_pages(request, page):
    context = {'page': page}
    return render(request, 'no_pages.html', context)