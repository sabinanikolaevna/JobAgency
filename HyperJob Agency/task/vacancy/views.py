from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy as vacancy_model_manager

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html', context={'vacancies': vacancy_model_manager.objects.all()})
