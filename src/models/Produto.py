class Produto:
    def __init__(self, id, nome, imagem, preco) -> None:
        self.__id = id
        self.__nome = nome
        self.__imagem = imagem
        self.__preco = preco
    
    def __getattribute__(self, name):
        return super().__getattribute__(f"_Produto__{name}")
        
listProdutos = []
listProdutos.append(Produto(1, "Headset JBL Tune 520BT", "jbl", 239.00))
listProdutos.append(Produto(2, "Apple AirPods (3ª geração)​​​​​​​", "apple", 1405.98))
listProdutos.append(Produto(3, "Samsung Galaxy Buds3", "samsung", 1249.00))
listProdutos.append(Produto(4, "Headset Gamer Sem Fio Logitech G733", "logitech", 986.43))
listProdutos.append(Produto(5, "Headset Sony WH-1000XM5", "sony", 2310.00))
listProdutos.append(Produto(6, "Headset sem fio PULSE Elite", "playstation", 884.99))