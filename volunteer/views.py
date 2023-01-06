from django.shortcuts import render

# Create your views here.
def volunteer(request):
    return render(request, 'volunteer.html')
def volunteerdetail(request):
    return render(request, 'volunteer-details.html')
def becomevolunteer(request):
    return render(request ,'become-a-volunteer.html')