from fasthtml.common import fast_app, serve, Titled
from componentes import gerar_titulo, gerar_formulario

app, routes = fast_app()

@routes("/")
def home():
    formulario = gerar_formulario()
    return Titled("Lista de Tarefas", formulario)

@routes("/adicionar_tarefas")

@routes("/blog")
def blog():
    return gerar_titulo("Blog", "Componentes em FastHTML")

@routes("/api")
def api():
    return gerar_titulo("", "")

serve()
