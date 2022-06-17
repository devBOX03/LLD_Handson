class User(object):
    def __init__(self, username: str, email: str, photo: str):
        self._username: str = username
        self._email: str = email
        self._photo: str = photo

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def photo(self) -> str:
        return self._photo
