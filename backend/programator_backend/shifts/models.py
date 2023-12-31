from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model


class Worker(models.Model):
    """Модель сотрудника."""
    fisrt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    otchestvo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fisrt_name} {self.last_name} {self.otchestvo}"


class Day(models.Model):
    """Модель для представления дней месяца."""
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)


class Event(models.Model):
    """Модель типа посещаемости (отпуск/выходной/.../)."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shift(models.Model):
    """Модель смены."""
    start_time = models.TimeField()
    end_time = models.TimeField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.worker} {self.start_time} {self.end_time} {self.day} "
                f"{self.event}")
