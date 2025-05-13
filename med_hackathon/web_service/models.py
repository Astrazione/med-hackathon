from django.db import models

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100,
                                    blank=False,
                                    null=False)
    def __str__(self):
        return f'Дисциплина {self.subject_id}: {self.subject_name[:50]}'

class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=100,
                                    blank=False,
                                    null=False)
    subject = models.ForeignKey(Subject,
                                on_delete=models.SET_NULL,
                                related_name="subjects",
                                verbose_name='Дисциплина',
                                blank=True,
                                null=True)

class Theme(models.Model):
    theme_id = models.AutoField(primary_key=True)
    theme_name = models.CharField(max_length=100,
                                  blank=True,
                                  null=True)
    theme_information = models.TextField()
    chapter = models.ForeignKey(Chapter,
                                  on_delete=models.SET_NULL,
                                  related_name='themes',
                                  verbose_name='Глава',
                                  null=True,
                                  blank=True
                                  )