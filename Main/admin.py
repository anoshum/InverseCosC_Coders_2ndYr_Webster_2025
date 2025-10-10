from django.contrib import admin

# Register your models here.
from .models import Usr,Worker,Complain

admin.site.register(Usr)
admin.site.register(Worker)
admin.site.register(Complain)