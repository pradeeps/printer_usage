from django.db import models


class Post(models.Model):
    printer_name = models.CharField(max_length=200)
    locked = models.BooleanField()
    locked_by = models.CharField(max_length=200, default=None)

    def __str__(self):
        return (self.printer_name, ' locked_status: ', 'True' if locked else 'Flase')
