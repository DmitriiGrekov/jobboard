from django.views.generic.base import TemplateView


class MainIndexView(TemplateView):
    """
        Котроллер для вывода главной страницы сайта
    """
    template_name = 'main/index.html'
