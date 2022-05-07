from typing import Callable, Dict, Any, Tuple, List

from .baseui import BaseUi
from .output import Widget, Html

__all__ = ["Bootstrap", "NavLink", "Nav"]

class Bootstrap(BaseUi):
    
    def show(self):
        obj = self.widget.show()
        if hasattr(self, 'style'):
            obj.style(self.style)
        if hasattr(self, 'onclick'):
            obj.onclick(self.onclick)
        return obj

class NavLink(Bootstrap, Widget):
    template = '''
    <a class="nav-link" data-toggle="pill" role="tab" aria-controls="v-pills-profile" aria-selected="{{active}}">{{name}}</a>
    '''

    def __init__(self, name: str, active: bool=False):
        self.text = name
        self.active = str(active).lower()
        self.widget = Widget(self.template, {'name': self.name, 'active': self.active})

class Nav(Bootstrap, Widget):
    template = '''
    <div class="nav flex-column nav-pills" role="tablist" aria-orientation="vertical">
    {{#menus}}
    {{& pywebio_output_parse}}
    {{/menus}}
    </div>
    '''

    def __init__(self, menus: List[NavLink]):
        self.menus = menus
        self.data = {}

    def show(self):
        self.data = {'menus': list(map(self.ui_to_show, self.menus))}
        return Widget(self.template, self.data).show()