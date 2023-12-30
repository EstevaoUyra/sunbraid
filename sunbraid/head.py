
def get_imports():
    return """
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://d3js.org/d3.v6.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@v0.0.1-alpha/sunbraid/cell/line.js"></script>
"""

def make_head():
    all_imports = get_imports()
    return '<head>' + all_imports + '</head>'


