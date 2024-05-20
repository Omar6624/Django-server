from django.db import models
class DataShow(models.Model):
    report_id = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    fiscal_year = models.IntegerField()
    total_revenue = models.FloatField()
    gross_profit = models.FloatField()
    operating_expense = models.FloatField()
    net_income = models.FloatField()
    earnings_per_share = models.FloatField()
    total_assets = models.FloatField()
    total_liabilities = models.FloatField()
    shareholders_equity = models.FloatField()
    cash_flow_operations = models.FloatField()
    cash_flow_investing = models.FloatField()
    cash_flow_financing = models.FloatField()
    auditor_name = models.CharField(max_length=255)
    audit_opinion = models.CharField(max_length=50)
    report_date = models.DateField()
    filing_date = models.DateField()
    sector = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    class Meta:
        db_table = 'financial_reports'

    def __str__(self):
        return f"{self.company_name} - {self.fiscal_year}"

