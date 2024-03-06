import jinja2
import pdfkit
import os


def create_pdf(data):
    # path_template = os.path.abspath('./templates/queue.html')
    path_template = './queue.html'
    path_exit = './queue.pdf'
    wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

    # values = "&lambda; = {{&lambda;}}, &micro; = {{&micro;}}, &rho; = {{&rho;}}, Po = {{Po}}, Pn = {{Pn}}, Ls = {{Ls}}, Lq = {{Lq}}, Ws = {{Ws}}, Wq = {{Wq}}"

    # with open('queue.html', 'w') as file:
    #     file.write("<div style='color: #334455; padding-top: 10px; text-align: center;'>"+values+"</div>")
    #     file.write("<div style='color: #334455; padding-top: 10px; text-align: center;'>&nbsp;</div>")

    name = path_template.split('\\')[-1]
    path = path_template.replace(name, '')

    loader = jinja2.FileSystemLoader(path)
    env = jinja2.Environment(loader=loader)
    template = env.get_template(name)

    content = template.render(data)

    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
    pdfkit.from_string(content, path_exit, configuration=config)
    # pdfkit.from_file('queue.html', path_exit, configuration=config)

