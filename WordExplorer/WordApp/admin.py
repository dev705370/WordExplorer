from django.contrib import admin
from WordApp.models import Word, Root, WordRoot, Adjective, Noun
from autocomplete_light import shortcuts


class Root_WordAdmin(admin.ModelAdmin) :
    fieldsets = [
        ('Root', {'fields': ['word', 'meaning']}),
        ('Comment', {'fields' : ['comment'], 'classes': ['collapse']}),
        ]
    list_display = ('word', 'meaning', 'comment')
    list_filter = ['word']
    search_fields = ['word']

admin.site.register(Root, Root_WordAdmin)
admin.site.register(Word, Root_WordAdmin)

class WordRootAdmin(admin.ModelAdmin):
    form = shortcuts.modelform_factory(WordRoot, exclude=[])
    extra = 5
admin.site.register(WordRoot, WordRootAdmin)

class NounAdmin(admin.ModelAdmin):
    form = shortcuts.modelform_factory(Noun, exclude=[])
admin.site.register(Noun, NounAdmin)

class AdjectiveAdmin(admin.ModelAdmin):
    form = shortcuts.modelform_factory(Adjective, exclude = [])
admin.site.register(Adjective, AdjectiveAdmin)