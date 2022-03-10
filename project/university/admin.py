from django.contrib import admin

from .models import *
# from django.contrib import admin

# Register your models here.
# usr = get_user_model()


admin.site.register(Section)
admin.site.register(Teaches)
admin.site.register(Takes)
admin.site.register(Advisor)
admin.site.register(Time_slot)
admin.site.register(Prereq)

class Classroom_Admin(admin.ModelAdmin):
    list_display = ('id', 'building', 'room_number', 'capacity' )
    list_display_links = ('building', 'room_number', 'capacity' )
    list_filter = ('building', 'room_number' )

    search_fields = ('building', 'room_number')

    list_per_page = 10
admin.site.register(Classroom, Classroom_Admin)


class Course_Admin(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'dept_name')
    list_display_links = ('course_id', 'title', 'dept_name')
    list_filter = ('dept_name',)

    search_fields = ('course_id', 'title')

    list_per_page = 10
admin.site.register(Course, Course_Admin)


class Department_Admin(admin.ModelAdmin):
    list_display = ( 'dept_name', 'building', 'budget')
    list_display_links = ( 'dept_name', 'building', 'budget')
    # list_filter = ('dept_name', 'building', 'budget')

    # search_fields = ('course_id', 'title')

    list_per_page = 10
admin.site.register(Department, Department_Admin)