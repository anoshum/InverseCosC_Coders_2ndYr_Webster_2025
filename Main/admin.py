from django.contrib import admin

# Register your models here.
from .models import User,Worker,Complain

admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Complain)