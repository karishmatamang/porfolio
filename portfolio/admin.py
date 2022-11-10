from django.contrib import admin

# Register your models here.
from .models import (
    PersonalPorfolio,
    Skills,
    ProfessionalSkill,
    EducationDegree,
    Hobby ,
    Experience   
)
 
admin.site.register(PersonalPorfolio)
admin.site.register(Skills)
admin.site.register(ProfessionalSkill)
admin.site.register(EducationDegree)
admin.site.register(Hobby)
admin.site.register(Experience)