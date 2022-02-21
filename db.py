import pandas as pd

def create_tables(cols_names, table_name):
    n = len(cols_names)
    header = []
    doc1 = '<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>'
    out1 = doc1 + f"<table id={table_name}><tr>"
    for name in cols_names:
        tab = f" <th>{name}</th>"
        out1 += tab
    out1 += "</tr></table>"
    out1 += "</body></html>"

    return out1



def add_data(data, tbl):
    table1 = tbl
    end = table1[-22:]
    table2 = table1[:-22]
    ans1 = "<tr>"
    for dat in data:
        ans1 += f"<td>{dat}</td>"
    data +="</tr>"
    table2 += ans1
    table2 += end
    return table2


  #EXAMPLE DEMO

res1 = [add_data(data=[8,5,3,5,6], tbl=create_tables(cols_names=['A','B','C','D','E'], table_name='table1'))]

for i in range(1000-1):
    tb1 = res1[-1]
    dat = list(np.random.randn(5))
    res1.append(add_data(data=dat, tbl=tb1))

df2 = pd.read_html(res1[-1])[0]
#df2
