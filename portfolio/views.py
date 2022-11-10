from django.shortcuts import render,redirect
from .models import (
    PersonalPorfolio,
    Experience,
    Hobby,
    ProfessionalSkill,
    Skills,
    EducationDegree
)

# Create your views here.
def home(request):

    details=PersonalPorfolio.objects.all().last()
    experience=Experience.objects.all()
    hobby=Hobby.objects.all()
    professionskill=ProfessionalSkill.objects.all()
    skill=Skills.objects.all()
    education=EducationDegree.objects.all()
    context={
        "object":details,
        "experience_obj":experience,
        "hobby_obj":hobby,
        "professionskill_obj":professionskill,
        "skill_obj":skill,
        "education_obj":education
    }
    return render(request,'home.html',context)

