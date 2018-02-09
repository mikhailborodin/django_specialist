from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .models import Question, Choice
from .resources import QuestionResource

class CommonAdmin(ImportExportModelAdmin):
    list_per_page = 10
    save_as = True

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(CommonAdmin):
    list_display = ('id', 'pub_date', 'question_text', 'type', '_link', 'published')
    list_filter = ('type', 'pub_date',)
    date_hierarchy = 'pub_date'
    resource_class = QuestionResource
    search_fields = ('question_text',)
    actions = ['make_published']
    inlines = [
        ChoiceInline,
    ]
    ordering = ('id', '-pub_date',)

    def make_published(self, request, queryset):
        queryset.update(published=True)

    make_published.short_description = 'Опубликовать'

    def _link(self, obj):
        return mark_safe('<a target="_blank" href="%s">--></a>' % obj.get_absolute_url())

admin.site.site_header = 'My admin'
admin.site.register(Permission)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
