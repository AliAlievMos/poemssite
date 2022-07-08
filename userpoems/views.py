from django.http import HttpResponse

def index(request):
    return HttpResponse("Здесь будет список всех стихов пользователей")
