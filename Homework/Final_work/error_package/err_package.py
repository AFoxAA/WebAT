from typing import Any


class DirectoryNameError(Exception):
    def __init__(self) -> None:
        self.message: str = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                             'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')

    def __str__(self) -> str:
        return self.message


class SiteAccessError(Exception):
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url
        self.message: str = f'Не удается получить доступ к сайту {self.base_url}.Пожалуйста, убедитесь в корректности URL.'

    def __str__(self) -> str:
        return self.message


class LocatorError(Exception):
    def __init__(self, locator: Any, time: Any) -> None:
        self.locator: Any = locator
        self.time: Any = time
        self.message: str = f'Элемент с локатором {self.locator} не найден после ожидания {self.time} секунд'

    def __str__(self) -> str:
        return self.message


class ErrorWhenSavingScreenshot(Exception):
    def __init__(self) -> None:
        self.message: str = ('Ошибка при сохранении скриншота. '
                             'В файле ".yaml" отсутствует значение для директории сохранения скриншотов.')

    def __str__(self) -> str:
        return self.message


class AlertError(Exception):
    def __init__(self) -> None:
        self.message: str = 'Произошла ошибка при работе с alert'

    def __str__(self) -> str:
        return self.message

class TextInputError(Exception):
    def __init__(self, locator: Any, word: Any) -> None:
        self.locator: Any = locator
        self.word: Any = word
        self.message: str = f'Ошибка при вводе текста "{word}" в текстовое поле ввода "{locator}"'

    def __str__(self) -> str:
        return self.message
