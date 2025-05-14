from django.contrib import admin
from .models import BirthChartRequest, RitualBooking, WitchQuestion, DreamInterpretation

admin.site.register(BirthChartRequest)
admin.site.register(RitualBooking)
admin.site.register(WitchQuestion)
admin.site.register(DreamInterpretation)

