<div align="center">

# TypeWebIO

_Write interactive web app in declaration way._

> 自由是服从自定的规则

 [![CodeFactor](https://www.codefactor.io/repository/github/luxuncang/TypeWebIo/badge)](https://www.codefactor.io/repository/github/luxuncang/TypeWebIo)
 [![GitHub](https://img.shields.io/github/license/luxuncang/TypeWebIo)](https://github.com/luxuncang/TypeWebIo/blob/master/LICENSE)
 [![CodeQL](https://github.com/luxuncang/TypeWebIo/workflows/CodeQL/badge.svg)](https://github.com/luxuncang/TypeWebIo/blob/master/.github/workflows/codeql-analysis.yml)

</div>

## **特性**

* 声明式UI
* 完全兼容PyWebIO
* 重新抽象了自定义组件

## 快速入门

### Layout

```python
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
```

### Popup

```python
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
```

### Edit

```python
from typewebio import *
from pywebio import start_server
from functools import partial

from pywebio.output import *

async def run_code():
    code = await pin.code
    with Scope.use_scope("web"):
        exec(code)

def edit_demo():

    # Create the main layoutthe main layout
    main = Scope("main")
    web = Scope("web")
    edit = Scope("edit")
    mc = Row([web, None, edit], size="50% 1% 49%")
    main.add_content(mc)

    # Create Edit layout
    edit.add_content(
        PinTextarea(
            "code",
            label="TypeWebIO Edit",
            rows=40,
            code={"mode": "python", "theme": "darcula"},
            value="from typewebio import *\n",
        )
    )

    edit.add_content(
        ButtonGroup(["Run", "Clear"], [run_code, partial(Scope.clear, "web")])
    )

    # Create Web layout
    web.add_content(Code("Hello World"))
    return main

app = edit_demo()

async def main_typewebio():
    Session.set_env(output_max_width="100%")
    app.show()

start_server(main_typewebio, port=8080, debug=True)
```

**注意: 本项目正在快速迭代中**
