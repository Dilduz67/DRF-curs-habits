from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User
from habits.models import Habit


class HabitTestCase(APITestCase):

    def setUp(self):
        """ Подготовка к тестированию """
        self.user = User(
            email="test@gmail.com",
            password="test",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        self.user.set_password("test")
        self.user.save()

        #self.client = APIClient()
        #token = AccessToken.for_user(user=self.user)
        #self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_habit(self):
         """ Тест создания привычки """
         self.client.force_authenticate(user=self.user)
         data = {
             "user": self.user.id,
             "place": "Парк",
             "time": "11:00:00",
             "action": "Пробежать 3 км",
             "is_pleasant": False,
             "is_useful": True,
             "periodicity": "weekly",
             "reward": "Попить кефир",
             "duration": 15,
             "is_public": True
         }

         response = self.client.post('/habit/create/', data=data, format='json')
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
         self.assertTrue(Habit.objects.all().exists())

    def test_get_share_habits(self):
        """ Тест получения информации о общедоступных привычках """
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "place": "Парк",
            "time": "11:00:00",
            "action": "Пробежать 3 км",
            "is_pleasant": False,
            "is_useful": True,
            "periodicity": "weekly",
            "reward": "Попить кефир",
            "duration": 15,
            "is_public": True
        }

        self.client.post('/habit/create/', data=data, format='json')
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_full_information_habit(self):
        """ Тест получения полной информации о привычке пользователя """
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "place": "Спортзал",
            "time": "11:00:00",
            "action": "Пробежать 3 км",
            "is_pleasant": False,
            "is_useful": True,
            "periodicity": "weekly",
            "reward": "Попить кефир",
            "duration": 15,
            "is_public": True
        }

        self.client.post('/habit/create/', data=data, format='json')
        habit_pk = Habit.objects.first().pk

        response = self.client.get(f"/habit/{habit_pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """ Тест обновления привычки пользователя """
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "place": "Спортзал",
            "time": "11:00:00",
            "action": "Пробежать 3 км",
            "is_pleasant": False,
            "is_useful": True,
            "periodicity": "weekly",
            "reward": "Попить кефир",
            "duration": 15,
            "is_public": True
        }
        new_data = {
            "user": self.user.id,
            "place": "Парк",
            "time": "11:00:00",
            "action": "Пробежать 10 км",
            "is_pleasant": False,
            "is_useful": True,
            "periodicity": "weekly",
            "reward": "Попить кефир",
            "duration": 15,
            "is_public": True
        }

        self.client.post('/habit/create/', data=data, format='json')
        habit_pk = Habit.objects.first().pk
        response = self.client.put(f"/habit/update/{habit_pk}/", new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_validate_duration_create_habit(self):
        """ Тест на создание привычки с продолжительностью более 120 секунд """
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "place": "Спортзал",
            "time": "11:00:00",
            "action": "Пробежать 3 км",
            "is_pleasant": False,
            "is_useful": True,
            "periodicity": "weekly",
            "reward": "Попить кефир",
            "duration": 300,
            "is_public": True
        }

        response = self.client.post('/habit/create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_pleasant_create_habit(self):
        """ Тест на создание приятной привычки с наградой """
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "place": "Спортзал",
            "time": "11:00:00",
            "action": "Пробежать 3 км",
            "is_pleasant": True,
            "is_useful": False,
            "periodicity": "weekly",
            "reward": "Попить кефир",
            "duration": 300,
            "is_public": True
        }

        response = self.client.post('/habit/create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

