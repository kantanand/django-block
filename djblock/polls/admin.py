from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', 
            {
                'fields': ['question_text','is_published','created_by']
            }
        ),
        ('Date information', 
            {
                'fields': ['pub_date'], 
                'classes': ['collapse']
            }
        ),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
