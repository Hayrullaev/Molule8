class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.__model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    @property
    def model(self):
        return self.__model

    @property
    def vin(self):
        return self.__vin

    @property
    def numbers(self):
        return self.__numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("VIN-номер вне допустимого диапазона")
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Номера должны состоять из 6 символов")
        else:
            return True



try:
    first = Car('BMV', 1000000, 'e749xo790')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 6780986, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 385685602, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')