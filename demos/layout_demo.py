'''
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def main():
    put_row([
        put_column([
            put_code('A'),
            put_row([
                put_code('B1'), None,  # None represents the space between the output
                put_code('B2'), None,
                put_code('B3'),
            ]),
            put_code('C'),
        ]), None,
        put_code('D'), None,
        put_code('E')
    ])
#source: https://pywebio-demos.pywebio.online/doc_demo?app=demo-put-row-column
'''

from typewebio import *
from pywebio import start_server


def layout_demo():
    r = Row()
    r.add_content(Code('B1'), None, Code('B2'), None, Code('B3'))
    l = Column()
    l.add_content(Code('A'), r, Code('C'))
    m_r = Row()
    m_r.add_content(l, None, Code('D'), None, Code('E'))

    return m_r

app = layout_demo()

def main_typewebio():

    app.show()

start_server(main_typewebio, port=8080, debug=True)
