from django.db import models


# การจะส่งออกเครื่องปรับอากาศไปขายยังประเทศต่างๆได้นั้น จำเป็น
# ในแต่ละประเทศจะมีการกำหนดให้มีการ
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ItemTest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specification(models.Model):
    item_test = models.ForeignKey(ItemTest, on_delete=models.CASCADE, related_name='specifications')
    description = models.TextField(max_length=700 , default= "xxxxxxx")
    TYPE_CHOICES = [
        ('S', 'Sampling test'),
        ('R', 'Routine test'),
    ]
    test_type = models.CharField(max_length=1, choices=TYPE_CHOICES , default='R')

    def __str__(self):
        return f"{self.item_test.name} - {self.description} ({self.get_test_type_display()})"


class CountryTestRequirement(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    REQUIREMENT_CHOICES = [
        ('-', 'No requirement'),
        ('1', 'Should be tested (If possible)'),
        ('2', 'Std.requirement (Must be tested)'),
        ('3', 'Std.requirement must be tested at external lab (CCC)'),
        ('4', 'Std.requirement which can select testing (Between Pressure and Refri. leakage test) (QCO)'),
    ]
    requirement = models.CharField(max_length=1, choices=REQUIREMENT_CHOICES)

    class Meta:
        unique_together = ('country', 'specification')

    def __str__(self):  
        return f"{self.country.name} - {self.specification.description} ({self.get_requirement_display()})"

    