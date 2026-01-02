from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health_check():
    """
    Простой эндпоинт для проверки работы сервера.
    Возвращает JSON с приветствием и статусом.
    """
    return jsonify({
        "message": "Hops-server (Rhino/Grasshopper compatible) is running!",
        "status": "OK",
        "version": "1.0"
    })


@app.route("/solve", methods=["GET"])
def solve_example():
    """
    Пример эндпоинта, который мог бы принимать параметры от Grasshopper.
    Сейчас просто возвращает тестовый результат.
    """
    return jsonify({
        "result": "Test computation completed",
        "input_received": None,
        "output": 42.0
    })


if __name__ == "__main__":
    # Запуск на 0.0.0.0 для доступности извне (Docker/локально)
    app.run(host="0.0.0.0", port=5000, debug=True)