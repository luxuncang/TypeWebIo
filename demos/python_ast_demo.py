from typewebio import *
from functools import partial
import ast

def get_ast(code, old_code):
    try:
        sast = ast.dump(ast.parse(code, mode="exec"), indent=4)
    except SyntaxError as e:
        sast = "SyntaxError: {}".format(e)
    finally:
        return sast # type: ignore

async def run_code():
    code = await pin.code  # type: ignore
    scl = Scrollable(height=900)
    sast = ast.dump(ast.parse(code, mode="exec"), indent=4)
    scl.add_content(Code(sast))
    with Scope.use_scope("webio_edit_demo_web", clear=True):
        scl.show()


async def onchange_code(code):
    if code == onchange_code.old_code:
        return None
    scl = Scrollable(height=900)
    sast = get_ast(code, onchange_code.old_code)
    onchange_code.old_code = code
    scl.add_content(Code(sast))
    with Scope.use_scope("webio_edit_demo_web", clear=True):
        scl.show()


def edit_demo():

    # Create the main layoutthe main layout
    main = Scope("webio_edit_demo_main")
    web = Scope("webio_edit_demo_web")
    edit = Scope("webio_edit_demo_edit")
    mc = Row([web, None, edit], size="50% 1% 49%")
    main.add_content(mc)

    # Create Edit layout
    pta = PinTextarea(
        "code",
        label="Python Ast",
        rows=40,
        code={"mode": "python", "theme": "darcula"},
        value="print('Hello World!')\n",
    )
    pta.on_change = onchange_code
    edit.add_content(pta)

    edit.add_content(
        ButtonGroup(
            ["Run", "Clear"], [run_code, partial(Scope.clear, "webio_edit_demo_web")]
        )
    )

    # Create Web layout
    web.add_content(Code(get_ast("print('Hello World!')\n", "")))
    return main


onchange_code.old_code = None
app = TypeWebIo("webio_edit_demo")
app.add_content(edit_demo())
app.run()
