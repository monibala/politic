from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index-2.html')
def events(request):
    return render(request, 'events.html')
def eventdetail(request):
    return render(request, 'events-details.html')
def gallery(request):
    return render(request, 'gallery.html')
def history(request):
    return render(request, 'history.html')
def donate(request):
    return render(request, 'donate.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faq.html')