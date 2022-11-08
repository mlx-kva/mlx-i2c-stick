import os
import yaml

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

loader=FileSystemLoader(THIS_DIR)

with open('context.yml', 'r') as file:
    context = yaml.safe_load(file)

env = Environment(
    loader=loader,
    autoescape=select_autoescape()
)

template = env.get_template("index.jinja2.html")

with open('index.html', 'w') as f:
    f.write(template.render(context))
