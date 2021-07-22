from django.db import models


class FemsPayload(models.Model):
    site = models.ForeignKey('FemsTrans', on_delete=models.CASCADE, related_name='payload' , default='')
    dev_id = models.CharField(max_length=128)
    dev_time = models.CharField(max_length=128)
    payload_data = models.TextField()

    class Meta:
        db_table = 'fems_payload'
        unique_together = (('site','dev_id', 'dev_time'),)

class FemsTrans(models.Model):
    site_id = models.CharField(primary_key=True, max_length=15)
    transaction_id = models.CharField(max_length=20)
    eng_type = models.IntegerField()
    version = models.CharField(max_length=128)

    class Meta:
        db_table = 'fems_trans'
