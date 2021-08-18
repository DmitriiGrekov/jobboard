from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.signing import BadSignature

from jobs.models import JobModel, ResumeMessageModel
from .forms import UserRegisterForm, UserUpdateForm
from .dispatch.dp_send_mes import signer
from .models import AdvUser
from jobs.models import ResumeModel
from jobs.forms import ResumeCommentForm


class UserLoginView(LoginView):
    """Контроллер авторизации пользователя"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LoginRequiredMixin, LogoutView):
    """Контроллер выхода из учетной записи пользователя"""
    template_name = 'accounts/logout.html'


class UserRegisterView(SuccessMessageMixin, CreateView):
    """Контроллер для регистрации пользователя"""
    template_name = 'accounts/register.html'
    model = AdvUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts:login')
    success_message = 'Вы успешно зарегестрированы, пожалуйста, активируйте \
                       свой аккаунт, перейдя по ссылке в письме'


def activate_user(request, token):
    """
    Функция проверки токена регистрации пользователя
    """
    try:
        username = signer.unsign(token)
    except BadSignature:
        return render(request, 'accounts/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_active:
        template = 'accounts/user_is_active.html'
    else:
        template = 'accounts/activation_done.html'
        user.is_active = True
        user.save()
    return render(request, template)


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
        Контроллер для изменения пароля пользователя
    """
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:change_password')
    success_message = 'Пароль успешно изменен'


class UserProfileView(LoginRequiredMixin, TemplateView):
    """
        Контроллер для вывода профиля пользователя
    """
    template_name = 'accounts/profile.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
        Контроллер для изменения данных пользователя
    """
    template_name = 'accounts/user_update.html'
    model = AdvUser
    form_class = UserUpdateForm
    success_url = reverse_lazy('accounts:profile')


@login_required
def add_favourits_jobs(request, pk):
    """
        Контроллер для добавления вакансии
    """
    job = JobModel.objects.get(pk=pk)
    request.user.favourits.add(job)
    messages.add_message(request,
                         messages.SUCCESS,
                         'Вакансия успешно добавлена в избранное')
    return redirect(reverse('accounts:show_favourits'))


@login_required
def delete_favourits(request, pk):
    """
        Контроллер для удаления вакансии
    """
    job = JobModel.objects.get(pk=pk)
    request.user.favourits.remove(job)
    messages.add_message(request,
                         messages.SUCCESS,
                         'Вакансия успешно убрана из избранного')
    return redirect(reverse('accounts:show_favourits'))


class ShowFavourtisView(LoginRequiredMixin, TemplateView):
    """
        Контроллер для показа избранных вакансий пользователя
    """
    template_name = 'accounts/favourits_jobs.html'


class ShowResumeView(LoginRequiredMixin, TemplateView):
    """
        Контроллер для вывода на экран откликов пользователя на вакансии
    """
    template_name = 'accounts/resume_jobs.html'


@login_required
def detail_resume_view(request, pk):
    """
        Контроллер для вывода на экран детальной страницы отклика на вакансию,
        с формой обратной связи
    """
    if request.method == 'POST':
        form = ResumeCommentForm(request.POST)
        if form.is_valid():
            resume = ResumeModel.objects.get(pk=pk)
            new_form = form.save(commit=False)
            new_form.resume = resume
            new_form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Сообщение успешно отправлено')
            return redirect(reverse('accounts:detail_resume',
                                    kwargs={'pk': pk}))
    else:
        resume = ResumeModel.objects.get(pk=pk)
        comments = ResumeMessageModel.objects.filter(resume=resume).order_by('-date_publish')
        context = {}
        context['comments'] = comments
        context['resume'] = ResumeModel.objects.get(pk=pk)
        context['form'] = ResumeCommentForm()
        return render(request, 'accounts/resume_detail.html', context)


class ShowUserVacancy(LoginRequiredMixin, TemplateView):
    """
        Контроллер для вывода вакансий данного пользователя
    """
    template_name = 'accounts/user_vacancy.html'


@login_required
def delete_jobs_user(request, pk):
    """
        Контроллер для удаления вакансии пользователя
    """
    job = JobModel.objects.get(pk=pk)
    if job in request.user.jobs.all():
        job.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             'Вакансия успешно удалена')
        return redirect(reverse('accounts:show_jobs'))
    else:
        messages.add_message(request,
                             messages.SUCCESS,
                             'У вас нет доступа, для удаления данной вакансии')
        return redirect(reverse('accounts:show_jobs'))


@login_required
def view_all_responses(request):
    """
        Контроллер для вывода на экран списка откликов пользователя,
        если пользователь является соискателем
    """
    if request.user.type_user == 'employment':
        responses = []
        for job in request.user.jobs.all():
            for resume in job.resume_user.all():
                responses.append(resume)
        context = {}
        context['responses'] = responses
        return render(request,
                      'accounts/jobs_response.html',
                      context)
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'У вас нет дуступа к списку откликов на вакансию')
        return redirect(reverse('accounts:profile'))


@login_required
def delete_resume_view(request, pk):
    """
        Контроллер для удаления отклика
    """
    resume = ResumeModel.objects.get(pk=pk)
    if resume in request.user.resume.all():
        resume.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             'Ваш отклик успешно удален')
        return redirect(reverse("accounts:show_resume"))
    else:
        messages.add_message(request,
                             messages.INFO,
                             'Этот отклик не принадлежит вам')
        return redirect(reverse('accounts:show_resume'))
