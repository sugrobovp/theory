def permission_required(permission):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if self.has_permission(permission):
                result = func(self, *args, **kwargs)
                return result
            raise Exception(f'Пользователь {self.username} не имеет прав')
        return wrapper
    return decorator


class User:

    def __init__(self, username: str, permissions: list):
        self.username = username
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions

    @permission_required("read")
    def read_data(self):
        print("Чтение данных")

    @permission_required("write")
    def write_data(self):
        print("Запись данных")

    @permission_required("delete")
    def delete_data(self):
        print("Удаление данных")


user_permissions = ["read", "write"]

user = User(username='Peter', permissions=user_permissions)

user.write_data()
