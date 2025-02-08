from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام کامل')
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True,blank=True, verbose_name='عکس پروفایل')
    bio = models.TextField(verbose_name='درباره من')
    email = models.EmailField(null=True,blank=True, verbose_name='ایمیل')
    linkedin = models.URLField(null=True,blank=True, verbose_name='لینکدین')
    github = models.URLField(null=True,blank=True, verbose_name='گیت هاب')

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,verbose_name='پروفایل')
    name = models.CharField(max_length=100, verbose_name='نام مهارت')
    level = models.IntegerField(verbose_name='سطح مهارت')

    def __str__(self):
        return f"{self.name} - {self.level}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='پروفایل')
    company_name = models.CharField(max_length=100, verbose_name='نام شرکت')
    job_title = models.CharField(max_length=100, verbose_name='عنوان شغلی')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان(در صورتی که پایان نداشته باشد خالی بگذارید)')
    description = models.TextField(verbose_name='توضیحات')


    def __str__(self):
        return f"{self.job_title} - {self.company_name}"

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='پروفایل')
    title = models.CharField(max_length=100, verbose_name='عنوان پروژه')
    description = models.TextField(verbose_name='توضیحات')
    github_link = models.URLField(blank=True,null=True,verbose_name=' لینک گیت هاب')
    link = models.URLField(null=True,blank=True, verbose_name='لینک پروژه')

    def __str__(self):
        return self.title

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='پروفایل')
    institution_name = models.CharField(max_length=255, verbose_name='نام موسسه')
    degree = models.CharField(max_length=255, verbose_name='مقطع تحصیلی')
    start_year = models.IntegerField(verbose_name='سال شروع')
    end_year = models.IntegerField(null=True, blank=True, verbose_name='سال پایان(در صورتی که پایان نداشته باشد خالی بگذارید)')


    def __str__(self):
        return f"{self.degree} - {self.institution_name}"

