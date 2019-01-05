from django.contrib import admin
from .models import TambahPengguna, UbahPengguna, AddUser

# Register your models here.
admin.site.register(TambahPengguna)
admin.site.register(UbahPengguna)
admin.site.register(AddUser)