# Bubble Sort con pruebas unitarias

Implementación orientada a objetos de Bubble Sort en Python. El método ordena
una lista de enteros de forma ascendente y modifica la lista original.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Cobertura

```bash
python -m coverage run --branch --source=src -m unittest discover -s tests
python -m coverage report -m
python -m coverage html
```
