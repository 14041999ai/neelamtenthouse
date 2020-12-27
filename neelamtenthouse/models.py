from django.db import models

# Create your models here.
class Event(models.Model):
    des = models.CharField(max_length=200)
    pub_date = models.DateTimeField( )
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to= "neelamtenthouse/images",  default="")
    id = models.AutoField
    title = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class faq(models.Model):
    ques_id = models.AutoField
    ques = models.CharField(max_length=100)
    ans = models.CharField(max_length=200)

    def __str__(self):
        return self.ques[0:10] + "..."
