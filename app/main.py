from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
    return "<h1>Pagina Segura</h1>"

serve()