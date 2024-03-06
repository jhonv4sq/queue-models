import json

def show_pn_table(datas):
    print('\nN  Pn  Sum pn')
    for pn in datas:
        data = json.loads(pn)
        print('|{}|{}|{}|'.format(data['n'],round(data['pn'], 4),round(data['sum_pn'], 4)))
