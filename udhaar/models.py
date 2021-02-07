from django.db import models

class Party(models.Model):
    dbname=models.CharField(max_length=30)
    

    def __str__(self):
     return self.dbname

class Transactions(models.Model):
    dbparty=models.ForeignKey(Party, on_delete=models.CASCADE)
    dbdate=models.DateField()
    dbamount=models.SmallIntegerField(null=True,blank=True)
    description=models.CharField(max_length=30)
    trace=models.CharField(max_length=30)
    credit_debit=models.SmallIntegerField(null=True,blank=True)



    