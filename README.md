# Parte Prática - Prova 1
## Cecília Gio Alonso Gonçalves

## Descrição
Esse repositório contém o deselvolvimento da parte prática da prova 1 Módulo 5. O objetivo final da questão é projeto Web implementado com o micro framework Flask em Python, que siga expecificações citadas no enunciado. 

## Pré-requisitos
**Python 3 instalado**
**Clonar o repositório**

## Guia de Instalação (Windows, através do terminal)
Na janela do terminal digite os seguintes comandos para cada dependência

**Criando Ambiente Virtual**

```python -m venv venv```
```venv\Scripts\activate```

**Instalar as dependências necessárias**

- flask 
```pip install flask```
- tinydb
```pip install tinydb```
- requirements.txt
```pip install -r requirements.txt```
```pip freeze > requirements.txt```

**Para executar a aplicação**
```python -m flask --app src\prova-web\app.py run --host 0.0.0.0 --port 8000```

**Descricão dos Arquivos**
