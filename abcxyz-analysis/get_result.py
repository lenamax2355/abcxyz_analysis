import sqlite3
import json

import abc_analysis as abc
import xyz_analysis as xyz


def get_products_data(cursor, sql):
    products_dict = {}
    for product in cursor.execute(sql):
        products_dict[product[0]] = {}
    return products_dict


def get_overall_result(cursor, product_sql, abc_sql, xyz_sql):
    products = get_products_data(cursor, products_sql)
    abc_result = abc.provide_analysis(cursor, abc_sql)
    xyz_result = xyz.provide_analisys(cursor, xyz_sql)
    intermediate_overall_result = []
    for product in zip(abc_result, xyz_result):
        intermediate_overall_result.append(''.join(product))
    final_overall_result = []
    for product in zip(products, intermediate_overall_result):
        final_overall_result.append(product)
    return final_overall_result


def write_result_to_database(connect, cursor, result):
    cursor.execute("""CREATE TABLE abc_xyz_analysis
                    (product text, result text)
                    """)

    for product in result:
        product_name = product[0]
        result = product[1]
        cursor.execute("""INSERT INTO abc_xyz_analysis 
                        (product, result) VALUES (?, ?)""",
                        (product_name, result))
        connect.commit()


if __name__ == "__main__":
    with open("/home/badger_bo/devel/abcxyz-analysis/abcxyz-analysis/data.json") as json_file:
        data_dict = json.load(json_file)
        for company in data_dict:
            database = data_dict[company]['database']
            products_sql = data_dict[company]['products_sql']
            abc_sql = data_dict[company]['abc_sql']
            xyz_sql = data_dict[company]['xyz_sql']
            conn = sqlite3.connect(database)
            c = conn.cursor()
            overall_result = get_overall_result(c, products_sql, abc_sql, xyz_sql)
            write_result_to_database(conn, c, overall_result)