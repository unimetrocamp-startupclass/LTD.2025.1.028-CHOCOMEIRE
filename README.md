# Documentação do Sistema

## SUMÁRIO
- [Dados do Cliente](#dados-do-cliente)
- [Equipe de Desenvolvimento](#equipe-de-desenvolvimento)
- [1. Introdução](#1-introdução)
- [2. Objetivo](#2-objetivo)
- [3. Escopo](#3-escopo)
- [4. Backlogs do Produto](#4-backlogs-do-produto)
- [5. Cronograma](#5-cronograma)
- [6. Materiais e Métodos](#6-materiais-e-métodos)
- [7. Resultados](#7-resultados)
- [8. Conclusão](#8-conclusão)
- [9. Homologação do MVP junto ao cliente](#9-homologação-do-mvp-junto-ao-cliente)
- [10. Divulgação](#10-divulgação)
- [11. Carta de Apresentação](#11-carta-de-apresentação)
- [12. Carta de Autorização](#12-carta-de-autorização)
- [13. Relato individual do processo](#13-relato-individual-do-processo)

---

## Dados do Cliente

**Título do Projeto:** Chocomeire - Um site para gerenciamento de encomendas de doces

**Cliente:** Edimeire Bezerra Romagnoli

**CNPJ/CPF:**  51.609.434/0001-24

**Contato:** (19) 99456-4187

**Email do contato:** meire_venditoo@hotmail.com

---

## Equipe de Desenvolvimento

| Nome completo       | Curso              | Disciplina                 |
|---------------------|--------------------|----------------------------|
|João Victor Romagnoli Vendito | Ciência da Computação  | Programação Orientada a Objetos em JAVA                            |
|João Paulo da Silva Júnior    | Ciência da Computação  | Programação Orientada a Objetos em JAVA                           |
|                     |                    |                            |
|                     |                    |                            |

**Professor Orientador:** Kesede Rodrigues Junior

---

## 1. Introdução 💡

O cliente identificou dificuldades no controle e organização das encomendas de doces, como anotações manuais, esquecimentos de pedidos e falta de acompanhamento eficaz. Para solucionar isso, será desenvolvido um sistema web de gerenciamento de pedidos que permita registrar, acompanhar e organizar as encomendas de forma centralizada. As tecnologias utilizadas... 

---

## 2. Objetivo 📌

Criar um site dinâmico e eficiente para o gerenciamento de encomendas de doces, atendendo às necessidades tanto dos clientes quanto dos proprietários do negócio. A plataforma será um ambiente digital, onde os usuários poderão realizar encomendas de doces personalizados com facilidade e praticidade, enquanto o proprietário terá controle total sobre os pedidos, o estoque e o fluxo de trabalho.

---

## 3. Escopo 🎯

O sistema permitirá:
- Cadastro de pedidos com data, tipo de doce e status.
- Visualização e edição dos pedidos.

Não serão implementadas:
- Integração com meios de pagamento.
- Sistema de entrega.

(OBS: Com o decorrer do projeto pode ser feito alterações nas implementações!)

---

## 4. Backlogs do Produto 📋

# Backlog do Projeto CHOCOMEIRE

## 1. Configuração Inicial
### Épico: Configuração do Ambiente
- **Tarefa:** Criar o repositório do projeto.
- **Tarefa:** Configurar o ambiente Flask.
  - *Subtarefa:* Instalar Flask, SQLAlchemy e outras dependências.
  - *Subtarefa:* Configurar SQLite como banco de dados local.
- **Tarefa:** Criar estrutura básica de diretórios (ex.: templates, static, models).

## 2. Desenvolvimento do Back-end
### Épico: Implementação das Classes e Banco de Dados
- **Tarefa:** Criar classe `Cliente` com SQLAlchemy.
- **Tarefa:** Criar classe `Produto` com SQLAlchemy.
- **Tarefa:** Criar classe `Pedido` com SQLAlchemy.
  - *Subtarefa:* Configurar tabelas e chaves primárias/estrangeiras.
- **Tarefa:** Implementar métodos específicos nas classes (ex.: cálculo do total do pedido).

### Épico: Desenvolvimento das Rotas Flask
- **Tarefa:** Criar rota `/cadastro_cliente`.
- **Tarefa:** Criar rota `/login_cliente`.
- **Tarefa:** Criar rota `/listar_produtos`.
- **Tarefa:** Criar rota `/novo_pedido`.
- **Tarefa:** Criar rota `/atualizar_status_pedido`.

## 3. Desenvolvimento do Front-end
### Épico: Design Responsivo
- **Tarefa:** Criar layout básico usando Bootstrap/Tailwind CSS.
  - *Subtarefa:* Design da página inicial.
  - *Subtarefa:* Design da página de catálogo de produtos.
  - *Subtarefa:* Design da página de carrinho de compras.

### Épico: Integração Front-end com Back-end
- **Tarefa:** Utilizar templates Jinja2 para renderizar dados do back-end.
- **Tarefa:** Implementar formulários HTML para cadastro e login (usando Flask-WTF).

## 4. Funcionalidades Adicionais
### Épico: Implementação de Autenticação
- **Tarefa:** Criar sistema de autenticação com hash de senha (ex.: werkzeug.security).
- **Tarefa:** Implementar validação de sessões para acesso seguro ao site.

### Épico: Carrinho e Pagamento
- **Tarefa:** Implementar funcionalidade de carrinho.
- **Tarefa:** Integrar com APIs de pagamento (opcional).

## 5. Testes e Validação
### Épico: Testes Automatizados
- **Tarefa:** Escrever testes para rotas Flask (ex.: com pytest ou unittest).
- **Tarefa:** Validar a interação do sistema com o banco de dados.

### Épico: Feedback do Usuário
- **Tarefa:** Criar ambiente de testes para coletar sugestões dos clientes/confeiteiros.
- **Tarefa:** Implementar melhorias com base no feedback.

## 6. Implantação
### Épico: Hospedagem e Configuração
- **Tarefa:** Configurar o projeto no PythonAnywhere.
  - *Subtarefa:* Subir o código para o servidor.
  - *Subtarefa:* Configurar o banco de dados remoto SQLite.

### Épico: Monitoramento
- **Tarefa:** Configurar logs no servidor para monitorar erros.
- **Tarefa:** Implementar ferramentas de análise de uso, como Google Analytics.

## 7. Marketing e Expansão
### Épico: Divulgação
- **Tarefa:** Criar contas nas redes sociais para promover o CHOCOMEIRE.
- **Tarefa:** Desenvolver páginas dedicadas para promoções e contato.

---

## 5. Cronograma 📅

(Insira aqui o cronograma em forma de imagem ou tabela com as etapas por quinzena)

---

## 6. Materiais e Métodos  🧰

### Modelagem do Sistema
- Diagrama de Casos de Uso
- MER (Modelo Entidade Relacionamento)

### Tecnologias Utilizadas
- **Python + Flask/Django**: Backend
- **HTML/CSS/JS**: Interface do usuário
- **SQLite/MySQL**: Banco de dados
- **Lucidchart/Draw.io**: Criação dos diagramas

### Arquitetura do Sistema
(Insira aqui uma imagem da arquitetura e descrição do fluxo de dados)

---

## 7. Resultados 📈

### Protótipo
(Insira prints das telas com descrição das funcionalidades)

### Códigos das principais funcionalidades
(Insira trechos do código com comentários explicativos)

---

## 8. Conclusão ☑️

### Impacto do sistema
O sistema digitalizou e otimizou o controle das encomendas, eliminando erros e melhorando a organização.

### Melhorias Futuras
- Inclusão de relatórios de vendas.
- Integração com WhatsApp ou SMS para notificações.

---

## 9. Homologação do MVP junto ao cliente 👥

(Fotos e legendas da apresentação do MVP ao cliente)

(Lista de presença com imagem ou arquivo)

---

## 10. Divulgação 📢 

### LinkedIn do Projeto
(Link para o perfil)

### Seminário de Projetos de Software
- Link do vídeo: 
- Fotos e legendas da apresentação
- Lista de presença

### FENETEC
- Link do vídeo da apresentação
- Fotos e legendas
- Lista de visitantes com nome e email

---

## 11. Carta de Apresentação ✉️

(Trecho institucional de apresentação do projeto e convite à participação do cliente)

---

## 12. Carta de Autorização ✍️

(Declaração de autorização assinada pelo cliente para execução do projeto)

---

## 13. Relato individual do processo 💬

### Nome do aluno 1
Relato individual.

### Nome do aluno 2
Relato individual.

### Nome do aluno 3
Relato individual.

### Nome do aluno 4
Relato individual.

### Nome do aluno 5
Relato individual.

---
