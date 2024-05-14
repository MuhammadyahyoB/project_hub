from django.db import models

# >>>>>> head <<< 
class Head(models.Model):
    """head model"""
    logo = models.ImageField(upload_to='logo')
    img = models.ImageField(upload_to='banners/')
    description = models.TextField()


# >>>>>>>>> portfolio <<< 
class Portfolio(models.Model):
    """portfolio model"""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True,null=True)


# >>>>>>>>> team <<<
class Team(models.Model):
    """team model"""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    major = models.CharField(max_length=255)


# >>>>>>>>>> message  <<<
class Message(models.Model):
    """ Massage model """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=False)


# >>>>>>>>> Resume <<<<
class Resume(models.Model):
    """ Resume model """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cv = models.FileField(upload_to='cv')
    is_active = models.BooleanField(default=False)


# >>>>>>>> vakansiya <<<<< 
class Vakansiya(models.Model):
    """ Vakansiya model"""
    name = models.CharField(max_length=255)
    work_day = models.CharField(max_length=1)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    task = models.TextField()
    technology = models.CharField(max_length=255)