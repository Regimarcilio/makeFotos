# makeFotos
Script para agrupamento de fotos em página A4

# Agrupar Fotos A4

Ferramenta desenvolvida em Python para organizar automaticamente múltiplas imagens em páginas A4 de alta resolução, permitindo a geração de layouts para impressão fotográfica, catálogos, portfólios e composições gráficas.

O sistema realiza o redimensionamento proporcional das imagens, aplica recorte central quando necessário e distribui as fotos em grades configuráveis, gerando páginas prontas para impressão em qualidade profissional.

## Recursos

* Seleção de imagens através do explorador de arquivos do sistema operacional.
* Suporte aos formatos JPG, JPEG, PNG e WEBP.
* Distribuição automática das fotos em páginas A4.
* Redimensionamento com preservação de proporção.
* Recorte central automático para preenchimento uniforme.
* Geração automática de múltiplas páginas conforme a quantidade de imagens selecionadas.
* Configuração da quantidade de fotos por linha e coluna.
* Exportação em alta qualidade para impressão.
* Compatibilidade com Windows, Linux e macOS.

## Tecnologias Utilizadas

* Python 3
* Pillow (PIL)
* Tkinter

## Estrutura do Projeto

```text
agrupar-fotos/
│
├── makeFotos.py
├── requirements.txt
├── README.md
└── output/
```

## Requisitos

* Python 3.10 ou superior
* Pillow

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/agrupar-fotos.git
```

Acesse o diretório do projeto:

```bash
cd agrupar-fotos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Caso utilize apenas o Pillow:

```bash
pip install pillow
```

## Execução

Execute o script:

```bash
python makeFotos.py
```

Ao iniciar:

1. Será aberta uma janela para seleção das imagens.
2. Escolha as fotos desejadas.
3. Selecione a pasta onde os arquivos gerados serão salvos.
4. O sistema processará automaticamente todas as imagens.
5. As páginas A4 serão exportadas em formato JPG.

## Configuração do Layout

No início do arquivo é possível ajustar os parâmetros principais:

```python
PHOTOS_PER_ROW = 2
PHOTOS_PER_COLUMN = 2

MARGIN = 80
SPACING = 30
```

### Exemplos

| Layout | Fotos por Página |
| ------ | ---------------- |
| 2 x 2  | 4                |
| 3 x 2  | 6                |
| 3 x 3  | 9                |
| 4 x 3  | 12               |
| 5 x 4  | 20               |

O sistema calcula automaticamente:

* Quantidade de páginas necessárias.
* Dimensões das fotos.
* Posicionamento dos elementos.
* Distribuição das imagens.

## Qualidade de Impressão

O projeto utiliza:

```python
PAGE_WIDTH = 2480
PAGE_HEIGHT = 3508
```

Correspondente ao formato A4 em 300 DPI, adequado para impressão de alta qualidade.

O redimensionamento é realizado utilizando o filtro:

```python
Image.LANCZOS
```

que oferece excelente preservação de detalhes durante o processamento.

## Fluxo de Processamento

```text
Selecionar Fotos
        │
        ▼
Selecionar Pasta de Saída
        │
        ▼
Calcular Layout
        │
        ▼
Redimensionar Imagens
        │
        ▼
Aplicar Recorte Central
        │
        ▼
Distribuir nas Páginas
        │
        ▼
Exportar Arquivos
```

## Possíveis Evoluções

* Exportação direta para PDF multipágina.
* Interface gráfica completa.
* Pré-visualização das páginas.
* Templates personalizáveis.
* Suporte a formatos de impressão adicionais.
* Inserção de bordas e molduras.
* Numeração automática das páginas.
* Marca d'água configurável.

## Licença

Este projeto está disponível sob a licença MIT.

## Autor

Desenvolvido por Reginaldo Marcilio.

GitHub: https://github.com/seu-usuario
LinkedIn: https://linkedin.com/in/seu-perfil

