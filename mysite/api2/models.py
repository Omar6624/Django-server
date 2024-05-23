from django.db import models
class DataShow(models.Model):
    Index = models.BigIntegerField(primary_key=True , db_column='index')
    DVC_Code = models.TextField(db_column='DVC Code')
    Company_Name = models.TextField(db_column='Company Name')
    Business_Nature = models.TextField(db_column='Business Nature')
    Business_Sector = models.TextField(db_column='Business Sector')
    Business_Industry = models.TextField(db_column='Business Industry')
    Listed = models.TextField(db_column='Listed')
    Legal_Status = models.TextField(db_column='Legal Status')
    User_Key = models.TextField(db_column='User Key')
    User_Name = models.TextField(db_column='User Name')
    Firm_Key = models.TextField(db_column='Firm Key')
    Firm_Name = models.TextField(db_column='Firm Name')
    Service_Category = models.TextField(db_column='Service Category')
    Service_Name = models.TextField(db_column='Service Name')
    Document_Date = models.TextField(db_column='Document Date')
    Document = models.TextField(db_column='Document')
    Reference_Law = models.TextField(db_column='Reference Law')
    DVC_Date = models.DateTimeField(db_column='DVC Date')
    Month = models.IntegerField(db_column='Month')
    Day = models.IntegerField(db_column='Day')
    Year = models.IntegerField(db_column='Year')
    class Meta:
        managed = False
        db_table = 'todatabase'


