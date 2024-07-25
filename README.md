# **🎮 Título do Projeto**

## 👥 Equipe
- **Andreywid Souza** - ayls@cin.ufpe.br
- **Jadiael Gadelha** - jgfl@cin.ufpe.br
- **João Victor Lopes** - jvcl@cin.ufpe.br
- **Mário Daniel** - mdtsf@cin.ufpe.br
- **Victor Diniz** - vpd@cin.ufpe.br

---

## 1. 📖 Visão Geral

### 1.1. Descrição
Uma breve descrição do projeto, explicando o objetivo do jogo e as principais funcionalidades.

---

## 2. 🛠 Arquitetura do Projeto

### 2.1. Estrutura de Diretórios
(exemplos)

```plaintext
├── assets/
│   ├── images/
│   ├── sounds/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── settings.py
│   ├── player.py
│   ├── enemy.py
│   ├── game.py
├── README.md
├── requirements.txt
```

### 2.2. Descrição dos Arquivos
(exemplos)
- **main.py**: Ponto de entrada do jogo.
- **settings.py**: Configurações globais do jogo (e.g., tamanho da tela, FPS).
- **player.py**: Classe Player, que gerencia as ações do jogador.
- **enemy.py**: Classe Enemy, que gerencia os comportamentos dos inimigos.
- **game.py**: Classe Game, que integra todos os componentes e gerencia o loop principal do jogo.
- **assets/**: Contém todos os recursos do jogo, como imagens e sons.

## 3. 📸 Capturas de Tela

### 3.1. Tela Inicial
![Tela Inicial](assets/screenshots/tela_inicial.png)

### 3.2. Gameplay
![Gameplay](assets/screenshots/gameplay.png)

## 4. 🛠 Ferramentas, Bibliotecas e Frameworks

### 4.1. Ferramentas Utilizadas
- **Python**: Linguagem de programação utilizada para desenvolvimento.
- **Pygame**: Biblioteca utilizada para criação de jogos 2D.

### 4.2. Justificativas
- **Python**: Escolha baseada na sua simplicidade e na relevância para iniciantes em programação.
- **Pygame**: Popularidade e facilidade de uso para desenvolvimento de jogos simples.

## 5. 🧑‍💻 Divisão de Trabalho

### 5.1. Tarefas e Responsáveis
- **Nome do Membro 1**: 'Andreywid Souza'
- **Nome do Membro 2**: 'Jadiael Gadelha'
- **Nome do Membro 3**: 'João Victor Lopes'
- **Nome do Membro 4**: 'Mário Teles'
- **Nome do Membro 5**: 'Victor Diniz'

## 6. 🧠 Conceitos Utilizados

### 6.1. Programação Orientada a Objetos (OOP)
- **Classes e Objetos**: Implementação das classes `Player`, `Enemy` e `Game`.
- **Herança**: Se aplicável, mencione onde foi usada.

### 6.2. Estruturas de Dados
- **Listas**: Utilizadas para gerenciar múltiplos inimigos.
- **Dicionários**: Se aplicável, descreva seu uso.

### 6.3. Tratamento de Eventos
- **Eventos do Pygame**: Controle de entradas do usuário e eventos do jogo.

## 7. 🚧 Desafios e Lições Aprendidas

### 7.1. Desafios Enfrentados 
(exemplos)

#### 7.1.1. Maior Erro Cometido
- **Erro**: Inicialmente, não organizamos bem a estrutura do projeto.
- **Solução**: Reestruturamos o projeto, separando responsabilidades em diferentes módulos.

#### 7.1.2. Maior Desafio Enfrentado
- **Desafio**: Implementação de colisões entre o jogador e os inimigos.
- **Solução**: Estudamos a documentação do Pygame e aplicamos testes iterativos para ajustar a lógica.

### 7.2. Lições Aprendidas
- **Planejamento**: A importância de planejar a estrutura do projeto antes de começar a programar.
- **Trabalho em Equipe**: Como trabalhar em equipe, dividindo tarefas e integrando diferentes partes do código.
- **Conhecimento Técnico**: Melhor entendimento de Pygame e dos conceitos de OOP.

# Guidelines de Contribuição

## Mensagens de Commit

Utilizamos uma convenção que fornece um conjunto de regras para formular uma estrutura de mensagem de commit consistente da seguinte forma:

```
<type>[optional scope]: <description>

[optional body]
```

O tipo do commit pode ser:

- `feat` – uma nova funcionalidade é introduzida com as mudanças.
- `fix` – ocorreu uma correção de bug.
- `refactor` – código refatorado que não corrige um bug nem adiciona uma funcionalidade.
- `docs` – atualizações na documentação, como o README ou outros arquivos markdown.
- `style` – mudanças que não afetam o significado do código, provavelmente relacionadas à formatação do código, como espaços em branco, pontos e vírgulas ausentes, e assim por diante.

A linha de assunto do tipo de commit deve ser toda em letras minúsculas com um limite de 75 caracteres. Além disso, o corpo opcional do commit deve ser usado para fornecer mais detalhes que não cabem nas limitações de caracteres da descrição da linha de assunto.

## Criação de Branches

Uma branch do git deve começar com uma categoria. Escolha uma destas: `feature`, `bugfix`, ou `test`.

- `feature` é para adicionar, refatorar ou remover uma funcionalidade.
- `bugfix` é para corrigir um bug.
- `test` é para experimentação.

Após a categoria, deve haver um "/" seguido por uma descrição que resume o propósito desta branch específica. Esta descrição deve ser curta e em `kebab-case`. Para resumir, siga este padrão ao criar branches:

```
git branch <category/description-in-kebab-case>
```

Exemplos:

- Você precisa adicionar, refatorar ou remover uma funcionalidade: `git branch feature/create-new-button-component`
- Você precisa corrigir um bug: `git branch bugfix/button-overlap-form-on-mobile`
- Você precisa experimentar algo: `git branch test/refactor-components-with-atomic-design`


