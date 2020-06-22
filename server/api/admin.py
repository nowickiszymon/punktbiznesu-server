from django.contrib import admin

from .models import Rekomendacje
from .models import Wiadomosci
from .models import Zamowienia
from .models import Blog

admin.site.register(Rekomendacje)
admin.site.register(Wiadomosci)
admin.site.register(Zamowienia)
admin.site.register(Blog)
