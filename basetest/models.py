from django.db import models
from django.contrib.auth.models import User


# Хранит определение моделей, которые описывают используемые в приложении данные

class Creator(models.Model):
    Name = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Website = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.Name

class Library(models.Model):
    Py2 = 2
    Py3 = 3
    CreatorID = models.ForeignKey(Creator, on_delete=models.SET_DEFAULT, default=87)
    Name = models.CharField(max_length=255, unique=True)
    ReleaseDate = models.DateField()
    LibVersion = models.CharField(max_length=255)
    PythonVersion = models.IntegerField(choices=((Py2, 'python 2'),
                                                 (Py3, 'python 3')))
    Description = models.TextField(unique=True)
    Documentation = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class Comments(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=25) # При удалении передаёт id User to DeleteUserId
    CommentsText = models.TextField("Комментарий")
    LibraryID = models.ForeignKey(Library, on_delete=models.CASCADE, default=0) # Ссылка на библиотеку
    AddDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CommentsText

class Task(models.Model):
    Class = models.CharField(max_length=30)
    TaskText = models.CharField(max_length=250)

    def __str__(self):
        return self.Class

class Module(models.Model):
    LibraryID = models.ForeignKey(Library, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField()
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.Name

# Таблица-кодификатор TaskSolving создана автоматически, после добавления поля tasks в Module и исполнения миграций