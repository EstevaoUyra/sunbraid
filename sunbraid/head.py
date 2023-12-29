def get_all_functions():
    with open('sunbraid/cell/line.js') as f:
        line = '<script>' + f.read() + '</script>'

    return line

def get_imports():
    return """
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://d3js.org/d3.v6.min.js"></script>

"""
def make_head():
    all_functions = get_all_functions()
    all_imports = get_imports()
    return '<head>' + all_functions + all_imports + '</head>'


