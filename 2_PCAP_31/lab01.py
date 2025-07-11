# ### ### # # ### ### ### ### ### ###
#   #   # # # #   #     # # # # # # #
# ### ### ### ### ###   # ### ### # #
# #     #   #   # # #   # # #   # # #
# ### ###   # ### ###   # ### ### ###


def f_display_part(num: int, row: int):
    if num == 0:
        match row:
            case 0:
                return '###'
            case 1:
                return '# #'
            case 2:
                return '# #'
            case 3:
                return '# #'
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 1:
        return '  #'
    if num == 2:
        match row:
            case 0:
                return '###'
            case 1:
                return '  #'
            case 2:
                return '###'
            case 3:
                return '#  '
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 3:
        match row:
            case 0:
                return '###'
            case 1:
                return '  #'
            case 2:
                return '###'
            case 3:
                return '  #'
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 4:
        match row:
            case 0:
                return '# #'
            case 1:
                return '# #'
            case 2:
                return '###'
            case 3:
                return '  #'
            case 4:
                return '  #'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 5:
        match row:
            case 0:
                return '###'
            case 1:
                return '#  '
            case 2:
                return '###'
            case 3:
                return '  #'
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 6:
        match row:
            case 0:
                return '###'
            case 1:
                return '#  '
            case 2:
                return '###'
            case 3:
                return '# #'
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 7:
        match row:
            case 0:
                return '###'
            case 1:
                return '  #'
            case 2:
                return '  #'
            case 3:
                return '  #'
            case 4:
                return '  #'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 8:
        match row:
            case 0:
                return '###'
            case 1:
                return '# #'
            case 2:
                return '###'
            case 3:
                return '# #'
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")
    if num == 9:
        match row:
            case 0:
                return '###'
            case 1:
                return '# #'
            case 2:
                return '###'
            case 3:
                return '  #'
            case 4:
                return '###'
            case _:  # ➜ captura cualquier otro int
                raise ValueError(f"Row inválida: {row}")


def main():
    while True:
        input_num = input('Ingrese número (-1 para salir): ')
        if input_num == '-1':
            break
        if not input_num.isdigit():
            print('Debe ingresar un número y debe ser igual o mayor a 0.')
            continue
        for row in range(5):
            full_row = [str(f_display_part(int(num), row))
                        for num in input_num]
            to_print = ' '.join(full_row)
            print(to_print)


if __name__ == '__main__':
    main()
