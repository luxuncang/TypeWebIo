from typing import List, Tuple, Union
from copy import copy

from pywebio import output as pwoutput
from pywebio.output import *  # type: ignore
from pywebio.output import Position, OutputPosition

from .baseui import BaseUi

__all__ = [
    "BaseOutput",
    "BaseNotice",
    "BaseLayout",
    "Scope",
    "Text",
    "Markdown",
    "Info",
    "Success",
    "Warn",
    "Error",
    "Html",
    "Link",
    "Processbar",
    "Loading",
    "Code",
    "Table",
    "Span",
    "Button",
    "ButtonGroup",
    "Image",
    "File",
    "Tabs",
    "Collapse",
    "Scrollable",
    "Toast",
    "Popup",
    "Row",
    "Column",
    "Grid",
    "style",
]


class BaseOutput(BaseUi):
    def show(self):
        func = getattr(pwoutput, self.uitype)
        agrg, kwarg = self.general_parameters(func, self.get_kw())
        obj = func(*agrg, **kwarg)
        if hasattr(self, "style"):
            obj.style(self.style)
        if hasattr(self, "on_click"):
            obj.onclick(self.onclick)  # type: ignore
        return obj

    @property
    def uitype(self):
        cls_naem = self.__class__.__name__
        if cls_naem == "Scope":
            return "put_scope"
        if cls_naem == "Text":
            return "put_text"
        if cls_naem == "Markdown":
            return "put_markdown"
        if cls_naem == "Info":
            return "put_info"
        if cls_naem == "Success":
            return "put_success"
        if cls_naem == "Warn":
            return "put_warning"
        if cls_naem == "Error":
            return "put_error"
        if cls_naem == "Html":
            return "put_html"
        if cls_naem == "Link":
            return "put_link"
        if cls_naem == "Processbar":
            return "put_processbar"
        if cls_naem == "Loading":
            return "put_loading"
        if cls_naem == "Code":
            return "put_code"
        if cls_naem == "Table":
            return "put_table"
        if cls_naem == "Span":
            return "put_span"
        if cls_naem == "Button":
            return "put_button"
        if cls_naem == "ButtonGroup":
            return "put_buttons"
        if cls_naem == "Image":
            return "put_image"
        if cls_naem == "File":
            return "put_file"
        if cls_naem == "Tabs":
            return "put_tabs"
        if cls_naem == "Scrollable":
            return "put_scrollable"
        if cls_naem == "Collapse":
            return "put_collapse"
        if cls_naem == "Widget":
            return "put_widget"
        raise Exception("Unknown type")

    def set_style(self, style):
        self.style = style

    def set_onclick(self, onclick):
        self.on_click = onclick

    def update_data(self, name, value):
        if hasattr(self, name):
            setattr(self, name, value)


class BaseNotice(BaseUi):
    def show(self):
        func = getattr(pwoutput, self.uitype)
        agrg, kwarg = self.general_parameters(func, self.get_kw())
        return func(*agrg, **kwarg)

    @property
    def uitype(self):
        cls_naem = self.__class__.__name__
        if cls_naem == "Toast":
            return "toast"
        if cls_naem == "Popup":
            return "popup"
        raise Exception("Unknown type")


class BaseLayout(BaseUi):
    def add_content(self, *content):
        self._content += list(content)  # type: ignore

    def remove_content(self, *content):
        for c in content:
            self._content.remove(c)  # type: ignore

    def show(self):
        self.content = list(map(self.ui_to_show, self.get_content()))
        func = getattr(pwoutput, self.uitype)
        agrg, kwarg = self.general_parameters(func, self.get_kw())
        obj = func(*agrg, **kwarg)
        if hasattr(self, "style"):
            obj.style(self.style)
        if hasattr(self, "on_click"):
            obj.onclick(self.onclick)  # type: ignore
        return obj

    @property
    def uitype(self):
        cls_naem = self.__class__.__name__
        if cls_naem == "Row":
            return "put_row"
        if cls_naem == "Column":
            return "put_column"
        if cls_naem == "Grid":
            return "put_grid"
        raise Exception("Unknown type")

    def set_style(self, style):
        self.style = style

    def set_onclick(self, onclick):
        self.on_click = onclick

    def get_content(self):
        if isinstance(self._content, list):  # type: ignore
            return self._content  # type: ignore
        return [self._content]  # type: ignore


