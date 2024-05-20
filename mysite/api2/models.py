from django.db import models
class DataShow(models.Model):
    index = models.BigIntegerField()
    DVC_Code = models.TextField()
    Company_Name = models.TextField()
    Business_Nature = models.TextField()
    Business_Sector = models.TextField()
    Business_Industry = models.TextField()
    Listed = models.TextField()
    Legal_Status = models.TextField()
    User_Key = models.TextField()
    User_Name = models.TextField()
    Firm_Key = models.TextField()
    Firm_Name = models.TextField()
    Service_Category = models.TextField()
    Service_Name = models.TextField()
    Document_Date = models.TextField()
    Document = models.TextField()
    Reference_Law = models.TextField()
    DVC_Date = models.DateTimeField()
    Month = models.IntegerField()
    Day = models.IntegerField()
    Year = models.IntegerField()
    class Meta:
        db_table = 'todatabase'


