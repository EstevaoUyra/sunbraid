from sunbraid._version import __version__
VERSION = __version__

def get_imports():
    return f"""
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            <script src="https://d3js.org/d3.v6.min.js"></script>
            <script src="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{VERSION}/static/functions/line.js"></script>
            <link href="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{VERSION}/static/css/containers.css" rel="stylesheet">
            """

def make_head():
    all_imports = get_imports()
    return '<head>' + all_imports + '</head>'

def make_body(html):
    return (
        '<body>' + 
        html + 
        f'<script src="https://cdn.jsdelivr.net/gh/estevaouyra/sunbraid@{VERSION}/static/functions/containers.js"></script>'+
        '</body>'
    )
