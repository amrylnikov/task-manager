from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.utils.translation import gettext as _

from task_manager.users.forms import RegisterUserForm
from task_manager.mixins import SpecifiedLoginRequiredMixin


class UserRegister(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    success_message = _("Пользователь успешно зарегистрирован")


class UsersShow(ListView):
    model = User
    template_name = 'users.html'
    paginate_by = 100


class UserEdit(SpecifiedLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    success_url = reverse_lazy('users')
    form_class = RegisterUserForm
    success_message = _("Пользователь успешно изменен!")


class UserDelete(SpecifiedLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'auth/user_confirm_delete.html'
    success_url = reverse_lazy('users')
    success_message = _("Пользователь успешно удален")

# TODO В логине исправить сообщения в html, щас там только опасности.
# TODO Как обработать ошибку, что возникает при попытке удаления?
