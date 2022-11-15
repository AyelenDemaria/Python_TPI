from django.contrib import admin
from .models import Cuota
from .views import reporte_pagos, reporte_morosos

admin.site.register_view('reporte-pagos', 'Reporte Pagos', view=reporte_pagos)
admin.site.register_view('reporte-morosos', 'Reporte Socios Morosos', view=reporte_morosos)

admin.site.register(Cuota)
