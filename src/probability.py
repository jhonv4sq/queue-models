import json

def get_po(queue): # Probabilidad de que el sistema este ocupado
    ρ = queue.ρ

    if queue.unlimited == True:
        limit = queue.limit

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


def probability_first_clinet(queue): # Probabilidad de ser el primer cliente en la cola
    λ = queue.λ / 60
    µ = queue.µ / 60
    ρ = λ / µ
    probability = get_po(queue) * ρ
    return probability


def customers_in_queue(queue): # Numero promedio de cliente en la cola
    time = int(input("Tiempo de espera en la cola en minutos: ")) # 2
    λ = queue.λ / 60
    µ = queue.µ / 60
    ρ = λ / µ
    customers = λ * time
    return round(customers)


def probability_four_clinets(queue): # probabilidad de que haya 4 clientes en la cola
    λ = queue.λ / 60
    µ = queue.µ / 60
    ρ = λ / µ
    probability = get_po(queue) * pow(ρ, 4)
    return probability


def limit_lost_clinet(queue): # Probabilidad de que un cliente llegue y no sea atendido porque este lleno
    data1 = 1 - queue.ρ
    pow1 = pow(queue.ρ, queue.limit)
    data2 = data1 * pow1

    pow2 = pow(queue.ρ, queue.limit+1)
    data3 = 1-pow2

    probability = data2 / data3
    return probability


def get_pn(queue):
    data = []
    stop = True
    totals = 0
    limit = queue.limit
    n = 0
    po = get_po(queue)
    ρ = queue.ρ
    unlimited = queue.unlimited

    while stop:
        
        pn = po * pow(ρ, n)

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

    return [data, len(data) - 1]


def get_ls(queue):
    limit = queue.limit
    po = get_po(queue)
    ρ = queue.ρ

    if queue.unlimited == True:
        if ρ != 1:
            # (results.rho * (1 - ((form.limite_cola + 1) * (results.rho ** form.limite_cola)) + (form.limite_cola * (results.rho ** (form.limite_cola + 1)))))
            data1 = (ρ * (1 - ((limit + 1) * pow(ρ, limit)) + (limit * pow(ρ, limit +1))))
            data2 = ((1 - ρ) * (1 - pow(ρ, limit + 1)))
            return data1 / data2
        else:
            return limit / 2

    else:
        return ρ / po


def get_lambda_efec(queue):
    data = json.loads(get_pn(queue)[0][queue.limit])
    return queue.λ * (1 - data['pn'])


def get_lambda_perd(queue):
    return queue.λ - get_lambda_efec(queue)


def get_lq(queue):
    ls = get_ls(queue)
    ρ = queue.ρ

    if queue.unlimited == True:
        data = get_lambda_efec(queue) / queue.µ
        return ls - data
    else:
        return ls - ρ


def get_ws(queue):
    ls = get_ls(queue)
    λ = queue.λ

    if queue.unlimited == True:
        data = 1 / queue.µ
        return get_wq(queue) / data
    else:
        return ls / λ


def get_wq(queue):
    lq = get_lq(queue)
    λ = queue.λ

    if queue.unlimited == True:
        return get_lq(queue) / get_lambda_efec(queue)
    else:
        return lq / λ

