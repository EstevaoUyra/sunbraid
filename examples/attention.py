import pandas as pd
from sunbraid.head import make_head
from sunbraid.cell.line import make_lineplot
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/attention.csv")
df = df.groupby(['attention', 'solutions']).apply(lambda df: [df[['subject', 'score']]]).rename("data").reset_index()

def rep(d, **kwargs):
    return (
        d[0].rename(columns={v:k for k,v in kwargs.items()})
        .assign(color='#000000')
        .assign(linestyle= lambda d: d.x.apply(lambda v: 'solid' if v%2 else 'dotted'))
        .assign(xlabel=lambda d: d.x)
        ).to_dict('records')

df['data'] = df['data'].apply(rep, x='subject', value='score')
df['plot'] = df['data'].apply(make_lineplot)

html = make_head() + df.style.set_table_attributes("class='table'").to_html()
with open('examples/attention.html', 'w') as f:
    f.write(html)
