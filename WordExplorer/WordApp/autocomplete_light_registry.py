import autocomplete_light.shortcuts as al
from WordApp.models import Noun, Adjective, WordRoot
from autocomplete_light import shortcuts

shortcuts.register(WordRoot)
shortcuts.register(Noun)
shortcuts.register(Adjective)

