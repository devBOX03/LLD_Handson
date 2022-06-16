class User(object):
    def __init__(self):
        self._username: str = None
        self._email: str = None
        self._photo: str = None

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        self._username = username

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def photo(self) -> str:
        return self._photo

    @photo.setter
    def photo(self, photo: str) -> None:
        self._photo = photo
