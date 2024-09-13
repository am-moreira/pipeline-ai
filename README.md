# Pipeline Gen AI - ETL com API e CRM de Vendas
Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) para um CRM de vendas utilizando diversas tecnologias de ponta, incluindo Python, Streamlit, PostgreSQL, OpenAI, Langchain, MKDocs, Pydantic, Git, SQLAlchemy, psycopg2 e dotenv.

### Tecnologias Utilizadas
* **Python:** Linguagem principal do projeto.
* **Streamlit:** Framework para construção de aplicações web de forma simples e rápida.
* **PostgreSQL:** Banco de dados relacional para armazenamento das informações de vendas.
    * **SQLAlchemy:** ORM para interação com o banco de dados PostgreSQL.
    * **psycopg2:** Driver para conectar e executar queries no PostgreSQL.
* **OpenAI:** Integração com a API da OpenAI para gerar respostas inteligentes.
* **Langchain:** Framework para trabalhar com grandes modelos de linguagem.
* **MKDocs:** Ferramenta para documentação do projeto.
* **Pydantic:** Validação de dados através de classes de modelos no Python.
* **Git:** Controle de versão do código.
* **dotenv:** Gerenciamento de variáveis de ambiente de forma segura.

### Funcionalidades
* **ETL (Extração, Transformação e Carga):** Implementa o pipeline completo para extrair dados de diferentes fontes, transformá-los e carregá-los no banco de dados.
* **Integração com API:** Uso de APIs externas para coletar e processar dados.
* **Integração com CRM:** Ferramentas para auxiliar na gestão de vendas, com armazenamento seguro no PostgreSQL.
* **Interface Web com Streamlit:** Visualização e gerenciamento do pipeline através de uma interface simples e interativa.
* **Integração com OpenAI:** Respostas inteligentes e automação de tarefas com a API da OpenAI.
* **Documentação com MKDocs:** Documentação completa do projeto com MKDocs, facilitando o entendimento e a colaboração.

### Estrutura do Projeto

    ├── .venv/                # Ambiente virtual do Python
    ├── app.py                # Aplicação principal em Streamlit
    ├── contrato.py           # Módulo de gerenciamento de contratos
    ├── database.py           # Configurações do banco de dados com SQLAlchemy
    ├── docs/                 # Documentação com MKDocs
    ├── .gitignore            # Arquivos e pastas ignorados pelo Git
    ├── requirements.txt      # Dependências do projeto
    ├── mkdocs.yml            # Configuração do MKDocs
    └── README.md             # Documentação do projeto

### Como Rodar o Projeto

Clone o repositório:

```
git clone https://github.com/am-moreira/pipeline-ai.git
```

Ative o ambiente virtual:

~~~
source .venv/Scripts/activate  # No Linux
.venv\Scripts\activate  # No Windows
~~~

Instale as dependências:

~~~
pip install -r requirements.txt
~~~

Configure as variáveis de ambiente no arquivo .env:

```
DB_HOST=localhost
DB_NAME=db
DB_USER=usuario
DB_PASS=senha
```

Execute a aplicação:

~~~
streamlit run app.py
~~~

### Contribuições
Sinta-se à vontade para contribuir com o projeto. Basta abrir uma issue ou enviar um pull request.