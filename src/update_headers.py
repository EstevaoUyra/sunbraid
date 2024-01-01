from glob import glob
import json

css = glob("static/css/*", recursive=True)
functions = glob("static/css/*", recursive=True)
scripts = glob("static/css/*", recursive=True)

config = {
    'css': css,
    'functions': functions,
    'scripts': scripts,
}
with open('sunbraid/static.json', 'w') as f:
    json.dump(config, f, indent=2)