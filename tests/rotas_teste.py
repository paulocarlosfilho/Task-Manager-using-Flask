import pytest
from todo_project import app, db, bcrypt
from todo_project.models import User, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

### Testando as rotas

def teste_about_page(client):
    resposta = client.get('/about')
    assert resposta.status_code == 200
    assert b'About' in resposta.data

def teste_home_page(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
    assert b'About' in resposta.data #Verificando se o abaut está na página

def teste_login_page(client):
    #Teste de Login
    resposta = client.get('/login')
    assert resposta.status_code == 200
    assert b'Login' in resposta.data

def teste_register_page(client):
    #Teste do pagina resister_page
    resposta = client.get('/register')
    assert resposta.status_code == 200
    assert b'Register' in resposta.data

def test_all_tasks_page_redirects_when_not_logged_in(client):
    #Teste para verificar se a pagina all_task redireciona a pessoa caso não esteja logado
    resposta = client.get('/all_tasks', follow_redirects=True)
    assert resposta.status_code == 200
    assert b'Please log in' in resposta.data  # Verifica se há uma mensagem de login na página