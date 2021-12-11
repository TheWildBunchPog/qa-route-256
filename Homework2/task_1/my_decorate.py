permitted_role = ['admin']


def check_access(role):
    def real_decorator(function):
        def wrapped():
            if role == 'admin':
                return function()
            elif role == 'user':
                raise PermissionError('Access denied for user "user"')

        return wrapped

    return real_decorator


@check_access('admin')
def user_login():
    return "Добро пожаловать!"


print(user_login())


# Результат работы: Добро пожаловать!


@check_access('user')
def user_login():
    return "Добро пожаловать!"


print(user_login())
# Результат работы: PermissionError: Access denied for user "user"
