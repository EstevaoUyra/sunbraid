import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


def b64encode(fig):
    if type(fig) == plt.Axes:
        fig = fig.figure

    if type(fig) == plt.Figure:
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        b64_string = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{b64_string}"

def embed_to_img(obj):
    if type(obj)!=str:
        img_src = b64encode(obj)
    else:
        img_src = obj

    return f'<img src="{img_src}" style="max-width:100%; max-height:100%;">'
        
def container(content, uid='', classes=''):
    div_start = ''
    if classes != '':
        div_start += f' class="{classes}"'
    if uid != '':
        div_start += f' id="{uid}"'
    return f"""<div{div_start}>
    {content}
    </div>
    """

def make_plotter(f, classes='incell'):
    def g(*args, **kwargs):
        fig, ax = plt.subplots()
        pres = f(*args, **kwargs, ax=ax)
        plt.close(fig)
        return container(embed_to_img(pres), classes=classes)
    return g