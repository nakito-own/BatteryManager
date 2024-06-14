from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from route import Route
from distribution import Distribution

app = Flask(__name__)
CORS(app)  # Добавляем поддержку CORS

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
        distribution_file_path = 'distribution_input.txt'
        with open(distribution_file_path, 'w', encoding='utf-8') as file:
            file.write(distribution_text)
        distribution = Distribution.from_file(distribution_file_path)
        response['distribution_output'] = str(distribution)
    else:
        response['distribution_output'] = "No distribution text provided."

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
