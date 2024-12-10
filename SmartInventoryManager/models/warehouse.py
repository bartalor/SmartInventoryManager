from django.db import models


class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.warehouse_name
