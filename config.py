from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições de diferentes origens (Cross-Origin Resource Sharing)


class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor


class LivroAPI:
    def __init__(self):
        self.livros = []
        self.livro_id_counter = 0

    # Listar todos os livros
    def listar_livros(self):
        return jsonify([livro.__dict__ for livro in self.livros]), 200

    # Obter detalhes de um livro específico
    def obter_livro(self, livro_id):
        livro = next((livro for livro in self.livros if livro.id == livro_id), None)
        if livro:
            return jsonify(livro.__dict__), 200
        else:
            return jsonify({'mensagem': 'Livro não encontrado'}), 404

    # Adicionar um novo livro
    def adicionar_livro(self, data):
        novo_livro = Livro(
            id=self.livro_id_counter + 1,
            titulo=data['titulo'],
            autor=data['autor']
        )
        self.livros.append(novo_livro)
        self.livro_id_counter += 1
        return jsonify(novo_livro.__dict__), 201

    # Atualizar detalhes de um livro
    def atualizar_livro(self, livro_id, data):
        livro = next((livro for livro in self.livros if livro.id == livro_id), None)
        if livro:
            livro.titulo = data.get('titulo', livro.titulo)
            livro.autor = data.get('autor', livro.autor)
            return jsonify(livro.__dict__), 200
        else:
            return jsonify({'mensagem': 'Livro não encontrado'}), 404

    # Remover um livro
    def remover_livro(self, livro_id):
        self.livros = [livro for livro in self.livros if livro.id != livro_id]
        return jsonify({'mensagem': 'Livro removido'}), 200


livro_api = LivroAPI()


# Definindo os endpoints da API

@app.route('/livros', methods=['GET'])
def listar_livros():
    return livro_api.listar_livros()


@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    return livro_api.obter_livro(livro_id)


@app.route('/livros', methods=['POST'])
def adicionar_livro():
    data = request.get_json()
    return livro_api.adicionar_livro(data)


@app.route('/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    data = request.get_json()
    return livro_api.atualizar_livro(livro_id, data)


@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def remover_livro(livro_id):
    return livro_api.remover_livro(livro_id)


# Rodar a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
