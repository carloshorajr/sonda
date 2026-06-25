# Arquitetura da Sonda

## Objetivo

A Sonda é uma plataforma de monitoramento remoto desenvolvida para coletar, armazenar e apresentar informações sobre conectividade, desempenho e disponibilidade de dispositivos instalados em campo.

O projeto foi concebido para operar de forma modular, permitindo a adição de novos coletores e novas funcionalidades sem necessidade de alterações estruturais na aplicação.

A arquitetura foi baseada na separação de responsabilidades, onde cada componente possui uma função única e bem definida.

O sistema é executado em contêiner Docker utilizando Python, Flask e uma interface web moderna para administração local da sonda.

## Princípios Arquiteturais

A arquitetura da Sonda segue os seguintes princípios:

- Separação de responsabilidades.
- Serviços independentes.
- Backend desacoplado da interface.
- Interface baseada em páginas e APIs REST.
- Toda interação com o sistema operacional ocorre através da camada de serviços.
- Nenhuma página acessa diretamente o sistema operacional.
- Toda lógica de negócio permanece concentrada na camada de serviços.
- O frontend possui apenas responsabilidades de apresentação.

## Estrutura do Projeto

A estrutura do projeto foi organizada de forma modular, separando claramente a interface, a lógica da aplicação, os serviços, os coletores e a infraestrutura necessária para execução da Sonda.

```
sonda/
│
├── backend/
│   ├── collectors/
│   ├── database/
│   ├── routes/
│   ├── services/
│   ├── __init__.py
│   └── app.py
│
├── data/
│
├── docker/
│
├── docs/
│
├── frontend/
│   ├── static/
│   └── templates/
│
├── scripts/
│
├── systemd/
│
├── requirements.txt
├── README.md
└── LICENSE
```

### backend

Contém toda a lógica da aplicação.

É responsável por:

- Rotas Flask;
- Serviços;
- APIs;
- Coletores;
- Comunicação com o sistema operacional.

### frontend

Responsável exclusivamente pela interface web.

Contém:

- Templates HTML;
- CSS;
- JavaScript;
- Recursos estáticos.

O frontend não possui lógica de negócio.

### services

Camada responsável por toda a lógica da aplicação.

Nenhuma rota deverá acessar diretamente o sistema operacional.

Toda comunicação deverá ocorrer através de um Service.

### collectors

Responsável pelos módulos de coleta de dados da Sonda.

Cada coletor deverá possuir responsabilidade única.

Exemplos:

- Wi-Fi;
- Gateway;
- DNS;
- Internet;
- Energia;
- Temperatura;
- Futuros sensores.

### data

Armazena todos os dados produzidos pela Sonda.

Exemplos:

- CSV;
- SQLite;
- Arquivos temporários;
- Logs.

### docker

Arquivos responsáveis pela construção e execução do ambiente de desenvolvimento.

### docs

Documentação técnica do projeto.

### scripts

Scripts auxiliares utilizados durante instalação, manutenção ou migração.

### systemd

Arquivos responsáveis pela integração da Sonda com o sistema operacional.

## Arquitetura da Aplicação

A aplicação está organizada em camadas.

```
Usuário

↓

Interface Web (Frontend)

↓

Flask (Routes)

↓

Services

↓

Sistema Operacional
```

Cada camada possui responsabilidades bem definidas e comunicação unidirecional.

As páginas nunca acessam diretamente o sistema operacional.

Toda interação ocorre através da camada de serviços.

## Serviços

Cada domínio da aplicação deverá possuir um Service específico.

Nenhum Service deverá assumir responsabilidades pertencentes a outro domínio.

### SystemService

Responsável pelas informações gerais da Sonda.

Exemplos:

- Hostname;
- CPU;
- Memória;
- Disco;
- Uptime.

### NetworkService

Responsável pela administração da conectividade.

Exemplos:

- Interfaces;
- Ethernet;
- Wi-Fi;
- SSID;
- Gateway;
- DNS;
- Scan de redes;
- Conexões;
- Perfis de rede.

### MetricsService

Responsável pela leitura e consolidação das métricas coletadas.

Exemplos:

- CSV;
- Banco de dados;
- Estatísticas;
- Dados para gráficos.

### EventService

Responsável pelo gerenciamento de eventos.

Exemplos:

- Timeline;
- Alarmes;
- Histórico;
- Exportação.

Novos serviços poderão ser adicionados conforme a evolução do projeto.

## Fluxo da Aplicação

Toda requisição deverá seguir obrigatoriamente o fluxo abaixo.

```
Browser

↓

Flask Route

↓

Service

↓

Sistema Operacional

↓

Service

↓

Template HTML

↓

Browser
```

Nenhuma camada poderá ignorar esse fluxo.

## Convenções de Desenvolvimento

Toda nova funcionalidade deverá seguir os princípios abaixo.

### Rotas

As rotas possuem apenas responsabilidade de:

- receber a requisição;
- chamar os serviços necessários;
- encaminhar os dados ao template.

### Services

Os Services concentram toda a lógica da aplicação.

Um Service nunca deverá:

- gerar HTML;
- acessar templates;
- manipular CSS;
- manipular JavaScript.

### Frontend

O frontend possui apenas responsabilidades de apresentação.

Toda informação deverá ser fornecida pelo backend.

### Templates

Templates nunca deverão conter lógica de negócio.

Seu único objetivo é apresentar os dados recebidos.

## Evolução da Arquitetura

Este documento deverá ser atualizado sempre que houver alterações estruturais na aplicação.

Toda nova camada, serviço ou componente deverá ser documentado antes de sua implementação definitiva.

Este documento é considerado a principal referência arquitetural do projeto.