from django.db import models


class Schedule_PH(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    dataD = models.CharField('Дата', max_length=25)
    mode = models.CharField('Режим', max_length=30)

    def __str__(self):
        return self.title

class SchedulePH(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    dataD = models.CharField('Дата', max_length=25)
    mode = models.CharField('Режим', max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural='Расписание по физике'



class ScheduleMath(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    dataD = models.CharField('Дата', max_length=25)
    mode = models.CharField('Режим', max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural='Расписание по математике'


class ScheduleIt(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    dataD = models.CharField('Дата', max_length=25)
    mode = models.CharField('Режим', max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural='Расписание по информатике'


class TeachersPH(models.Model):
    title = models.CharField('ФИО', max_length=75)
    description = models.CharField('Должность', max_length=256)
    dataD = models.CharField('Ученая степень', max_length=256)
    mode = models.CharField('Ссылка на фотографию', max_length=256)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Преподавателя'
        verbose_name_plural='Преподаватели по физике'

class TeachersPH(models.Model):
    title = models.CharField('ФИО', max_length=75)
    description = models.CharField('Должность', max_length=256)
    dataD = models.CharField('Ученая степень', max_length=256)
    mode = models.CharField('Ссылка на фотографию', max_length=256)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Преподавателя'
        verbose_name_plural='Преподаватели по физике'

class TeachersMath(models.Model):
    title = models.CharField('ФИО', max_length=75)
    description = models.CharField('Должность', max_length=256)
    dataD = models.CharField('Ученая степень', max_length=256)
    mode = models.CharField('Ссылка на фотографию', max_length=256)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Преподавателя'
        verbose_name_plural='Преподаватели по математике'


class TeachersIt(models.Model):
    title = models.CharField('ФИО', max_length=75)
    description = models.CharField('Должность', max_length=256)
    dataD = models.CharField('Ученая степень', max_length=256)
    mode = models.CharField('Ссылка на фотографию', max_length=256)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Преподавателя'
        verbose_name_plural='Преподаватели по информатике'


class Contact(models.Model):
    title = models.CharField('ФИО', max_length=75)
    description = models.CharField('Описание', max_length=256)
    mode = models.CharField('Ссылка на фотографию', max_length=256)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural='Контакты ответственных за проведение школы'
