from src.item import Item

class Phone(Item):
    """
    Дочерний класс от Item для представления телефонов в магазине.
    """

    def __init__(self, name: str, price: int or float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item.
        Поля name, price quantity подтягиваются из родительского класса.
        :param number_of_sim: Количество сим-карт.
        """
        if not isinstance(number_of_sim, int) or number_of_sim < 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.number_of_sim = number_of_sim
        super().__init__(name, price, quantity)

    def __repr__(self) -> str:
        """Строковое представление объекта для разработчиков"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """Выводит количество сим-карт"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value):
        if not isinstance(new_value, int) or new_value < 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = new_value