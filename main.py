import DocString_EpYtext
import DocString_google
import DocString_reST
import DocString_SciPy


def print_hi(name):
    print(f'Hi, {name}')


def call_functions_add_numbers():
    print(DocString_EpYtext.add_numbers(1, 2))
    print(DocString_google.add_numbers(3, 4))
    print(DocString_reST.add_numbers(5, 6))
    print(DocString_SciPy.add_numbers(7, 8))


if __name__ == '__main__':
    print_hi('PyCharm')
    call_functions_add_numbers()
