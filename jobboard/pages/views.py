from django.views.generic.list import ListView
from accounts.models import AdvUser


class CandidatesView(ListView):
    """
        Контроллер для вывода страницы с кандидатами
    """
    template_name = 'pages/list.html'
    context_object_name = 'candidates'
    paginate_by = 1

    def get_queryset(self):
        return AdvUser.objects.filter(type_user='applicant')
