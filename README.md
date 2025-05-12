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
|João Victor Romagnoli Vendito | Ciência da Computação  | Programação Orientada a Objetos em JAVA                           |
|João Paulo da Silva Júnior    | Ciência da Computação  | Programação Orientada a Objetos em JAVA                           |

**Professor Orientador:** Kesede Rodrigues Junior

---

## 1. Introdução 💡

O cliente identificou dificuldades no controle e organização das encomendas de doces, como anotações manuais, esquecimentos de pedidos e falta de acompanhamento eficaz. Para solucionar isso, será desenvolvido um sistema web de gerenciamento de pedidos que permita registrar, acompanhar e organizar as encomendas de forma centralizada. As tecnologias utilizadas... 

---

## 2. Objetivo 📌

Criar um site dinâmico e eficiente para o gerenciamento de encomendas de doces, atendendo às necessidades tanto dos clientes quanto dos proprietários do negócio. A plataforma será um ambiente digital, onde os usuários poderão realizar encomendas de doces personalizados com facilidade e praticidade, enquanto o proprietário terá controle total sobre os pedidos, o estoque e o fluxo de trabalho.

---

## 3. Escopo 🎯

### Funcionalidades para Clientes
- **Cadastro e Login:** Autenticação segura para clientes.
- **Catálogo de Produtos:** Visualização de doces disponíveis com descrição e preços.
- **Carrinho de Compras:** Gerenciamento de itens adicionados ao carrinho.
- **Finalização de Pedidos:** Confirmação de compra e cálculo do total com resumo do pedido.
- **Rastreamento de Pedidos:** Status do pedido (ex.: "em preparo" ou "entregue").

### Funcionalidades para Administradores (Confeiteiros)
- **Login Administrativo:** Acesso seguro ao painel de controle.
- **Gerenciamento de Produtos:** Adicionar, editar ou remover doces no catálogo.
- **Visualização de Pedidos:** Lista de pedidos feitos pelos clientes com detalhamento.
- **Atualização de Status:** Controle do progresso do pedido.

---

## Tecnologias e Ferramentas
- **Linguagem de Programação:** Python.
- **Framework:** Flask (para construir o back-end e estruturar o site).
- **Banco de Dados:** SQLite (leve e integrado, perfeito para começar).
- **ORM:** SQLAlchemy (orientação a objetos para interação com o banco de dados).
- **Hospedagem:** PythonAnywhere (fácil de configurar e mantém o projeto na nuvem).

---

## Estrutura do Banco de Dados

### Tabelas principais
1. **Clientes**
   - `id`: Chave primária, único.
   - `nome`: Nome do cliente.
   - `email`: Email do cliente.
   - `senha`: Hash para segurança.

2. **Produtos**
   - `id`: Chave primária, único.
   - `nome`: Nome do produto.
   - `descrição`: Descrição detalhada do doce.
   - `preco`: Preço unitário.
   - `quantidade_disponível`: Estoque disponível.

3. **Pedidos**
   - `id`: Chave primária, único.
   - `id_cliente`: Chave estrangeira para a tabela de clientes.
   - `id_produto`: Chave estrangeira para a tabela de produtos.
   - `quantidade`: Quantidade do produto.
   - `preco_total`: Preço total do pedido.
   - `status`: Status do pedido (ex.: "em preparo", "pronto", "entregue").

---

## Fluxo de Desenvolvimento

### Fase 1: Planejamento
- Mapear os requisitos detalhados (ex.: número de páginas, funcionalidades adicionais).
- Criar protótipos simples do layout e fluxo.

### Fase 2: Desenvolvimento
1. **Configuração do ambiente**
   - Criar o projeto Flask e instalar dependências (Flask, SQLAlchemy, Flask-WTF, etc.).
   - Configurar o banco de dados SQLite.

2. **Implementação**
   - Criar as classes Python (ex.: Cliente, Produto, Pedido) e mapear com SQLAlchemy.
   - Desenvolver rotas Flask (ex.: `/novo_pedido`, `/listar_produtos`).
   - Utilizar templates HTML e CSS para o front-end.

### Fase 3: Testes
- Validar o sistema de login e segurança.
- Testar rotas, funcionalidades e integração com banco de dados.
- Garantir que o design seja responsivo.

### Fase 4: Implantação
- Configurar o projeto no PythonAnywhere.
- Realizar testes de produção para confirmar funcionalidade.

### Fase 5: Feedback e Ajustes
- Coletar opiniões de usuários e confeiteiros.
- Corrigir erros e implementar melhorias conforme necessário.

---

## Resultados Esperados
- Um sistema funcional e intuitivo.
- Gestão eficiente de pedidos de doces e catálogo de produtos.
- Escalabilidade para adicionar novas funcionalidades no futuro.

## 4. Backlogs do Produto 📋

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

## 🗓️ Cronograma do Projeto

