from src.model.queue import Queue
from src.probability import *
from src.table import show_pn_table


def main():
    limit = 0
    time = 0

    unlimited = input("(Y) con limite, (N) sin limite: ").capitalize()

    match unlimited:
        case 'Y':
            unlimited = True

        case 'N':
            unlimited = False

        case default:
            unlimited = False

    if unlimited == True:
        limit = int(input("Máximo de cliente que puede soportar: ")) # 50

    λ = int(input("Media de llegada de clientes: ")) # 90  10
    µ = int(input("Media de servicio a clientes: ")) # 120  12

    queue = Queue(unlimited, λ, µ, limit)
    # queue = Queue(True, 10, 12, 50)

    print('\nλ: {}'.format(queue.λ))
    print('µ: {}'.format(queue.µ))
    print('ρ: {}'.format(queue.ρ))
    print('\nPo: {}'.format(round(get_po(queue), 3)))
    print('Pn: {}'.format(get_pn(queue)[1]))
    print('Ls: {}'.format(round(get_ls(queue), 3)))
    print('Lq: {}'.format(round(get_lq(queue), 3)))
    print('Ws: {}'.format(round(get_ws(queue), 3)))
    print('Wq: {}'.format(round(get_wq(queue), 3)))

    if unlimited == True:
        print('λ Efec: {}'.format(get_lambda_efec(queue)))
        print('λ perd: {}'.format(get_lambda_perd(queue)))

    array = get_pn(queue)[0]
    show_pn_table(array)

    input("\n precione enter para finalizar")


if __name__ == '__main__':
    main()
