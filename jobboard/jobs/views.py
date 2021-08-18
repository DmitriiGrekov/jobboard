from django.contrib.auth.decorators import login_required
from jobs.forms import JobForm, ResumeForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.contrib import messages
from .models import JobModel, JobCategory
from django.db.models import Q


class JobsListView(View):
    """
        Контроллер для вывода всех вакансий
    """

    def get_gender(self):
        return JobModel.GENDER_CHOICES

    def get_employment_choices(self):
        return JobModel.EMPLOYMENT_CHOICES

    def get_experience_choices(self):
        return JobModel.EXPERIENCE_CHOICES

    def get_category(self):
        return JobCategory.objects.all()

    def get(self, request):
        vacancies = JobModel.objects.all().order_by('-date_publish')
        paginator = Paginator(vacancies, 1)
        page = request.GET.get('page')
        vacancies = paginator.get_page(page)
        context = {}
        context['vacancies'] = vacancies
        context['gender_choices'] = self.get_gender()
        context['employment_choices'] = self.get_employment_choices()
        context['experience_choices'] = self.get_experience_choices()
        context['category'] = self.get_category()
        # f = JobsFilters(request.GET, queryset=JobModel.objects.all())
        return render(request, 'jobs/list.html', context)


class JobListFilterView(View):
    """
        Кoнтроллер для вывода на экран вакансий в соответствии с фильтром
    """
    def get_gender(self):
        return JobModel.GENDER_CHOICES

    def get_employment_choices(self):
        return JobModel.EMPLOYMENT_CHOICES

    def get_experience_choices(self):
        return JobModel.EXPERIENCE_CHOICES

    def get_category(self):
        return JobCategory.objects.all()

    def get(self, request):
        keyword = request.GET.get('keyword') if request.GET.get('keyword') else 'None'
        gender = request.GET.get('gender')
        employment = request.GET.get('employment') if request.GET.get('employment') else 'None'
        experience = request.GET.get('experience') if request.GET.get('experience') else 'None'
        category = request.GET.get('category')
        if category != 'Category':
            category = JobCategory.objects.get(pk=category)
            url = request.get_full_path()
            vacancies = JobModel.objects.filter(
                 Q(title__icontains=keyword) |
                 Q(description__icontains=keyword) |
                 Q(responsibility__icontains=keyword) |
                 Q(qualifications__icontains=keyword) |
                 Q(benefits__icontains=keyword) |
                 Q(gender=gender) |
                 Q(employment=employment) |
                 Q(experience=experience) |
                 Q(category=category)
                                            )
        else:
            url = request.get_full_path()
            vacancies = JobModel.objects.filter(
                 Q(title__icontains=keyword) |
                 Q(description__icontains=keyword) |
                 Q(responsibility__icontains=keyword) |
                 Q(qualifications__icontains=keyword) |
                 Q(benefits__icontains=keyword) |
                 Q(gender=gender) |
                 Q(employment=employment) |
                 Q(experience=experience)
                                            )
        paginator = Paginator(vacancies, 1)
        page = request.GET.get('page')
        vacancies = paginator.get_page(page)
        context = {}
        context['vacancies'] = vacancies
        context['gender_choices'] = self.get_gender()
        context['employment_choices'] = self.get_employment_choices()
        context['experience_choices'] = self.get_experience_choices()
        context['category'] = self.get_category()
        context['url'] = url
        return render(request, 'jobs/list.html', context)


class JobsDetailView(View):
    """
        Контроллер для вывода на экран детальной страницы вакансии
    """
    def get(self, request, pk):
        vacancy = JobModel.objects.get(pk=pk)
        context = {}
        context['vacancy'] = vacancy
        context['form'] = ResumeForm()
        if request.user.is_authenticated:
            for resume in request.user.resume.all():
                if vacancy == resume.vacancy:
                    context['already_sended'] = True
                    break
        return render(request, 'jobs/detail.html', context)

    def post(self, request, pk):
        vacancy = JobModel.objects.get(pk=pk)
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.vacancy = vacancy
            new_resume.save()
            request.user.resume.add(new_resume)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Отклик успешно отправлен')
            return redirect(reverse("jobs:detail", kwargs={'pk': pk}))


@login_required
def create_job_view(request):
    """
        Контроллер для создания вакансии
    """
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            new_job = form.save()
            request.user.jobs.add(new_job)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Вакансия успешно создана')
            return redirect(reverse('jobs:list'))
    else:
        form = JobForm()
        return render(request, 'jobs/create_job.html', {'form': form})
