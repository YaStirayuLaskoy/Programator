from rest_framework import serializers

from shifts.models import Worker, Day, Shift


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('fisrt_name', 'last_name', 'otchestvo')


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('start_time', 'end_time', 'worker', 'day', 'event')
