from django.contrib import admin
# Register your models here.
from .models import Question,Choice

class ChioceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,      {'fields':['question_text']}),
        ('Date infortion',{'fields':['pub_date']}),
    ]
    inlines = [ChioceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)