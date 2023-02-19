from django.shortcuts import render
from .models import SchedulePH
from .models import ScheduleMath
from .models import ScheduleIt
from .models import TeachersPH
from .models import TeachersIt
from .models import TeachersMath
from .models import Contact
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


#def about(request):
  #  return render(request, 'main/about.html')


def education(request):
    return render(request, 'main/education.html')


# def schedule(request):
#     return render(request, 'main/schedule.html')
#

def teachers(request):
    return render(request, 'main/teachers.html')



def contact(request):
    return render(request, 'main/contact.html')

def aboutRINX(request):
    return render(request, 'main/aboutRINX.html')


def physics(request):
    sheds = SchedulePH.objects.all()
    teacherPH = TeachersPH.objects.all()
    return render(request, 'main/physics.html', {'title':'Физика', 'sched': sheds, 'teacherPH':teacherPH} )


def mathematics(request):
    sheds = ScheduleMath.objects.all()
    teacherMath = TeachersMath.objects.all()
    return render(request, 'main/mathematics.html', {'title':'Математика', 'sched': sheds, 'teacherMath':teacherMath} )


def computer(request):
    sheds = ScheduleIt.objects.all()
    teacherIt = TeachersIt.objects.all()
    return render(request, 'main/computer.html', {'title':'Математика', 'sched': sheds, 'teacherIt': teacherIt}  )

def contactKB(request):
    Contacts = Contact.objects.all()
    return render(request, 'main/contactKB.html', {'title':'Контакты','Contacts': Contacts})


def gallery(request):
    return render(request, 'main/gallery.html')