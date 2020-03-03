import os
import matplotlib.pyplot as plt
from fpdf import FPDF


def create_pie_chart(path, result):
    result_without_products = []
    for product in result:
        result_without_products.append(product[1])
    labels = ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    sizes = []
    for group in labels:
        sizes.append(result_without_products.count(group))
    colors = ['#64d448', '#51a33c', '#428731', '#ebe41a', '#ebc11a', '#ff8d0a',
            '#de5f50', '#cf3e2d', '#a30808']
    patches, texts1, texts2 = plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, 
                                    startangle=90, counterclock=False)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def make_table_preset(result):
    table = [['Product', 'Group']]
    for product in result:
        table.append(list(product))
    return table


def create_pdf(path, image, table):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.image(image, x=10, y=8, w=180)
    pdf.ln(60)
    pdf.ln(75)
    spacing = 1.1
    col_width = pdf.w / 2.2
    row_height = pdf.font_size * 1.5
    for row in table:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1, align="L")
        pdf.ln(row_height*spacing)
    pdf.output(path)


def compile_report(name, result):
    image_path = 'reports/' + name + '.png'
    pdf_path = 'reports/' + name + '.pdf'
    create_pie_chart(image_path, result)
    table_preset = make_table_preset(result)
    create_pdf(pdf_path, image_path, table_preset)
    os.remove(image_path)
