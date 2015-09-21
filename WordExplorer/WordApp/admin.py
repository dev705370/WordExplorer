from django.contrib import admin
from WordApp.models import Word, Root, WordRoot, Adjective, Noun
from autocomplete_light import shortcuts


class RootAdmin(admin.ModelAdmin) :
    fieldsets = [
        ('Root', {'fields': ['word', 'meaning']}),
        ('Comment', {'fields' : ['comment'], 'classes': ['collapse']}),
        ]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class MyApp1Admin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

class RootWordAdmin(admin.ModelAdmin) :
    fieldsets = [
        ('Root Word', {'fields': ['word', 'meaning']}),
        ('Comment', {'fields' : ['comment'], 'classes': ['collapse']}),
        ]
    list_display = ('word', 'meaning', 'comment')
    list_filter = ['word']
    search_fields = ['word']

class AutoCompleteAdmin(admin.ModelAdmin):
    form = shortcuts.modelform_factory(Word_Root_Relationship, exclude=['word_id'])

class WordAdmin(admin.ModelAdmin) :
    fieldsets = [
        ('Word', {'fields': ['word', 'meaning']}),
        ('Comment', {'fields': ['comment'], 'classes': ['collapse']}),
        ]
#class RootWOrdAutoComplete(autocomplete_light.AutocompleteModelBase):
#    search_fields = ['^word']
#    model = RootWord

#admin.site.register(Word_Root_Relationship, AutoCompleteAdmin)

#autocomplete_light.register(RootWOrdAutoComplete)

#admin.site.register(MyApp1, MyApp1Admin)
admin.site.register(RootWord, RootWordAdmin)
admin.site.register(Word, WordAdmin)
