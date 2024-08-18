import pandas as pd
from data import creator
from pathlib import Path

ROOT_DIR = Path(__file__)

# CSS
LOCAL_CSS = ROOT_DIR.parent.parent / "assets" / "css" / "styles.css"

# CSV's
LOCAL_TRANSACTIONS = creator.LOCAL_TRANSACTIONS
LOCAL_CATEGORIES = creator.LOCAL_CATEGORIES
LOCAL_ACCOUNTS = creator.LOCAL_ACCOUNTS
LOCAL_CREDIT_CARDS = creator.LOCAL_CREDIT_CARDS

# Função para ler o arquivo CSS
def local_css():
    with open(LOCAL_CSS) as f:
        return f'<style>{f.read()}</style>'
    
# Carrega transações
def local_transactions():
    df = pd.read_csv(LOCAL_TRANSACTIONS, sep=";")
    return df

# Carrega categorias
def local_categories():
    df = pd.read_csv(LOCAL_CATEGORIES, sep=";")
    return df

# Carrega contas
def local_accounts():
    df = pd.read_csv(LOCAL_ACCOUNTS, sep=";")
    return df

# Carrega cartões de crédito
def local_credit_cards():
    df = pd.read_csv(LOCAL_CREDIT_CARDS, sep=";")
    return df

# Carrega exemplo de transações
def example_transactions():
    # Gerando dados fictícios para entradas e despesas mensais
    categorias = ['Salário', 'Freelance', 'Investimentos', 'Presentes', 'Outros']
    entradas = [4000, 1500, 800, 200, 300]
    despesas = [1000, 500, 200, 150, 100]

    # Expandindo os dados para múltiplos meses
    datas = pd.date_range(start='2023-01-01', periods=6, freq='ME')
    data_expanded = {
        'Data': [],
        'Categoria': [],
        'Tipo': [],
        'Valor': []
    }

    for data in datas:
        for i, categoria in enumerate(categorias):
            data_expanded['Data'].append(data)
            data_expanded['Categoria'].append(categoria)
            data_expanded['Tipo'].append('Entradas')
            data_expanded['Valor'].append(entradas[i])
            data_expanded['Data'].append(data)
            data_expanded['Categoria'].append(categoria)
            data_expanded['Tipo'].append('Despesas')
            data_expanded['Valor'].append(despesas[i])

    # Criação do DataFrame
    df = pd.DataFrame(data_expanded)
    return df
