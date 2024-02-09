class UserModel:
    id: int = 0

    def __init__(self, _id, *args, **kwargs):
        self.id = _id
        super().__init__(*args, **kwargs)


class AccountModel:
    id: int = 0

    def __init__(self, _id, *args, **kwargs):
        self.id = _id
        super().__init__(*args, **kwargs)
