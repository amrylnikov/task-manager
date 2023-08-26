import django_filters
from django.contrib.auth.models import User

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    # username = django_filters.CharFilter(method='my_custom_filter')
    # author = django_filters.BooleanFilter
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all(), label='Статус')
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all(), label='Исполнитель')
    labels = django_filters.ModelMultipleChoiceFilter(queryset=Label.objects.all(), label='Метка')

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
