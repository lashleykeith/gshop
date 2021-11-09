from django.contrib import admin

from .models import Course, Enrollment, Announcement, Comment, Lesson, Material, GettingStarted, Week, Assignments, TeacherComments, WeeklyComment, Feedback, AdminComment, FeedbackForAdmin

class CourseAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date','created_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug' : ('name',)}

class MaterialInlineAdmin(admin.StackedInline):

	model = Material

class LessonAdmin(admin.ModelAdmin):

	list_display = ['name', 'number', 'course', 'release_date']
	search_fields = ['name', 'description']
	list_filter = ['created_at']

	inlines = [
		MaterialInlineAdmin
	]


admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
admin.site.register(GettingStarted)
admin.site.register(Assignments)
admin.site.register(Week)
admin.site.register(WeeklyComment)
admin.site.register(TeacherComments)
admin.site.register(Feedback)
admin.site.register(AdminComment)
admin.site.register(FeedbackForAdmin)