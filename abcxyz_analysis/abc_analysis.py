import sqlite3


def get_data(cursor, sql):
    data_list = []
    for product in cursor.execute(sql):
        data_list.append(product[0])
    return data_list


def calculate_shares(data, total):
    list_of_shares = []
    for product in data:
        share = product / total * 100
        list_of_shares.append(share)
    return list_of_shares
        

def calculate_accumulated_shares(shares):
    list_of_accumulated_shares = []
    sum_of_shares = 0
    for share in shares:
        sum_of_shares += share
        list_of_accumulated_shares.append(sum_of_shares)
    return list_of_accumulated_shares


def assign_to_groups(accumulated_shares):
    list_of_groups = []
    for accumulated_share in accumulated_shares:
        if accumulated_share < 80:
            list_of_groups.append('A')
        elif accumulated_share < 95:
            list_of_groups.append('B')
        else:
            list_of_groups.append('C')
    return list_of_groups


def provide_analysis(cursor, sql):
    data = get_data(cursor, sql)
    total = sum(data)
    shares = calculate_shares(data, total)
    accumulated_shares = calculate_accumulated_shares(shares)
    groups = assign_to_groups(accumulated_shares)
    return groups