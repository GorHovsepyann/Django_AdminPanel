from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField('category tesaky',max_length=250)
    img = models.ImageField('category nkary',upload_to='Uteliqner/')
    
    def __str__(self) -> str:
        return self.name
    
class subcategory(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,related_name='sub_cat')
    name = models.CharField('subcategory anuny',max_length=250)
    img = models.ImageField('subcategory nkary',upload_to='Uteliqner/')