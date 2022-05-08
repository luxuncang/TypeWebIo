from pywebio.session import *

__all__ = ["Session"]

class Session:

    local = local
    info = info
    hold = hold

    @classmethod
    def download(cls, name: str, content: bytes):
        return download(name, content)

    @classmethod
    def run_js(cls, code: str, **args):
        return run_js(code, **args)

    @classmethod
    def eval_js(cls, code: str, **args):
        return eval_js(code, **args)

    @classmethod
    def register_thread(cls, thread):
        return register_thread(thread)

    @classmethod
    def defer_call(cls, func):
        return defer_call(func)

    @classmethod
    def set_env(cls, **env_info):
        return set_env(**env_info)

    @classmethod
    def go_app(cls, name, new_window=True):
        return go_app(name, new_window=True)

    @classmethod
    def add_head(cls, url: str):
        '''<script src="https://unpkg.com/element-ui/lib/index.js"></script>'''
        return cls.run_js(f'''$('head').append('{url}')''')