from src.model.queue import Queue
from src.probability import *
from src.table import show_pn_table
from src.pdf import create_pdf


def main():
    limit = 0
    server = 1

    question = input("(Y) De varios servidores, (N) De un servidor: ").capitalize()

    if question == 'Y':
        server = int(input("Números de servidores: "))

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

    λ = int(input("λ Numero medio de llegada por unidad de tiempo: ")) # 90  10
    µ = int(input("µ Numero medio de paquetes que el servidor es capaz de atender por unidad de tiempo: ")) # 120  12

    queue = Queue(unlimited, λ, µ, server, limit)

    print('\nλ: {}'.format(queue.λ))
    print('µ: {}'.format(queue.µ))
    print('ρ: {}'.format(queue.ρ))
    print('\nPo: {}'.format(get_po(queue)))
    print('Pn: {}'.format(get_pn(queue)))
    print('Ls: {}'.format(get_ls(queue)))
    print('Lq: {}'.format(get_lq(queue)))
    print('Ws: {}'.format(get_ws(queue)))
    print('Wq: {}'.format(get_wq(queue)))

    if unlimited == True:
        print('λ Efec: {}'.format(get_lambda_efec(queue)))
        print('λ perd: {}'.format(get_lambda_perd(queue)))

    array = get_pn_array(queue)
    show_pn_table(array)

    # create_pdf(get_data(queue))
    input("\n precione enter para finalizar")


if __name__ == '__main__':
    main()
    # queue = Queue(True, 100, 30, 4, 120)
    # print(get_lq(queue))
