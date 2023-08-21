from pyramid.config import Configurator
from pyramid.response import Response

def home(request):
    return Response("""
        <html>
        <head>
            <title>Wilfred Lai - Portfolio</title>
            <link rel="stylesheet" href="static/style.css">
        </head>
        <body>
            <header>
                <img src="static/wilfred.png" alt="Wilfred Lai">
                <h1>Wilfred Lai</h1>
                <p>Finalist Student, BSc in Mathematics and Computer Science</p>
            </header>
            
            <!-- ... Rest of your content ... -->
            
            <footer>
                <p>Contact me at: wilfredayiekolai@gmail.com</p>
            </footer>
        </body>
        </html>
    """)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    config.add_static_view(name='static', path='strm:static')  # Change this line
    app = config.make_wsgi_app()
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
