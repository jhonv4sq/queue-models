import jinja2
import pdfkit
import os
import json


def create_pdf(data, array):
    # path_template = os.path.abspath('./templates/queue.html')
    path_template = './queue.html'
    path_exit = './queue.pdf'
    wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

    with open('queue.html', 'w') as file:
        file.write("<h3 style='text-align: center;'><strong>lambda  = "+str(data['λ'])+", mu  = "+str(data['µ'])+", rho = "+str(data['ρ'])+", Po = "+str(data['Po'])+", Pn = "+str(data['Pn'])+", Ls = "+str(data['Ls'])+", Lq = "+str(data['Lq'])+", Ws = "+str(data['Ws'])+", Wq = "+str(data['Wq'])+"&nbsp;</strong></h3>")
        file.write("<hr />")

        if "λ_efec" in data:
            file.write("<h4 style='text-align: center;'><strong> lambda efec  = "+str(data['λ_efec'])+", lambda perd  = "+str(data['λ_perd'])+"&nbsp;</strong></h4>")
            file.write("<hr />")

        file.write("<p>&nbsp;</p>")
        file.write("<p>&nbsp;</p>")
        file.write("<table class='default' style='margin-left: auto; margin-right: auto; width: 507px; height: 123px;'>")
        file.write("<tbody>")
        file.write("<tr style='height: 15px;'>")
        file.write("<th style='width: 133.65px; height: 15px;'>N</th>")
        file.write("<th style='width: 160.962px; height: 15px;'>PN</th>")
        file.write("<th style='width: 193.587px; height: 15px;'>PN acumulado</th>")

        for pn in array:
            info = json.loads(pn)
            file.write("</tr>")
            file.write("<tr style='height: 36px;'>")
            file.write("<td style='width: 133.65px; height: 36px;text-align: center;'>"+str(info['n'])+"</td>")
            file.write("<td style='width: 133.65px; height: 36px;text-align: center;'>"+str(round(info['pn'], 4))+"</td>")
            file.write("<td style='width: 133.65px; height: 36px;text-align: center;'>"+str(round(info['sum_pn'], 4))+"</td>")
            file.write("</tr>")
        file.write("</tbody>")
        file.write("</table>")

    name = path_template.split('\\')[-1]
    path = path_template.replace(name, '')

    loader = jinja2.FileSystemLoader(path)
    env = jinja2.Environment(loader=loader)
    template = env.get_template(name)

    content = template.render(data)

    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
    pdfkit.from_string(content, path_exit, configuration=config)
    # pdfkit.from_file('queue.html', path_exit, configuration=config)

