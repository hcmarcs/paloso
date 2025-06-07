from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def em_breve():
    return render_template_string('''
    <html>
        <head>
            <title>Em Breve</title>
            <style>
                body {
                    background-color: #b2d8b2;
                    color: white;
                    font-weight: bold;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-size: 2em;
                    font-family: Arial, sans-serif;
                }
            </style>
        </head>
        <body>
            EM BREVE ...
        </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
