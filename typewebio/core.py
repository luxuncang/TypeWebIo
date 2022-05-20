from pywebio import config
from pywebio.platform.fastapi import start_server
from pywebio.session import hold

from functools import partial

from .bootstrap import *
from .input import *
from .output import *
from .session import *
from .pin import *

__all__ = ["TypeWebIo"]


class TypeWebIo(Session):
    def __init__(
        self,
        name: str,
        head: list = None,
        body: list = None,
        js: list = None,
        html: list = None,
        output_max_width="100%",
        **env_info
    ):
        self.scope = Scope(name)
        self.head = head or []
        self.body = body or []
        self.js = js or []
        self.html = html or []
        self.output_max_width = output_max_width
        self.env_info = env_info
        self.init_show_func = []
        self.before_show_func = []

    def show_init(self):
        self.set_env(**{"output_max_width": self.output_max_width, **self.env_info})
        for h in self.head:
            self.add_head(h)
        for b in self.body:
            self.add_body(b)
        for j in self.js:
            self.run_js(j)
        for h in self.html:
            self.add_html(h)
        for f in self.init_show_func:
            f()

    def show(self):
        self.show_init()
        res = self.scope.show()
        for f in self.before_show_func:
            f()
        return res

    def run(
        self,
        port=8080,
        host="127.0.0.1",
        cdn=False,
        static_dir=None,
        remote_access=False,
        debug=False,
        allowed_origins=None,
        check_origin=None,
        auto_open_webbrowser=False,
        **uvicorn_settings
    ):

        async def start_typewebio():
            return self.show()

        start_server(
            start_typewebio,
            port,
            host,
            cdn,
            static_dir,
            remote_access,
            debug,
            allowed_origins,
            check_origin,
            auto_open_webbrowser,
            **uvicorn_settings
        )

    def add_content(self, *content):
        return self.scope.add_content(*content)

    def remove_content(self, *content):
        return self.scope.remove_content(*content)

    def set_init_show(self, *func):
        self.init_show_func += list(func)

    def set_before_show(self, *func):
        self.before_show_func += list(func)