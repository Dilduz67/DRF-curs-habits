from rest_framework import serializers

from habits.models import Habit
from habits.validators import DurationValidator, PleasantRewardValidator,PleasantUsefulValidator, PeriodsValidator

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            DurationValidator(field='duration'),
            PleasantRewardValidator(field1='is_pleasant', field2='reward'),
            PleasantUsefulValidator(field1='is_pleasant', field2='is_useful'),
            PeriodsValidator(field1='periodicity')
        ]