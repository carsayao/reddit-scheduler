from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):    # More compact
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Move published date above question text
    # fields = ['pub_date', 'question_text']

    # Pretty fieldset form
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# Inefficient way of adding Choice objects to system. It’d be better if
# you could add a bunch of Choices directly when you create the Question object
# admin.site.register(Choice)