class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

number = 5

while True:

    try:

        i_num = int (input("Entre com um número: "))
        if i_num < number:
            raise ValueTooSmallError#raise dispara o método
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Valor é menor, Tente novamente!")
    except ValueTooLargeError:
        print("Valor é maior, Tente novamente!")
        print()
print("Valor está correto ;)")