| Etapa               | Descrição                             | Data de Início | Data de Término | Status     |
|---------------------|----------------------------------------|----------------|------------------|------------|
| Planejamento        | Mapear requisitos detalhados  | 14/04/2025 | 28/04/2025      | ✅ Concluída  |
| Desenvolvimento              | Criar as classes Python, desenvolver rotas Flask      | 24/04/2025     | 15/05/2025    | 🚧 Em andamento |
| Desenvolvimento              | Utilizar Templates HTML e CSS para o front-end     | 24/04/2025     | 15/05/2025    | 🚧 Em andamento |
| Design   | Criar Layout e fluxo do site     | 24/04/2025    | 15/05/2025     | 🚧 Em andamento |
| Testes              |  Validar sistema de login e segurança, testar rotas, funcionalidades e integração com banco de dados, garantir que o design seja responsivo         | 30/04/2025     | 15/05/2025      | 🚧 Em andamento |
|  |           |     |         |                                                                                   |
|          |   |   |     | |


---


## 6. Materiais e Métodos  🧰

### Modelagem do Sistema
- Diagrama de Casos de Uso
![Diagrama de Casos de Uso](docs/diagrama.casos.uso.png)

- Diagrama de Classes
![Diagrama de Classes](docs/diagrama.classes.png)

### Tecnologias Utilizadas
- **Python + Flask**: Backend
- **HTML/CSS/JS**: Interface do usuário
- **SQLite/**: Banco de dados
- **SQLAlchemy/**: orientação a objetos
- **PythonAnywhere/**: hospedagem do site
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
![Linkedin.png](https://github.com/unimetrocamp-startupclass/LTD.2025.1.028-CHOCOMEIRE/blob/main/Linkedin.png)
www.linkedin.com/in/chocomeire-ltda-2a1a60360

### Seminário de Projetos de Software
- Link do vídeo: 
- Fotos e legendas da apresentação
- Lista de presença

### FENETEC
- Link do vídeo da apresentação
- Fotos e legendas
- Lista de visitantes com nome e emai

---

## 11. Carta de Apresentação ✉️

Vimos por meio desta apresentar o grupo de acadêmicos do **Centro Universitário Unimetrocamp**, localizado na **Av. Sales de Oliveira, 1661 - Campinas - SP**, a fim de convidá-lo a participar de uma atividade extensionista associada ao componente curricular **ARA0075 - Programação Orientada à Objeto**, sob responsabilidade do(a) orientador(a) **Prof. Kesede Rodrigues Julio**.

Em consonância ao **Plano Nacional de Educação**, o **Centro Universitário Unimetrocamp** desenvolve o **Desenvolvimento de Software**, que, norteado pela metodologia da **Engenharia de Software**, tem por princípios:
- Diagnóstico dos problemas/demandas/necessidades;
- Participação ativa dos interessados/públicos participantes;
- Construção dialógica, coletiva e experiencial de conhecimentos;
- Planejamento de ações;
- Desenvolvimento e avaliação das ações;
- Sistematização dos conhecimentos.

Nesse contexto, a disciplina mencionada tem como escopo:
- Levantamento de requisitos;
- Planejamento dos modelos;
- Codificação dos modelos;
- Testes dos códigos;
- Homologação do MVP.

Solicitamos o apoio da **Chocomeire** para a realização das seguintes atividades:
- Diagnósticos através de reuniões agendadas;
- Análises feitas pelos integrantes do time de desenvolvimento;
- Levantamento de requisitos por meio de reuniões agendadas (online ou presencial);
- Desenvolvimento de projeto utilizando **Metodologia Ágil Scrum**;
- Mentorias com o professor da disciplina;
- Pesquisas em documentações, repositórios e plataformas de IA.

### Formalização:
Em caso de aceite, solicitamos a assinatura da **Carta de Autorização**, formalizando as atividades e informações que o(s) aluno(s) poderá(ão) ter acesso.

### Fórum de Acompanhamento:
Registramos também o convite para o **fórum semestral de acompanhamento e avaliação das atividades realizadas**, que será comunicado previamente em convite específico.

Desde já, nos colocamos à disposição para quaisquer esclarecimentos.

**Local:** Campinas, 17 de Abril de 2025  
**Assinatura:** Direção Acadêmica da IES  
**Assinatura:** Docente


---

## 12. Carta de Autorização ✍️


Eu, **Edimeire Bezerra Romagnoli**, Confeiteira da Chocomeire, autorizo a realização das seguintes atividades acadêmicas do componente extensionista **ARA0075 - Programação Orientada à Objeto**, do **Centro Universitário Unimetrocamp**, sob orientação do(a) **Prof. Kesede Rodrigues Julio**:

### Atividades Autorizadas:
- Realização de um site para gerenciamento de encomendas de doces.

#### Alunos Autorizados:
| Nome                          | Curso                   | Matrícula     |
|--------------------------------|-------------------------|--------------|
| João Victor Romagnoli Vendito  | Ciência da Computação   | 202402531425 |
| João Paulo da Silva Júnior     | Ciência da Computação   | 202402531409 |

Declaro que fui informado por meio da Carta de Apresentação sobre as características e objetivos das atividades que serão realizadas na organização/instituição/empresa a qual represento e afirmo estar ciente de tratar-se de uma atividade realizada com intuito exclusivo de ensino de alunos de graduação, sem a finalidade de exercício profissional.

### Autorizo, em caráter de confidencialidade:
- O acesso a informações e dados necessários à execução da atividade;
- O registro de imagem por meio de fotografias;
- Outro:

**Local:** Campinas, 17 de Abril de 2025  
**Assinatura:** Edimeire Bezerra Romagnoli  


---

## 13. Relato individual do processo 💬

### Nome do aluno 1
Relato individual.

### Nome do aluno 2
Relato individual.

