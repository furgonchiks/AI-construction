import doctest
class Vehicle:
    """
    Класс, представляющий транспортное средство.
    """
    def __init__(self, brand: str, max_speed_kmh: float, fuel_capacity_l: float):
        """
        Создание и подготовка к работе объекта "Транспортное средство"
        :param brand: Марка транспортного средства
        :param max_speed_kmh: Максимальная скорость в км/ч
        :param fuel_capacity_l: Вместимость топливного бака в литрах
        Примеры:
        >>> vehicle = Vehicle("Toyota", 200.0, 50.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not brand:
            raise ValueError("Марка не может быть пустой строкой")
        self.brand = brand

        if not isinstance(max_speed_kmh, (int, float)):
            raise TypeError("Максимальная скорость должна быть int или float")
        if max_speed_kmh <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed_kmh = max_speed_kmh

        if not isinstance(fuel_capacity_l, (int, float)):
            raise TypeError("Вместимость бака должна быть int или float")
        if fuel_capacity_l <= 0:
            raise ValueError("Вместимость бака должна быть положительным числом")
        self.fuel_capacity_l = fuel_capacity_l

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.
        :return: Сообщение о запуске двигателя
        Примеры:
        >>> vehicle = Vehicle("Toyota", 200.0, 50.0)
        >>> vehicle.start_engine()
        """

    def refuel(self, amount_l: float) -> None:
        """
        Заправляет транспортное средство.
        :param amount_l: Количество топлива в литрах
        Примеры:
        >>> vehicle = Vehicle("Toyota", 200.0, 50.0)
        >>> vehicle.refuel(30.0)
        """
    def get_estimated_range(self, fuel_consumption_l_per_100km: float) -> float:
        """
        Рассчитывает примерный запас хода.
        :param fuel_consumption_l_per_100km: Расход топлива на 100 км
        :return: Запас хода в километрах
        Примеры:
        >>> vehicle = Vehicle("Toyota", 200.0, 50.0)
        >>> vehicle.get_estimated_range(5.0)
        """
class Book:
    """
    Класс, представляющий книгу.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param title: Название книги
        :param author: Автор книги
        :param page_count: Количество страниц
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not title:
            raise ValueError("Название не может быть пустой строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not author:
            raise ValueError("Автор не может быть пустой строкой")
        self.author = author

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.page_count = page_count

    def open(self, page_number: int = 1) -> str:
        """
        Открывает книгу на указанной странице.
        :param page_number: Номер страницы
        :return: Сообщение об открытии книги
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.open(50)
        """
    def get_genre(self) -> str:
        """
        Возвращает жанр книги.
        :return: Жанр книги
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_genre()
        """
    def get_chapter_titles(self) -> list:
        """
        Возвращает список названий глав.
        :return: Список названий глав
        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_chapter_titles()
        """

class SocialMediaAccount:
    """
    Класс, представляющий аккаунт в социальной сети.
    """
    def __init__(self, username: str, email: str, join_date: str):
        """
        Создание и подготовка к работе объекта "Аккаунт в социальной сети"
        :param username: Имя пользователя
        :param email: Адрес электронной почты
        :param join_date: Дата регистрации
        Примеры:
        >>> account = SocialMediaAccount("john_doe", "john@example.com", "2023-01-15")
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not username:
            raise ValueError("Имя пользователя не может быть пустой строкой")
        self.username = username

        if not isinstance(email, str):
            raise TypeError("Email должен быть строкой")
        if not email or '@' not in email:
            raise ValueError("Email должен быть валидным адресом")
        self.email = email

        if not isinstance(join_date, str):
            raise TypeError("Дата регистрации должна быть строкой")
        self.join_date = join_date

    def post(self, content: str) -> str:
        """
        Публикует контент в социальной сети.
        :param content: Текст публикации
        :return: Идентификатор публикации
        Примеры:
        >>> account = SocialMediaAccount("john_doe", "john@example.com", "2023-01-15")
        >>> account.post("Hello, world!")
        """
    def add_friend(self, username: str) -> str:
        """
        Отправляет запрос на добавление в друзья.
        :param username: Имя пользователя для добавления
        :return: Сообщение о результате запроса
        Примеры:
        >>> account = SocialMediaAccount("john_doe", "john@example.com", "2023-01-15")
        >>> account.add_friend("jane_doe")
        """
    def get_friends_count(self) -> int:
        """
        Возвращает количество друзей.
        :return: Количество друзей
        Примеры:
        >>> account = SocialMediaAccount("john_doe", "john@example.com", "2023-01-15")
        >>> account.get_friends_count()
        """

if __name__ == "__main__":
    doctest.testmod()