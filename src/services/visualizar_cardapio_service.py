class VisualizarCardapioService:

      products = {
            "1" : {
                  "Titulo" : "X-Burguer",
                  "Preco" : "1000",
                  "Preparo" : "20"
            },

            "2" : {
                  "Titulo" : "Batata Frita",
                  "Preco" : "500",
                  "Preparo" : "10"
            },

            "3" : {
                  "Titulo" : "Refrigerante",
                  "Preco" : "200",
                  "Preparo" : "5"
            }
      }

      def view_menu(self):
            print("\n" + "┌" + "─"*44 + "┐")
                  
            for product in self.products:
                  print(f"│{product} {self.products[product]["Titulo"]} ----- R${self.products[product]["Preco"][:2]}")

            print("└" + "─"*44 + "┘\n")
