import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
from tkinter import Tk, filedialog, simpledialog

def carregar_arquivo_csv():
    """Abre uma caixa de diálogo para o usuário escolher um arquivo CSV."""
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    return caminho_arquivo

def salvar_tabela_imagem(df, titulo, nome_arquivo):
    """Cria e salva uma imagem com a tabela fornecida."""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')
    tabela = table(ax, df, loc='center', cellLoc='center', colWidths=[0.2] * len(df.columns))
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(10)
    tabela.scale(1.2, 1.2)
    ax.set_title(titulo, fontsize=14)
    
    # Mostrar a imagem na tela
    plt.show()
    
    # Salvar a imagem
    plt.savefig(nome_arquivo, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

def main():
    print("Selecione o arquivo de estoque:")
    caminho_estoque = carregar_arquivo_csv()
    print("Selecione o arquivo de contas a receber:")
    caminho_devedores = carregar_arquivo_csv()

    if not caminho_estoque or not caminho_devedores:
        print("Erro: Você deve selecionar ambos os arquivos CSV.")
        return

    # Ler dados dos arquivos CSV
    df_estoque = pd.read_csv(caminho_estoque)
    df_devedores = pd.read_csv(caminho_devedores)

    # Perguntar ao usuário os nomes dos arquivos de saída
    nome_arquivo_estoque = simpledialog.askstring("Salvar Tabela", "Nome do arquivo de imagem para a tabela de estoque (com extensão .png):")
    nome_arquivo_devedores = simpledialog.askstring("Salvar Tabela", "Nome do arquivo de imagem para a tabela de devedores (com extensão .png):")

    if not nome_arquivo_estoque or not nome_arquivo_devedores:
        print("Erro: Você deve fornecer nomes para ambos os arquivos de imagem.")
        return

    # Criar e salvar a tabela de estoque
    salvar_tabela_imagem(df_estoque, 'Tabela de Estoque', nome_arquivo_estoque)
    print(f"Tabela de Estoque salva como {nome_arquivo_estoque}")

    # Criar e salvar a tabela de devedores
    salvar_tabela_imagem(df_devedores, 'Tabela de Devedores', nome_arquivo_devedores)
    print(f"Tabela de Devedores salva como {nome_arquivo_devedores}")

if __name__ == "__main__":
    main()
