from django.db import models

# sales/models.py

from django.db import models

class SalesData(models.Model):
    FAT_CONTENT_CHOICES = [
        ('Low Fat', 'Low Fat'),
        ('Regular', 'Regular'),
        ('Non-Edible', 'Non-Edible'),
    ]

    LOCATION_TYPE_CHOICES = [
        ('Tier 1', 'Tier 1'),
        ('Tier 2', 'Tier 2'),
        ('Tier 3', 'Tier 3'),
    ]

    OUTLET_SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    OUTLET_TYPE_CHOICES = [
        ('Grocery Store', 'Grocery Store'),
        ('Supermarket Type1', 'Supermarket Type1'),
        ('Supermarket Type2', 'Supermarket Type2'),
        ('Supermarket Type3', 'Supermarket Type3'),
    ]

    Item_Identifier = models.CharField(max_length=50)
    Item_Weight = models.FloatField()
    Item_Fat_Content = models.CharField(max_length=20, choices=FAT_CONTENT_CHOICES)
    Item_Visibility = models.FloatField()
    Item_Type = models.CharField(max_length=50)
    Item_MRP = models.FloatField()
    Outlet_Identifier = models.CharField(max_length=50)
    Outlet_Establishment_Year = models.IntegerField()
    Outlet_Size = models.CharField(max_length=10, choices=OUTLET_SIZE_CHOICES)
    Outlet_Location_Type = models.CharField(max_length=10, choices=LOCATION_TYPE_CHOICES)
    Outlet_Type = models.CharField(max_length=50, choices=OUTLET_TYPE_CHOICES)
    Item_Outlet_Sales = models.FloatField()

    def __str__(self):
        return self.Item_Identifier

class TrainData(models.Model):
    Item_Identifier = models.CharField(max_length=50)
    Item_Weight = models.FloatField(null=True)
    Item_Fat_Content = models.CharField(max_length=50)
    Item_Visibility = models.FloatField()
    Item_Type = models.CharField(max_length=50)
    Item_MRP = models.FloatField()
    Outlet_Identifier = models.CharField(max_length=50)
    Outlet_Establishment_Year = models.IntegerField()
    Outlet_Size = models.CharField(max_length=20, null=True)
    Outlet_Location_Type = models.CharField(max_length=20)
    Outlet_Type = models.CharField(max_length=50)
    Item_Outlet_Sales = models.FloatField()

    def __str__(self):
        return self.Item_Identifier
