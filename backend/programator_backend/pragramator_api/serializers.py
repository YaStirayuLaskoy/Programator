from rest_framework import serializers

from shifts.models import Worker, Day, Shift, Event


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('fisrt_name', 'last_name', 'otchestvo')


class DaySerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    day_of_week = serializers.SerializerMethodField()

    class Meta:
        model = Day
        fields = ('date', 'day', 'day_of_week')

    def get_day(self, obj):
        return obj.date.strftime('%d')

    def get_day_of_week(self, obj):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                        'Friday', 'Saturday', 'Sunday']
        return days_of_week[obj.date.weekday()]

    def validate_date(self, value):
        if Day.objects.filter(date=value).exists():
            raise serializers.ValidationError(
                "День с такой датой уже существует."
            )
        return value


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name')


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('worker', 'start_time', 'end_time', 'day', 'event')
