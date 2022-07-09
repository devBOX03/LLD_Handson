class Operator(object):
    def __init__(self, name: str, email: str, phone: str):
        self._name = name
        self._email = email
        self._phone = phone

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone
