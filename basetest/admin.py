from django.contrib import admin
from basetest.models import Creator
from basetest.models import Library
from basetest.models import Module
from basetest.models import Comments
from basetest.models import Task

# Предназначен для административных функций, в частности, здесь призводится регистрация
# моделей, которые используются в интерфейсе администратора


# Выдача библиотек, над которыми работал Создатель
class CreatorInLine(admin.StackedInline):
    model = Library
    fields = ["Name"]
    extra = 0

# Выдача комментариев к разделу с библиотеками
class LibraryInLine(admin.StackedInline):
    model = Comments
    extra = 0

# Ниже - свойства выдачи информации (сортировка + поиск по опредеделённым полям в каждом из разделов)

class LibraryAdmin(admin.ModelAdmin):
    inlines = [LibraryInLine]
    list_display = ["Name", "ReleaseDate", "PythonVersion", "CreatorID"]
    list_display_links = ["Name", "CreatorID"]
    list_filter = ["PythonVersion"]
    search_fields = ["Name", "PythonVersion",
                     "ReleaseDate", "Description"]

class CreatorAdmin(admin.ModelAdmin):
    inlines = [CreatorInLine]
    list_display = ["Name", "Country"]
    list_filter = ["Country"]
    search_fields = ["Name", "Country", "Website"]

class ModuleAdmin(admin.ModelAdmin):
    list_display = ["Name", "LibraryID", "Description"]
    list_filter = ["tasks__Class"]
    search_fields = ["Name", "Description"]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["Class", "TaskText"]
    list_filter = ["module__Name"]
    search_fields = ["Class", "TaskText"]

class CommentsAdmin(admin.ModelAdmin):
    list_display = ["UserID", "LibraryID", "CommentsText", "AddDate"]
    list_display_links = ["UserID", "CommentsText"]
    list_filter = ["UserID"]
    search_fields = ["CommentsText", "AddDate"]

# Регистрация моделей в админке + их свойства
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Task, TaskAdmin)
