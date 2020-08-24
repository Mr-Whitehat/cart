from django.http import HttpResponse

def index(request):
    return HttpResponse('''<center><h1><strong>Hello cart!</h1></strong><br>
                        <a href="https://www.google.com/">Google</a><br><br>
    <a href="https://www.youtube.com/" target="_blank">YouTube</a></center>'''  )