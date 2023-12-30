
VERSION = 'v0.0.2-alpha'

def get_imports():
    return f"""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://d3js.org/d3.v6.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{VERSION}/sunbraid/cell/line.js"></script>
<link href="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{VERSION}/sunbraid/css/containers.css" rel="stylesheet">
"""

def make_head():
    all_imports = get_imports()
    return '<head>' + all_imports + '</head>'


