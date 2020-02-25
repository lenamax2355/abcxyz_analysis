from statistics import mean, pstdev


def get_data(cursor, sql):
    quarters_margin_list = []
    for product in cursor.execute(sql):
        quarters_margin_list.append([product[0], product[1], product[2], product[3]])
    return quarters_margin_list


def calculate_coefficients_of_variation(data):
    coefficients_of_variation = []
    for product in data:
        coefficient_of_variation = pstdev(product)  / mean(product) * 100
        coefficients_of_variation.append(coefficient_of_variation)
    return coefficients_of_variation


def assign_to_groups(coefficients_of_variation):
    list_of_groups = []
    for variation in coefficients_of_variation:
        if variation > 25:
            list_of_groups.append('Z')
        elif variation < 25 and variation > 10:
            list_of_groups.append('Y')
        else:
            list_of_groups.append('X')
    return list_of_groups


def provide_analisys(cursor, sql):
    data = get_data(cursor, sql)
    coefficients_of_variation = calculate_coefficients_of_variation(data)
    groups = assign_to_groups(coefficients_of_variation)
    return groups