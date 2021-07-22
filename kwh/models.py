from django.db import models

class FemsPayload(models.Model):
    payload_id = models.AutoField(primary_key=True)
    site = models.ForeignKey('FemsTrans', related_name='siteid', on_delete= models.DO_NOTHING, default='')
    dev = models.ForeignKey('FemsTrans',related_name='devid',on_delete= models.DO_NOTHING, default='')
    dev_time = models.ForeignKey('FemsTrans',related_name='devtime' ,on_delete= models.DO_NOTHING, db_column='dev_time', default='')
    payload_data = models.TextField()

    class Meta:
        db_table = 'fems_payload'
        unique_together = (('site', 'dev', 'dev_time'),)

class FemsTrans(models.Model):
    site_id = models.CharField(primary_key=True, max_length=15)
    dev_id = models.CharField(max_length=128)
    transaction_id = models.CharField(max_length=20)
    dev_time = models.CharField(max_length=128)
    eng_type = models.IntegerField()
    version = models.CharField(max_length=128)

    class Meta:
        db_table = 'fems_trans'
        unique_together = (('site_id', 'dev_id', 'dev_time'),)

