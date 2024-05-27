from flask import Flask, request, render_template, jsonify
from route import Route

app = Flask(__name__)


class Distribution:
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f"Distribution:\n{self.content}"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    response = {}

    # Обработка маршрутов
    routes_text = request.json.get('routes_text', None)
    if routes_text:
        routes_file_path = 'routes_input.txt'
        with open(routes_file_path, 'w', encoding='utf-8') as file:
            file.write(routes_text)
        routes = Route.from_file(routes_file_path)
        response['routes_output'] = "\n\n".join(str(route) for route in routes)
    else:
        response['routes_output'] = "No routes text provided."

    # Обработка распределения
    distribution_text = request.json.get('distribution_text', None)
    if distribution_text:
        distribution = Distribution(distribution_text)
        response['distribution_output'] = str(distribution)
    else:
        response['distribution_output'] = "No distribution text provided."

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
