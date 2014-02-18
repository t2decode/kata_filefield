from django.contrib import admin
from kata.models import Media, Course

class MediaInline(admin.StackedInline):
    model = Media
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    inlines = [MediaInline]

admin.site.register(Media)
admin.site.register(Course, CourseAdmin)