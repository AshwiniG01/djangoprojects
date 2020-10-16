from django.shortcuts import render
from datetime import datetime

# Create your views here.
def display_time(request):
	server_time=datetime.now()
	hour=int(datetime.now().hour)
	msg="Welcome to study online,Good"
	if hour>0 and hour<12:
		msg=msg+"morning"
	elif hour>12 and hour<16:
		msg=msg+"afternoon"
	elif hour>16 and hour<21:
		msg+msg+"evening"
	else:
		msg=msg+"night"
	msg=msg
	data={'msg':msg,'time':server_time}
	return render(request=request, template_name='timeapp/timee.html',context=data)

