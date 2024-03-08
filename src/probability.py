import json
from src.model.queue import Queue

def get_po(queue): # Probabilidad de que el sistema este ocupado
    ρ = queue.ρ
    limit = queue.limit
    server = queue.server

    if server == 1:
        if queue.unlimited == True:
            if ρ == 1:
                po = 1 / (limit + 1)
            else:
                data1 = 1 - ρ
                pow1 =  pow(ρ, limit + 1)
                data2 = 1 - pow1
                po = data1 / data2
        else:
            po = 1 - queue.ρ

        return po

    else:



def get_pn_array(queue):
    data = []
    stop = True
    totals = 0
    limit = queue.limit
    n = 0
    po = get_po(queue)
    ρ = queue.ρ
    unlimited = queue.unlimited
    server = queue.server

    while stop:

        if server == 1:
            pn = po * pow(ρ, n)
        else:
            pn = get_pn(queue, n)

        totals += pn
        info = {
            'n': n,
            'pn': pn,
            'sum_pn': totals,
        }

        data.append(json.dumps(info))
        n += 1

        if unlimited == True:
            if n > limit:
                stop = False
        else:
            if round(pn, 4) == 0.0000:
                stop = False
        pn = 0

    return data


def get_pn(queue, clientAmount= 0):
    server = queue.server

    if server == 1:
        return len(get_pn_array(queue)) - 1
    else:
        unlimited = queue.unlimited
        ρ = queue.ρ
        λ = queue.λ
        po = get_po(queue)
        pow1 = pow(ρ, clientAmount)

        if unlimited == True:
            if (clientAmount >= 0) and (clientAmount <= server):
                fact = factorial(clientAmount)
                div = pow1 / fact

                return div * po
            else:
                fact = factorial(server)
                res = clientAmount - server
                pow2 = pow(server, res)
                mul = fact * pow2
                div = pow1 / mul

                return div * po
        else:



def get_ls(queue):
    limit = queue.limit
    server = queue.server
    po = get_po(queue)
    ρ = queue.ρ
    unlimited = queue.unlimited

    if server == 1:
        if unlimited == True:
            if ρ != 1:
                data1 = (ρ * (1 - ((limit + 1) * pow(ρ, limit)) + (limit * pow(ρ, limit +1))))
                data2 = ((1 - ρ) * (1 - pow(ρ, limit + 1)))
                return data1 / data2
            else:
                return limit / 2
        else:
            return ρ / po
    else:
        lq = get_lq(queue)
        if unlimited == True:
            lambdaEfec = get_lambda_efec(queue)
            div = lambdaEfec / queue.µ

            return lq + div
        else:
            return lq + ρ


def get_lambda_efec(queue):
    data = json.loads(get_pn_array(queue)[queue.limit])
    if queue.server == 1:
        return queue.λ * (1 - data['pn'])
    else:
        return queue.λ * (1 - get_pn(queue, queue.limit))


def get_lambda_perd(queue):
    return queue.λ - get_lambda_efec(queue)


def get_lq(queue):
    ρ = queue.ρ
    limit = queue.limit
    server = queue.server
    unlimited = queue.unlimited

    if server == 1:
        ls = get_ls(queue)
        if unlimited == True:
            data = get_lambda_efec(queue) / queue.µ
            return ls - data
        else:
            return ls - ρ
    else:
        div = ρ / server
        if unlimited == True:
            po = get_po(queue)
            if div == 1:
                pow1 = pow(ρ, server)
                res1 = limit - server
                res2 = limit - server + 1
                mul1 = pow1 * res1 * res2

                fact = factorial(server)
                mul2 = 2 * fact

                div = mul1 / mul2
                return po * div
            else:
                sum1 = server + 1
                pow1 = pow(ρ, sum1)

                res1 = server - 1
                fact = factorial(res1)
                res2 = server - ρ
                pow2 = pow(res2, 2)
                mul1 = fact * pow2

                div = pow1 / mul1
                return po * div
        else:
            pn = get_pn(queue, server)

            div = (server * ρ) / pow(server - ρ, 2)
            return div * pn


def get_ws(queue):
    server = queue.server
    unlimited = queue.unlimited
    ls = get_ls(queue)
    wq = get_wq(queue)

    if server == 1:
        if unlimited == True:
            data = 1 / queue.µ
            return wq / data
        else:
            return ls / queue.λ
    else:
        div = 1 / queue.µ
        return wq + div


def get_wq(queue):
    lq = get_lq(queue)
    λ = queue.λ
    server = queue.server

    if server == 1:
        if queue.unlimited == True:
            return get_lq(queue) / get_lambda_efec(queue)
        else:
            return lq / λ
    else:
        return lq / λ


def get_data(queue):

    data = {}

    if queue.unlimited == True:
        data = {
            'λ': round(queue.λ, 3),
            'µ': round(queue.µ, 3),
            'ρ': round(queue.ρ, 3),
            'Po': round(get_po(queue), 3),
            'Pn': round(get_pn(queue)[1], 3),
            'Ls': round(get_ls(queue), 3),
            'Lq': round(get_lq(queue), 3),
            'Ws': round(get_ws(queue), 3),
            'Wq': round(get_wq(queue), 3),
            'λ_efec': get_lambda_efec(queue),
            'λ_perd': get_lambda_perd(queue)
        }
    else:
        data = {
            'λ': round(queue.λ, 3),
            'µ': round(queue.µ, 3),
            'ρ': round(queue.ρ, 3),
            'Po': round(get_po(queue), 3),
            'Pn': round(get_pn(queue)[1], 3),
            'Ls': round(get_ls(queue), 3),
            'Lq': round(get_lq(queue), 3),
            'Ws': round(get_ws(queue), 3),
            'Wq': round(get_wq(queue), 3),
        }

    return data


def factorial(number):
    if number != 0:
        return number * factorial(number - 1)
    else:
        return 1
