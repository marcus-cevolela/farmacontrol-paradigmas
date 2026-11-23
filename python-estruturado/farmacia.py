# paradigma estruturado
import os

# define cada categoria e seu estoque minimo
CATEGORIAS = [
    {"codigo": 1, "nome": "Venda livre", "quantidade_minima": 10},
    {"codigo": 2, "nome": "Antibiótico", "quantidade_minima": 5},
    {"codigo": 3, "nome": "Controlado", "quantidade_minima": 3},
]

# define o estoque inicial de medicamentos
estoque = [
    {"codigo": 1, "nome": "Dipirona", "categoria": 1, "preco": 5.00, "quantidade": 20},
    {"codigo": 2, "nome": "Amoxicilina", "categoria": 2, "preco": 25.00, "quantidade": 10},
    {"codigo": 3, "nome": "Clonazepam", "categoria": 3, "preco": 15.00, "quantidade": 2},
]

# busca a categoria pelo codigo e retorna o dicionario dela
def buscar_categoria(codigo):
    for categoria in CATEGORIAS:
        if categoria["codigo"] == codigo:
            return categoria
    return None

# lista o estoque
def listar():
    # verifica se o estoque está vazio
    if len(estoque) == 0:
        print("Estoque vazio.")
        return

    # percorre cada item do estoque 
    for medicamento in estoque:
        cat = buscar_categoria(medicamento["categoria"])

        print(f"Código: {medicamento['codigo']} | Nome: {medicamento['nome']} | Categoria: {cat['nome']} | Preço: R$ {medicamento['preco']:.2f} | Quantidade: {medicamento['quantidade']}")

        if medicamento["quantidade"] < cat["quantidade_minima"]:
            print(" ⚠ ATENÇÃO: Estoque abaixo do mínimo!")
