# SIAPESQ

# Flask Login and Registration

Este é um exemplo básico de um aplicativo Flask que implementa funcionalidades de login e registro de usuários.

## Pré-requisitos

Certifique-se de ter o Python e o Flask instalados em seu ambiente de desenvolvimento, caso não tenha siga as instruções a baixo:

## Instalação

1. Clone este repositório em seu ambiente local:

    ```
    git clone <[(https://github.com/Iahnke/SIAPESQ.git)>
    
    ```
1.1 Abra a pasta onde os arquivos estão localizados e clique com o botão direito dentro dela. Em seguida, selecione a opção 'Abrir no Terminal.

2. Instale as dependências necessárias no Windows PowerShell:

    ```
    pip install pipenv
    pipenv install flask flask-login flask-sqlalchemy
    pipenv shell
    pipenvinstall mysqlclient
    
    ```
# Agora no seu editor de código:

1. Abra o arquivo `app.py` e edite a URL do banco de dados, se necessário:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    ```

2. Execute o seguinte comando no terminal para criar o banco de dados:

    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Executando o Aplicativo

Para executar o aplicativo, execute o seguinte comando no terminal:

```
python app.py
```

O aplicativo estará acessível em `http://localhost:5000`.

## Funcionalidades

- **Página Inicial (/)**: Página inicial do aplicativo.
- **Registro de Usuário (/register)**: Página para registrar novos usuários.
- **Login (/login)**: Página para autenticar usuários existentes.
- **Logout (/logout)**: Rota para fazer logout do usuário atual.

## Contribuindo

Sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull request com melhorias para este aplicativo.

---
