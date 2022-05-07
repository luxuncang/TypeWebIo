'''
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def main():
    with popup('Popup title') as s:
        put_html('<h3>Popup Content</h3>')
        put_text('html: <br/>')
        put_buttons([('clear()', s)], onclick=clear)
    
    put_text('Also work!', scope=s)

start_server(main, port=8080, debug=True)
#source: https://pywebio-demos.pywebio.online/doc_demo?app=demo-popup-context
'''

from typewebio import *
from pywebio import start_server


def popup_demo():
    p = Popup('Popup title')
    s = Scope('popup_text')
    s.add_content(Html('<h3>Popup Content</h3>'))
    s.add_content(Text('html: <br/>'))
    s.add_content(ButtonGroup([('clear()', 'popup_text')], Scope.clear))
    p.add_content(s)
    return p

app = popup_demo()

def main_typewebio():
    app.show()

start_server(main_typewebio, port=8080, debug=True)