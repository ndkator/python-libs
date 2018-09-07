from basetest.models import Library, Comments
from basetest.models import Module, Creator
from basetest.models import Task
from django.views.generic.list import ListView
from django.views.generic.list import View
from django.db.models import Q
from django.shortcuts import render, redirect
from basetest.forms import CommentForm
from datetime import datetime
from datetime import date

# Определяет функции, которые получают запросы пользователей, обрабатывает их и возвращает ответ

# ВСЁ, ЧТО СВЯЗАНО С БИБЛИОТЕКАМИ:
class LibraryListView(ListView):    # Выводит ListView при переходе на /libs/
    model = Library
    queryset = Library.objects.all()
    template_name = "basetest/libraout.html"
    paginate_by = 5


def liblocal(request, pk):          # Генерирует страницу отдельной библиотеки; Добавляет раздел с комментариями
    libra = Library.objects.filter(id=pk) # Формирует добавление нового комментария в БД
    comma = Comments.objects.filter(LibraryID=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.UserID = request.user
            form.LibraryID_id = pk
            form.save()
            return redirect(liblocal, pk)
    else:
        form = CommentForm()
    return render(request, "basetest/libraread.html", {"libra": libra,
                                                   "comma": comma,
                                                   "form": form})

class LibfilterListView(ListView):      # Фильтр "Отсортировать по имени"
    model=Library
    queryset=Library.objects.all().order_by('Name')
    template_name = "basetest/filter/libname.html"
    paginate_by = 5

class LibfilterListViewZ(ListView):      # REVERSE-Фильтр "Отсортировать по имени"
    model=Library
    queryset=Library.objects.all().order_by('-Name')
    template_name = "basetest/filter/libreversename.html"
    paginate_by = 5

class Py2filterListView(ListView):      # Фильтр "Python 2"
    model=Library
    queryset=Library.objects.all().filter(PythonVersion=2)
    template_name = "basetest/filter/libpy2.html"
    paginate_by = 5

class Py3filterListView(ListView):      # Фильтр "Python 3"
    model=Library
    queryset=Library.objects.all().filter(PythonVersion=3)
    template_name = "basetest/filter/libpy3.html"
    paginate_by = 5


# ВСЁ, ЧТО СВЯЗАНО С МОДУЛЯМИ:
class ModuleListView(ListView):             # Выводит ListView при переходе на /modules/
    model = Module
    queryset = Module.objects.all()
    template_name = "basetest/moduleout.html"
    paginate_by = 5

def modulelocal(request, pk):               # Генерирует страницу отдельного модуля
    mod = Module.objects.filter(id=pk)
    mytask = Task.objects.filter(module__id=pk)
    return render(request, "basetest/moduleread.html", {"mod" : mod,
                                                        "mytask": mytask})

class ModulefilterListView(ListView):      # Фильтр "Отсортировать по имени"
    model=Module
    queryset=Module.objects.all().order_by('Name')
    template_name = "basetest/filter/modname.html"
    paginate_by = 5

class ModulefilterListViewZ(ListView):      # REVERSE-Фильтр "Отсортировать по имени"
    model=Module
    queryset=Module.objects.all().order_by('-Name')
    template_name = "basetest/filter/modreversename.html"
    paginate_by = 5

class ModuleLibIDfilterListView(ListView):  # Фильтр "Отсортировать по Library ID"
    model=Module
    queryset=Module.objects.all().order_by('LibraryID')
    template_name = "basetest/filter/modlibsid.html"
    paginate_by = 5

class ModuleLibIDfilterListViewZ(ListView):  # REVERSE-Фильтр "Отсортировать по Library ID"
    model=Module
    queryset=Module.objects.all().order_by('-LibraryID')
    template_name = "basetest/filter/modreverselibsid.html"
    paginate_by = 5


# ВСЁ, ЧТО СВЯЗАНО С СОЗДАТЕЛЯМИ:
class CreatorListView(ListView):            # Выводит ListView при переходе на /creators/
    model = Creator
    queryset =  Creator.objects.all()
    template_name = "basetest/createout.html"
    paginate_by = 5

def creatorlocal(request, pk):              # Генерирует страницу отдельного создателя
    create = Creator.objects.filter(id=pk)
    mylib = Library.objects.filter(CreatorID=pk)
    return render(request, "basetest/createread.html", {"create": create,
                                                        "mylib": mylib})

class CreatorfilterListView(ListView):      # Фильтр "Отсортировать по имени"
    model=Creator
    queryset=Creator.objects.all().order_by('Name')
    template_name = "basetest/filter/createname.html"
    paginate_by = 5

class CreatorfilterListViewZ(ListView):      # REVERSE-Фильтр "Отсортировать по имени"
    model=Creator
    queryset=Creator.objects.all().order_by('-Name')
    template_name = "basetest/filter/createreversename.html"
    paginate_by = 5

class CreatorCountryfilterListView(ListView):  # Фильтр "Отсортировать по Country"
    model=Creator
    queryset=Creator.objects.all().order_by('Country')
    template_name = "basetest/filter/createcountry.html"
    paginate_by = 5

class CreatorCountryfilterListViewZ(ListView):  # REVERSE-Фильтр "Отсортировать по Country"
    model=Creator
    queryset=Creator.objects.all().order_by('-Country')
    template_name = "basetest/filter/createreversecountry.html"
    paginate_by = 5


# ВСЁ, ЧТО СВЯЗАНО С ЗАДАНИЯМИ:
class TaskListView(ListView):               # Выводит ListView при переходе на /tasks/
    model = Task
    queryset =  Task.objects.all()
    template_name = "basetest/taskout.html"
    paginate_by = 5

def tasklocal(request, pk):
    tas = Task.objects.filter(id=pk)
    mymodule = Module.objects.filter(tasks__id=pk)
    return render(request, "basetest/taskread.html", {"tas": tas,
                                                      "mymodule": mymodule})



class TaskfilterListView(ListView):      # Фильтр "Отсортировать по имени"
    model=Task
    queryset=Task.objects.all().order_by('Class')
    template_name = "basetest/filter/taskname.html"
    paginate_by = 5

class TaskfilterListViewZ(ListView):      # REVERSE-Фильтр "Отсортировать по имени"
    model=Task
    queryset=Task.objects.all().order_by('-Class')
    template_name = "basetest/filter/taskreversename.html"
    paginate_by = 5



# ВЬЮШКИ ДЛЯ ПОИСКА
####################### БИБЛИОТЕКИ #############################

class SearchView(View):
    template_name = "basetest/filter/BigLibSearch.html"
    def get(self, request, *args, **kwargs):
        SearchTable = request.GET.get('par1')
        PythonTable = request.GET.get('par2')
        query = request.GET.get('q')
        first = request.GET.get('first')
        second = request.GET.get('second')

        if SearchTable == 'Names':
            if PythonTable == 'All':
                if first and second:
                    pre_founded_libs = Library.objects.filter(ReleaseDate__range=
                                                              [first,second])
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    founded_libs = Library.objects.filter(
                        Q(Name__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py2':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                                  [first,second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Name__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py3':
                if first and second:
                     pre_founded_libs = Library.objects.filter(PythonVersion=3)
                     pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                                  [first,second])
                     founded_libs = pro_founded_libs.filter(
                         Q(Name__icontains=query))
                     context = {'founded_libs': founded_libs}
                     return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

        elif SearchTable == 'Desc':
            if PythonTable == 'All':
                if first and second:
                    pre_founded_libs = Library.objects.filter(ReleaseDate__range=
                                                              [first, second])
                    founded_libs = pre_founded_libs.filter(
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    founded_libs = Library.objects.filter(
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py2':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    founded_libs = pre_founded_libs.filter(
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py3':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    founded_libs = pre_founded_libs.filter(
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

        elif SearchTable == 'NamesAndDesc':
            if PythonTable == 'All':
                if first and second:
                    pre_founded_libs = Library.objects.filter(ReleaseDate__range=
                                                              [first, second])
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    founded_libs = Library.objects.filter(
                        Q(Name__icontains=query) |
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py2':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py3':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(Description__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

        elif SearchTable == 'Creator':
            if PythonTable == 'All':
                if first and second:
                    pre_founded_libs = Library.objects.filter(ReleaseDate__range=
                                                              [first, second])
                    founded_libs = pre_founded_libs.filter(
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    founded_libs = Library.objects.filter(
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            if PythonTable == 'Py2':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    founded_libs = pre_founded_libs.filter(
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            if PythonTable == 'Py3':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    founded_libs = pre_founded_libs.filter(
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

        else:
            if PythonTable == 'All':
                if first and second:
                    pre_founded_libs = Library.objects.filter(ReleaseDate__range=
                                                              [first, second])
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(ReleaseDate__icontains=query) |
                        Q(LibVersion__icontains=query) |
                        Q(Description__icontains=query) |
                        Q(Documentation__icontains=query) |
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    founded_libs = Library.objects.filter(
                        Q(Name__icontains=query) |
                        Q(ReleaseDate__icontains=query) |
                        Q(LibVersion__icontains=query) |
                        Q(Description__icontains=query) |
                        Q(Documentation__icontains=query) |
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py2':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(ReleaseDate__icontains=query) |
                        Q(LibVersion__icontains=query) |
                        Q(Description__icontains=query) |
                        Q(Documentation__icontains=query) |
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=2)
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(ReleaseDate__icontains=query) |
                        Q(LibVersion__icontains=query) |
                        Q(Description__icontains=query) |
                        Q(Documentation__icontains=query) |
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)

            elif PythonTable == 'Py3':
                if first and second:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    pro_founded_libs = pre_founded_libs.filter(ReleaseDate__range=
                                                               [first, second])
                    founded_libs = pro_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(ReleaseDate__icontains=query) |
                        Q(LibVersion__icontains=query) |
                        Q(Description__icontains=query) |
                        Q(Documentation__icontains=query) |
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)
                else:
                    pre_founded_libs = Library.objects.filter(PythonVersion=3)
                    founded_libs = pre_founded_libs.filter(
                        Q(Name__icontains=query) |
                        Q(ReleaseDate__icontains=query) |
                        Q(LibVersion__icontains=query) |
                        Q(Description__icontains=query) |
                        Q(Documentation__icontains=query) |
                        Q(CreatorID__Name__icontains=query) |
                        Q(CreatorID__Country__icontains=query))
                    context = {'founded_libs': founded_libs}
                    return render(self.request, self.template_name, context)


class SearchTrue(View):
    template_name = "basetest/filter/TrueSearch.html"
    def get(self, request, *args, **kwargs):
        SearchTable = request.GET.get('par1')
        HowSearch = request.GET.get('par2')
        query = request.GET.get('q')
        if SearchTable == 'Library':
            if HowSearch == 'All':
                founded_libs = Library.objects.filter(
                    Q(Name__icontains=query) |
                    Q(ReleaseDate__icontains=query) |
                    Q(LibVersion__icontains=query) |
                    Q(Description__icontains=query) |
                    Q(Documentation__icontains=query))
                context = {'founded_libs': founded_libs}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Name':
                founded_libs = Library.objects.filter(
                    Q(Name__icontains=query))
                context = {'founded_libs': founded_libs}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Desc':
                founded_libs = Library.objects.filter(
                    Q(Description__icontains=query))
                context = {'founded_libs': founded_libs}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'NameAndDesc':
                founded_libs = Library.objects.filter(
                    Q(Name__icontains=query) |
                    Q(Description__icontains=query))
                context = {'founded_libs': founded_libs}
                return render(self.request, self.template_name, context)
            else:
                founded_libs = Library.objects.filter(
                    Q(CreatorID__Country__icontains=query))
                context = {'founded_libs': founded_libs}
                return render(self.request, self.template_name, context)

        elif SearchTable == 'Module':
            if HowSearch == 'All' or HowSearch == 'NameAndDesc':
                founded_mods = Module.objects.filter(
                    Q(Name__icontains=query) |
                    Q(Description__icontains=query))
                context = {'founded_mods': founded_mods}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Name':
                founded_mods = Module.objects.filter(
                    Q(Name__icontains=query))
                context = {'founded_mods': founded_mods}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Desc':
                founded_mods = Module.objects.filter(
                    Q(Description__icontains=query))
                context = {'founded_mods': founded_mods}
                return render(self.request, self.template_name, context)
            else:
                founded_mods = Module.objects.filter(
                    Q(LibraryID__CreatorID__Country__icontains=query))
                context = {'founded_mods': founded_mods}
                return render(self.request, self.template_name, context)

        elif SearchTable == 'Creator':
            if HowSearch == 'All':
                founded_create = Creator.objects.filter(
                    Q(Name__icontains=query) |
                    Q(Website__icontains=query) |
                    Q(Country__icontains=query))
                context = {'founded_create': founded_create}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Name':
                founded_create = Creator.objects.filter(
                    Q(Name__icontains=query))
                context = {'founded_create': founded_create}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Country':
                founded_create = Creator.objects.filter(
                    Q(Country__icontains=query))
                context = {'founded_create': founded_create}
                return render(self.request, self.template_name, context)
            else:
                pass

        else:
            if HowSearch == 'All' or HowSearch == 'NameAndDesc':
                founded_task = Task.objects.filter(
                    Q(Class__icontains=query)|
                    Q(TaskText__icontains=query))
                context = {'founded_task' : founded_task}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Name':
                founded_task = Task.objects.filter(
                    Q(Class__icontains=query))
                context = {'founded_task': founded_task}
                return render(self.request, self.template_name, context)
            elif HowSearch == 'Desc':
                founded_task = Task.objects.filter(
                    Q(TaskText__icontains=query))
                context = {'founded_task': founded_task}
                return render(self.request, self.template_name, context)
            else:
                pass


class SearchViewPy2(View):                      # Поиск по разделу "Python 2" в таблице БИБЛИОТЕКИ
    template_name = "basetest/filter/libsearch.html"
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        pre_founded_libs = Library.objects.filter(PythonVersion=2)
        founded_libs = pre_founded_libs.filter(
            Q(Name__icontains=query))
        context = {'founded_libs' : founded_libs}
        return render(self.request, self.template_name, context)

class SearchViewPy3(View):                      # Поиск по разделу "Python 3" в таблице БИБЛИОТЕКИ
    template_name = "basetest/filter/libsearch.html"
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        pre_founded_libs = Library.objects.filter(PythonVersion=3)
        founded_libs = pre_founded_libs.filter(
            Q(Name__icontains=query))
        context = {'founded_libs' : founded_libs}
        return render(self.request, self.template_name, context)

####################### МОДУЛИ #############################
class ModuleSearchView(View):                         # Поиск по всем аргументам в таблице МОДУЛИ
    template_name = "basetest/filter/modsearch.html"
    def get(self, request, *args, **kwargs):
        SearchTable = request.GET.get('par1')
        query = request.GET.get('q')
        if SearchTable == 'NamesAndDesc':
            founded_mods = Module.objects.filter(
                Q(Name__icontains=query)|
                Q(Description__icontains=query))
            context = {'founded_mods' : founded_mods}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Names':
            founded_mods = Module.objects.filter(
                Q(Name__icontains=query))
            context = {'founded_mods': founded_mods}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Desc':
            founded_mods = Module.objects.filter(
                Q(Description__icontains=query))
            context = {'founded_mods': founded_mods}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Libs':
            founded_mods = Module.objects.filter(
                Q(LibraryID__Name__icontains=query))
            context = {'founded_mods': founded_mods}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Tasks':
            founded_mods = Module.objects.filter(
                Q(tasks__Class__icontains=query))
            context = {'founded_mods': founded_mods}
            return render(self.request, self.template_name, context)


####################### СОЗДАТЕЛИ #############################
class CreatorSearchView(View):                         # Поиск по всем аргументам в таблице СОЗДАТЕЛИ
    template_name = "basetest/filter/createsearch.html"
    def get(self, request, *args, **kwargs):
        SearchTable = request.GET.get('par1')
        query = request.GET.get('q')
        if SearchTable == 'All':
            founded_create = Creator.objects.filter(
                Q(Name__icontains=query)|
                Q(Website__icontains=query)|
                Q(Country__icontains=query))
            context = {'founded_create' : founded_create}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Names':
            founded_create = Creator.objects.filter(
                Q(Name__icontains=query))
            context = {'founded_create': founded_create}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Country':
            founded_create = Creator.objects.filter(
                Q(Country__icontains=query))
            context = {'founded_create': founded_create}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Site':
            founded_create = Creator.objects.filter(
                Q(Website__icontains=query))
            context = {'founded_create': founded_create}
            return render(self.request, self.template_name, context)


####################### ЗАДАЧИ #############################
class TaskSearchView(View):                         # Поиск по всем аргументам в таблице ЗАДАЧИ
    template_name = "basetest/filter/tasksearch.html"
    def get(self, request, *args, **kwargs):
        SearchTable = request.GET.get('par1')
        query = request.GET.get('q')
        if SearchTable == 'All':
            founded_task = Task.objects.filter(
                Q(Class__icontains=query)|
                Q(TaskText__icontains=query))
            context = {'founded_task' : founded_task}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Abbrev':
            founded_task = Task.objects.filter(
                Q(Class__icontains=query))
            context = {'founded_task' : founded_task}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Desc':
            founded_task = Task.objects.filter(
                Q(TaskText__icontains=query))
            context = {'founded_task' : founded_task}
            return render(self.request, self.template_name, context)
        elif SearchTable == 'Mod':
            founded_task = Task.objects.filter(
                Q(module__Name__icontains=query))
            context = {'founded_task' : founded_task}
            return render(self.request, self.template_name, context)