from django.contrib import admin
from .models import Schedule_PH
from .models import SchedulePH
from .models import ScheduleMath
from .models import ScheduleIt
from .models import TeachersPH
from .models import TeachersMath
from .models import TeachersIt
from .models import Contact

admin.site.register(Schedule_PH)

admin.site.register(SchedulePH)

admin.site.register(ScheduleMath)

admin.site.register(ScheduleIt)

admin.site.register(TeachersPH)

admin.site.register(TeachersMath)

admin.site.register(TeachersIt)

admin.site.register(Contact)