
from flask import Flask, render_template # type: ignore
app = Flask(__name__)

# Sample Blog Posts
posts = [
    {"id": 1, "title": "Introduccion a Python", "content": "Python es un lenguaje de programación de alto nivel, versátil y popular, conocido por su sintaxis clara y legible, similar al inglés. Es interpretado, orientado a objetos y de propósito general, ideal para principiantes y profesionales en desarrollo web, ciencia de datos, inteligencia artificial y automatización.", "autor": "Leonardo Zapa"},
    {"id": 2, "title": "Importancia del Diseño Web con Python", "content": "Hacer páginas web en Python es fundamental por su sintaxis sencilla y legible, que aumenta la productividad y agiliza el desarrollo. Frameworks robustos como Django y Flask facilitan la creación de sitios seguros, escalables y rápidos, ideales para comercio electrónico y aplicaciones complejas. Además, permite integrar fácilmente inteligencia artificial y análisis de datos. "
    "Puntos clave de la importancia de Python en el desarrollo web:"
    "Productividad y Simplicidad: Su sintaxis similar al inglés permite escribir menos código, facilitando el mantenimiento y reduciendo errores."
    "Frameworks Poderosos: Django ofrece herramientas predefinidas para seguridad, autenticación y manejo de bases de datos, mientras Flask brinda flexibilidad para microservicios."
    "Versatilidad (IA y Datos): Python es el lenguaje líder en Ciencia de Datos y Machine Learning, lo que permite integrar funcionalidades inteligentes, chatbots o analítica avanzada directamente en la web.", "autor": "Leonardo Zapa"},
    {"id": 3, "title": "Seguridad y Herramientas de Python", "content": "Python es fundamental en ciberseguridad para automatizar tareas, analizar datos y crear herramientas personalizadas de hacking ético, gracias a su sintaxis sencilla y potentes librerías. Destacan herramientas como Scapy (redes), Bandit (análisis de código), PyCryptodome (criptografía) y frameworks de pruebas como ZAP. Permite el desarrollo seguro y el análisis de vulnerabilidades.", "autor": "Leonardo Zapa"},
    {"id": 4, "title": "Mi Mejor Experiencia con Python", "content": "Cuando se habla de programacion, pocos lenguajes logran equilibrar facilidad de uso y potencia como Python. Para muchos desarrolladores desde principiantes hasta expertos, trabajar con Python no solo es productivo, si no tambien una experiencia realmente agradable. Una de las mejores cosas que tiene este lenguaje de programacion es lo facil que resulta empezar. Su sintaxis es clara casi como leer inglés, lo que permite enfocarse en la lógica sin perderse en reglas complicadas. Por ejemplo, imprimir un mensaje en pantalla toma solo una línea, lo que genera una sensación inmediata de logro. Esto hace que la primera experiencia con Python sea motivadora: en pocos minutos puedes escribir programas funcionales. Python cuenta con una comunidad global enorme. Esto significa que casi cualquier problema que encuentres ya ha sido resuelto por alguien más. Además, sus librerías hacen que tareas complejas sean mucho más simples Pandas (para datos) NumPy (para cálculos) Flask o Django (para web). Python también permite experimentar. Puedes crear desde bots hasta aplicaciones completas, pasando por análisis de datos o incluso proyectos de inteligencia artificial. La libertad que ofrece hace que programar no se sienta como una obligación, sino como una actividad creativa...", "autor": "Leonardo Zapa"},
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "<h1>Post Not Found</h1>", 404

if __name__ == '__main__':
    app.run()
