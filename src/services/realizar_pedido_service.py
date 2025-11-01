class RealizarPedidoService:
    next_id = 0
    def __init__(self, titulo: str, preco: str, preparo: str):
        self.titulo = titulo
        self.preco = preco
        self.preparo = preparo
        next_id += 1
        self.orders = {}

    def take_order(self):
        self.orders = {
            self.next_id : {
                "Titulo" : {[]},
                "Preco" : {[]},
                "Preparo" : {[]}
            }
        }

    def view_order(self):
        for order in self.orders:
            print(order)