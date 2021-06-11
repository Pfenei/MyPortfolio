from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    date = models.DateField()
    mainframework = models.CharField(max_length=200)
    subframework = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=200)
    is_schoolproject = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Technology(models.Model):
    iconurl = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Framework(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='frameworks')
    frameworkname = models.CharField(max_length=200)
    frameworkurl = models.CharField(max_length=200)

    def __str__(self):
        return self.frameworkname


class Study(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Course(models.Model):
    platform = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    completionDate = models.DateField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
