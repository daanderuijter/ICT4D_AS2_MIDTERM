from django.contrib import admin

# Register your models here.

from .models import Choice, Question, Topic

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Topic', {'fields': ['topic']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'topic')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class TopicAdmin(admin.ModelAdmin):
    fields = ['topic_text']
    list_display = ('topic_text', 'question_count', 'get_wikipedia_article')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, TopicAdmin)
