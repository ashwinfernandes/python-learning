def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'The ID of `greeting`in `greet_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(1): {locals()}')

    def make_greeting(item: str) -> str:
        print(f'local namespace in `make_greeting`(1): {locals()}')
        greeting = 'Hola'
        print(f'The ID of `greeting`in `make_greeting` is {id(greeting)}')
        print(f'local namespace in `make_greeting`(2): {locals()}')
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside green_pythons, `greeting` is {greeting}')
    print(f'The ID of `greeting`in `greet_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(2): {locals()}')


names = ['John']#, 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
