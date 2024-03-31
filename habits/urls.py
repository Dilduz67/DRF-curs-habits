from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIview, HabitListAPIview, HabitUpdateAPIview, HabitRetrieveAPIview, \
    HabitDeleteAPIview, UserHabitListAPIView

app_name = HabitsConfig.name

router = DefaultRouter()

urlpatterns = [
    path('habit/create/', HabitCreateAPIview.as_view(), name='habit_create'),
    path('', HabitListAPIview.as_view(), name='habits_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIview.as_view(), name='habit_get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIview.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDeleteAPIview.as_view(), name='habit_delete'),
    path('user_habits/', UserHabitListAPIView.as_view(), name='user_habits'),
]