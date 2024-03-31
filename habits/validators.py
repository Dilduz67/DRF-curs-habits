from rest_framework.serializers import ValidationError

class DurationValidator:
    def __init__(self, field):
        self.field = field
    def __call__(self, value):
        duration = value.get(self.field)
        if duration > 120:
            raise ValidationError('Время для привычки не может быть более 120 секунд.')


class PleasantRewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tmp_field1 = dict(value).get(self.field1)
        tmp_field2 = dict(value).get(self.field2)
        if tmp_field1==True and tmp_field2 != None:
            raise ValidationError('У приятной привычки не может быть вознаграждения')


class PleasantUsefulValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2
    def __call__(self, value):
        tmp_field1 = dict(value).get(self.field1)
        tmp_field2 = dict(value).get(self.field2)
        if tmp_field1 == True and tmp_field2 == True:  # not "is" nor "=="
            raise ValidationError('У приятной привычки не может быть связанной полезной привычки.')


class PeriodsValidator:
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        possible_values = ['daily', 'weekly']
        tmp_field1 = dict(value).get(self.field1)
        if tmp_field1 not in possible_values:
            raise ValidationError('Неверный интервал.')
#