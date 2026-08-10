# Robot Face

Projeto de renderização e animação facial para um robô social utilizando **Python** e **Pygame**.

O objetivo deste projeto é controlar as expressões faciais, animações e sincronização labial (visemes) de um robô contador de histórias. A arquitetura foi desenvolvida para permitir a futura integração com ROS 2.

---

# Funcionalidades atuais

Atualmente o projeto possui:

- Renderização da face em tempo real utilizando Pygame.
- Expressões faciais pré-definidas.
- Piscada automática.
- Animação das sobrancelhas.
- Animação automática da fala utilizando visemes.
- Ajuste individual da posição dos visemes `I` e `U`.
- Sistema de poses independentes das animações das sobrancelhas.
- Estrutura preparada para modos de animação (como o modo dormir).

---

# Estrutura do projeto

```text
robot_face/
│
├── assets/
│   ├── face/
│   ├── eyes/
│   ├── eyebrows/
│   └── mouth/
│       ├── emotions/
│       └── visemes/
│
├── asset_manager.py
├── animator.py
├── expressions.py
├── face_state.py
├── layout.py
├── renderer.py
└── test_renderer.py
```

---

# Dependências

É necessário possuir:

- Python 3
- Pygame

## Instalação

```bash
pip install pygame
```

---

# Executando

Dentro da pasta do projeto execute:

```bash
python3 test_renderer.py
```

Uma janela será aberta contendo a face do robô.

---

# Controles do teclado

## Expressões

| Tecla | Expressão |
| ------ | --------- |
| N | Normal |
| H | Feliz |
| J | Feliz piscando |
| S | Triste |
| A | Assustado |
| B | Bravo |

---

## Visemes

Utilizados apenas para testes.

| Tecla | Viseme |
| ------ | ------- |
| 1 | A |
| 2 | E |
| 3 | I |
| 4 | O |
| 5 | U |

---

## Animação de fala

| Tecla | Função |
| ------ | ------ |
| T | Inicia animação automática da fala |
| Espaço | Para a animação da fala |

---

## Modo dormir

Atualmente em desenvolvimento.

| Tecla | Função |
| ------ | ------ |
| D | Entrar no modo dormir |
| W | Acordar |

---

# Arquitetura

O projeto é dividido em módulos independentes.

## AssetManager

Responsável por carregar todos os assets da aplicação.

Carrega:

- Face
- Olhos
- Sobrancelhas
- Boca
- Visemes

---

## FaceState

Armazena o estado atual do rosto.

Controla:

- Expressão dos olhos
- Expressão das sobrancelhas
- Expressão da boca
- Viseme atual
- Posição base das sobrancelhas
- Animação das sobrancelhas

---

## Renderer

Responsável por desenhar todos os elementos da face na tela.

A ordem de renderização é:

1. Face
2. Sobrancelhas
3. Olhos
4. Boca

---

## Animator

Controla todas as animações.

Atualmente implementa:

- Piscada automática
- Animação da fala
- Animação das sobrancelhas
- Estrutura para modos de animação

---

## Expressions

Arquivo utilizado para armazenar combinações de expressões.

Exemplo:

```python
HAPPY = (
    "happy",
    "normal",
    "happy"
)
```

Isso permite reutilizar facilmente cada expressão em todo o projeto.

---

# Personalização

As posições dos elementos podem ser alteradas em:

```text
layout.py
```

É possível ajustar:

- Posição dos olhos
- Posição das sobrancelhas
- Posição da boca
- Posição dos visemes

Os visemes `I` e `U` possuem posições independentes.

---

# Assets

Todos os arquivos PNG permanecem independentes.

As expressões são geradas através da combinação dinâmica dos elementos, permitindo criar novas emoções sem alterar os arquivos originais.

---

# Próximos passos

Planejados para as próximas versões:

- Modo dormir completo.
- Sequência de bocejo.
- Animação de acordar.
- Novas expressões faciais.
- Movimento dos olhos.
- Mais animações das sobrancelhas.
- Integração com ROS 2.
- Integração com sintetizador de voz.
- Sincronização automática dos visemes com a fala.
- Controle das expressões através de tópicos ROS 2.

---

# Objetivo

Este projeto faz parte do desenvolvimento de um robô social voltado para interação com crianças.

O objetivo é fornecer uma arquitetura modular para controlar expressões faciais, animações e sincronização labial, facilitando a integração com sistemas de diálogo, síntese de voz e ROS 2.
