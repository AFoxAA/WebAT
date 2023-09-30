class DirectoryNameError(Exception):
    def __init__(self):
        self.message = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                        'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')

    def __str__(self):
        return self.message


class SiteAccessError(Exception):
    def __init__(self, base_url):
        self.base_url = base_url
        self.message = f'Не удается получить доступ к сайту {self.base_url}.Пожалуйста, убедитесь в корректности URL.'

    def __str__(self):
        return self.message


class LocatorError(Exception):
    def __init__(self, locator, time):
        self.locator = locator
        self.time = time
        self.message = f'Элемент с локатором {self.locator} не найден после ожидания {self.time} секунд'

    def __str__(self):
        return self.message


class ErrorWhenSavingScreenshot(Exception):
    def __init__(self):
        self.message = ('Ошибка при сохранении скриншота. '
                        'В файле ".yaml" отсутствует значение для директории сохранения скриншотов.')

    def __str__(self):
        return self.message
