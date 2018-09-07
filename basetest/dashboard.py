from basetest.models import Creator, Library, Module, Comments
from controlcenter import Dashboard, widgets
from django.db.models import Count

class CreatorSingleBarChart(widgets.SingleBarChart):
    # Строит бар-чарт по числу создателей
    title = 'Топ стран по числу живущих в них создателей библиотек Python'
    model = Creator
    width = widgets.LARGE
    limit_to = 10

    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            # float как промежуточные значения, это ни к чему
            'onlyInteger': True,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series

    def values(self):
        queryset = self.get_queryset()
        return (queryset.values_list('Country')
                        .annotate(baked=Count('Country'))
                        .order_by('-baked')[:self.limit_to])

class LibrarySinglePieChart(widgets.SinglePieChart):
    # Строит бар-чарт по числу библиотек для разных версих Py
    title = 'Количество находящихся на сайте библиотек (Py3 / Py2)'
    model = Library
    width = widgets.MEDIUM
    limit_to = 10

    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            # float как промежуточные значения, это ни к чему
            'onlyInteger': True,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series

    def values(self):
        queryset = self.get_queryset()
        return (queryset.values_list('PythonVersion')
                        .annotate(baked=Count('PythonVersion'))
                        .order_by('-baked')[:self.limit_to])

class LibrarySingleBarChart(widgets.SingleBarChart):
    # Строит бар-чарт по числу созданных библиотек
    title = 'Топ авторов библиотек'
    model = Library
    width = widgets.MEDIUM
    limit_to = 5

    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            # float как промежуточные значения, это ни к чему
            'onlyInteger': True,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series#RESTAURANTS

    def values(self):
        queryset = self.get_queryset()
        return (queryset.values_list('CreatorID__Name')
                        .annotate(baked=Count('CreatorID'))
                        .order_by('-baked')[:self.limit_to])


class ModuleSingleBarChart(widgets.SingleBarChart):
    # Строит бар-чарт по числу созданных библиотек
    title = 'Количество модулей, входящих в библиотеки'
    model = Module
    width = widgets.LARGE
    limit_to = 10

    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            # float как промежуточные значения, это ни к чему
            'onlyInteger': True,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series

    def values(self):
        queryset = self.get_queryset()
        return (queryset.values_list('LibraryID__Name')
                        .annotate(baked=Count('LibraryID'))
                        .order_by('-baked')[:self.limit_to])

class CommentsSingleBarChart(widgets.SingleBarChart):
    # Строит бар-чарт по числу комментариев
    title = 'Топ комментаторов'
    model = Comments
    width = widgets.MEDIUM
    limit_to = 3

    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            # float как промежуточные значения, это ни к чему
            'onlyInteger': True,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series

    def values(self):
        queryset = self.get_queryset()
        return (queryset.values_list('UserID__username')
                        .annotate(baked=Count('UserID'))
                        .order_by('-baked')[:self.limit_to])


class MyDashboard(Dashboard):
    widgets = (
        CreatorSingleBarChart,
        LibrarySinglePieChart,
        LibrarySingleBarChart,
        ModuleSingleBarChart,
        CommentsSingleBarChart
    )