class Scope(BaseOutput):
    def __init__(
        self,
        name: str,
        content: list = None,  # type: ignore
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.name = name
        self.content = content or []
        self._content = copy(content) or []
        self.scope = scope
        self.position = position

    def show(self):
        self.content = list(map(self.ui_to_show, self.get_content()))
        return super().show()

    def add_content(self, *content):
        self._content += list(content)

    def remove_content(self, *content):
        for c in content:
            self._content.remove(c)

    def get_content(self):
        if isinstance(self._content, list):
            return self._content
        return [self._content]

    @classmethod
    def use_scope(cls, name=None, clear=False, **kwargs):
        return use_scope(name, clear, **kwargs)

    @classmethod
    def put_scope(cls, name, content: list = None, scope=None, position: int = -1):  # type: ignore
        content = content or []
        return put_scope(name, content, scope, position)

    @classmethod
    def get_scope(cls, stack_id: int = None):  # type: ignore
        return get_scope(stack_id)

    @classmethod
    def clear(cls, scope: str = None):  # type: ignore
        return clear(scope)

    @classmethod
    def remove(cls, scope: str = None):  # type: ignore
        return remove(scope)

    @classmethod
    def scroll_to(cls, scope: str = None, position: Position = Position.TOP):  # type: ignore
        return scroll_to(scope, position)  # type: ignore


class Text(BaseOutput):
    def __init__(
        self, *texts, sep=" ", inline=False, scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.texts = texts
        self.sep = sep
        self.inline = inline
        self.scope = scope
        self.position = position


class Markdown(BaseOutput):
    def __init__(
        self,
        mdcontent,
        lstrip=True,
        options=None,
        sanitize=True,
        scope=None,
        position=OutputPosition.BOTTOM,
        **kwargs
    ):
        self.kw = locals()
        self.mdcontent = mdcontent
        self.lstrip = lstrip
        self.options = options
        self.sanitize = sanitize
        self.scope = scope
        self.position = position
        self.kwargs = kwargs


class Info(BaseOutput):
    def __init__(
        self, *contents, closable=False, scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.contents = contents
        self.closable = closable
        self.scope = scope
        self.position = position


class Success(BaseOutput):
    def __init__(
        self, *contents, closable=False, scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.contents = contents
        self.closable = closable
        self.scope = scope
        self.position = position


class Warn(BaseOutput):
    def __init__(
        self, *contents, closable=False, scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.contents = contents
        self.closable = closable
        self.scope = scope
        self.position = position


class Error(BaseOutput):
    def __init__(
        self, *contents, closable=False, scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.contents = contents
        self.closable = closable
        self.scope = scope
        self.position = position


class Html(BaseOutput):
    def __init__(
        self,
        html: str,
        sanitize: bool = False,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.html = html
        self.sanitize = sanitize
        self.scope = scope
        self.position = position


class Link(BaseOutput):
    def __init__(
        self,
        name,
        url=None,
        app=None,
        new_window=False,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.name = name
        self.url = url
        self.app = app
        self.new_window = new_window
        self.scope = scope
        self.position = position


class Processbar(BaseOutput):
    def __init__(
        self,
        name,
        init=0,
        label=None,
        auto_close=False,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.name = name
        self.init = init
        self.label = label
        self.auto_close = auto_close
        self.scope = scope
        self.position = position

    @classmethod
    def set_processbar(cls, name, value, label=None):
        return set_processbar(name, value, label)


class Loading(BaseOutput):
    def __init__(
        self, shape="border", color="dark", scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.shape = shape
        self.color = color
        self.scope = scope
        self.position = position


class Code(BaseOutput):
    def __init__(
        self,
        content,
        language="",
        rows: str = None,  # type: ignore
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.content = content
        self.language = language
        self.rows = rows
        self.scope = scope
        self.position = position


class Table(BaseOutput):
    def __init__(self, tdata, header=None, scope=None, position=OutputPosition.BOTTOM):
        self.kw = locals()
        self.tdata = tdata or []
        self._tdata = tdata or []
        self.header = header or []
        self._header = header or []
        self.scope = scope
        self.position = position

    def show(self):
        self.tdata = [list(map(self.ui_to_show, i)) for i in self.get_tdata()]
        self.header = list(map(self.ui_to_show, self.get_header()))
        return super().show()

    def get_tdata(self):
        return self._tdata

    def get_header(self):
        return self._header

    def add_tdata(self, *tdata):
        self._tdata += list(tdata)

    def add_header(self, *header):
        self._header += list(header)

    def remove_tdata(self, *tdata):
        for i in tdata:
            self._tdata.remove(i)

    def remove_header(self, *header):
        for i in header:
            self._header.remove(i)


class Span(BaseOutput):
    def __init__(self, content, row=1, col=1):
        self.kw = locals()
        self.content = content
        self.row = row
        self.col = col


class Button(BaseOutput):
    def __init__(
        self,
        label,
        onclick,
        color=None,
        small=None,
        link_style=False,
        outline=False,
        disabled=False,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.label = label
        self.onclick = onclick
        self.color = color
        self.small = small
        self.link_style = link_style
        self.outline = outline
        self.disabled = disabled
        self.scope = scope
        self.position = position


class ButtonGroup(BaseOutput):
    def __init__(
        self,
        buttons,
        onclick,
        small=None,
        link_style=False,
        outline=False,
        group=False,
        scope=None,
        position=OutputPosition.BOTTOM,
        **callback_options
    ):
        self.kw = locals()
        self.buttons = buttons
        self.onclick = onclick
        self.small = small
        self.link_style = link_style
        self.outline = outline
        self.group = group
        self.scope = scope
        self.position = position
        self.callback_options = callback_options


class Image(BaseOutput):
    def __init__(
        self,
        src,
        format=None,
        title="",
        width=None,
        height=None,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.src = src
        self.format = format
        self.title = title
        self.width = width
        self.height = height
        self.scope = scope
        self.position = position


class File(BaseOutput):
    def __init__(
        self, name, content, label=None, scope=None, position=OutputPosition.BOTTOM
    ):
        self.kw = locals()
        self.name = name
        self.content = content
        self.label = label
        self.scope = scope
        self.position = position


class Tabs(BaseOutput):
    def __init__(
        self,
        tabs: List[Tuple[str, BaseOutput]],
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.tabs = tabs
        self._tabs = copy(tabs) or []
        self.scope = scope
        self.position = position

    def show(self):
        self.tabs = list(
            map(
                self.get_tab,
                zip(self.get_tab_names(), map(self.ui_to_show, self.get_tab_value())),
            )
        )
        return super().show()

    def add_tab(self, name, tab):
        self._tabs.append((name, tab))

    def remove_tab(self, name):
        self._tabs = list(filter(lambda x: x[0] != name, self._tabs))

    def get_tab_value(self):
        return map(lambda tab: tab[1], self._tabs)

    def get_tab_names(self):
        return map(lambda tab: tab[0], self._tabs)

    def get_tab(self, tab: tuple):
        return {"title": tab[0], "content": tab[1]}


class Collapse(BaseOutput):
    def __init__(
        self,
        title,
        content: list,
        open=False,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.title = title
        self.content = content or []
        self._content = copy(content) or []
        self.open = open
        self.scope = scope
        self.position = position

    def show(self):
        self.content = list(map(self.ui_to_show, self.get_content()))
        return super().show()

    def add_content(self, *content):
        self._content += list(content)

    def remove_content(self, *content):
        for c in content:
            self._content.remove(c)

    def get_content(self):
        if isinstance(self._content, list):
            return self._content
        return [self._content]


class Scrollable(BaseOutput):
    def __init__(
        self,
        content: list = None,  # type: ignore
        height=400,
        keep_bottom=False,
        border=True,
        scope=None,
        position=OutputPosition.BOTTOM,
        **kwargs
    ):
        self.kw = locals()
        self.content = content or []
        self._content = copy(content) or []
        self.height = height
        self.keep_bottom = keep_bottom
        self.border = border
        self.scope = scope
        self.position = position
        self.kwargs = kwargs

    def show(self):
        self.content = list(map(self.ui_to_show, self.get_content()))
        return super().show()

    def add_content(self, *content):
        self._content += list(content)

    def remove_content(self, *content):
        for c in content:
            self._content.remove(c)

    def get_content(self):
        if isinstance(self._content, list):
            return self._content
        return [self._content]


class Widget(BaseOutput):
    def __init__(self, template, data=None, scope=None, position=OutputPosition.BOTTOM):
        self.kw = locals()
        self.template = template
        self.data = data or {}
        self.scope = scope
        self.position = position


class Toast(BaseNotice):
    def __init__(
        self, content: str, duration=2, position="center", color="info", onclick=None
    ):
        self.kw = locals()
        self.content = content
        self.duration = duration
        self.position = position
        self.color = color
        self.onclick = onclick


class Popup(BaseNotice):
    def __init__(
        self,
        title,
        content: list = None,  # type: ignore
        size=PopupSize.NORMAL,
        implicit_close=True,
        closable=True,
    ):
        self.kw = locals()
        self.title = title
        self.content = content or []
        self._content = copy(content) or []
        self.size = size
        self.implicit_close = implicit_close
        self.closable = closable

    @classmethod
    def close(cls):
        return close_popup()

    def show(self):
        self.content = list(map(self.ui_to_show, self.get_content()))
        return super().show()

    def add_content(self, *content):
        self._content += list(content)

    def remove_content(self, *content):
        for c in content:
            self._content.remove(c)

    def get_content(self):
        if isinstance(self._content, list):
            return self._content
        return [self._content]


class Row(BaseLayout):
    def __init__(
        self,
        content: list = None,  # type: ignore
        size=None,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.content = content or []
        self._content = copy(content) or []
        self.size = size
        self.scope = scope
        self.position = position


class Column(BaseLayout):
    def __init__(
        self,
        content: list = None,  # type: ignore
        size=None,
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.content = content or []
        self._content = copy(content) or []
        self.size = size
        self.scope = scope
        self.position = position


class Grid(BaseLayout):
    def __init__(
        self,
        content: list,
        cell_width="auto",
        cell_height="auto",
        cell_widths=None,
        cell_heights=None,
        direction="row",
        scope=None,
        position=OutputPosition.BOTTOM,
    ):
        self.kw = locals()
        self.content = content or []
        self._content = copy(content) or []
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_widths = cell_widths
        self.cell_heights = cell_heights
        self.direction = direction
        self.scope = scope
        self.position = position
