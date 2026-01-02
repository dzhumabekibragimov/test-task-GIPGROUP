# Тестовое задание — Backend Developer (GIPGROUP)

## Структура проекта
.
├── hops_server/              # Flask-сервер, совместимый с Hops (Rhino/Grasshopper)
├── cuda_benchmark/          # Сравнение CPU vs CUDA
├── documentation_flow/      # Mermaid-диаграмма процесса автоматизации
├── revit_dynamo/            # Dynamo-скрипт для Revit
├── .gitignore
└── README.md


1. Hops-server (Flask)

### Запуск
```bash
cd hops_server
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
Сервер доступен по адресу: http://localhost:5000
Проверка: curl http://localhost:5000/
```

2. Сравнение CPU vs CUDA
Запуск
```Bash
cd cuda_benchmark
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python benchmark.py
Выводит время выполнения матричного умножения на CPU и GPU (если CUDA доступна).
```
3. Dynamo-скрипт для Revit

Файл: revit_dynamo/create_columns_rebar.dyn
Откройте в Dynamo для Revit (рекомендуется шаблон КЖ от Autodesk).
Скрипт создаёт колонны и простое продольное армирование, затем создаёт спецификацию.

4. Mermaid-диаграмма
Файл: documentation_flow/workflow.mmd
Отображается в любом Markdown-редакторе с поддержкой Mermaid (VS Code, GitHub, Obsidian и т.д.).