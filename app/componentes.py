from fasthtml.common import Div, H1, P, Form, Input, Button

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P("") 
    )

def gerar_formulario():
    return Form(
        Input(type="text", name="tarefa", placeholder="Insira uma Tarefa..."),
        Button("Enviar"),
        method="post",
        action="/adiciona_tarefa"
    )
