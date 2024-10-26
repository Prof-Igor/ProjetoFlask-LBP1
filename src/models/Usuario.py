from hashlib import sha256

class Usuario:
    def __init__(self, id, nome, senha, tipo = 0) -> None:
        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__tipo = tipo
    
    def __getattribute__(self, name):
        return super().__getattribute__(f"_Usuario__{name}")
        
listUsuarios = []
listUsuarios.append(Usuario(1, "Igor", sha256("1234".encode()).hexdigest()))
listUsuarios.append(Usuario(2, "Aluno", sha256("1234".encode()).hexdigest(), 1))