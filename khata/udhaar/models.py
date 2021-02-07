from django.db import models

class Party(models.Model):
    dbname=models.CharField(max_length=30)
    dbnumber=models.PositiveSmallIntegerField(null=True,blank=True)
    balance=models.FloatField(default =0.0)

    def __str__(self):
     return self.dbname

class Transactions(models.Model):
    dbparty=models.ForeignKey(Party, on_delete=models.CASCADE)
    dbdate=models.DateField()
    dbamount=models.PositiveSmallIntegerField(null=True,blank=True)
    description=models.CharField(max_length=30)

  