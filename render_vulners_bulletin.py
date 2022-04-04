from jinja2 import Environment, FileSystemLoader

def render_bulletin(bulletin_data):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("vulners_report_template.html")
    return template.render(bulletin_data)
