<h1 align="center"><strong>Kenzie Commerce API</strong></h1>
<br/>

## **Descrição**

>Este projeto consiste em uma API construída em Python com o objetivo de suportar uma plataforma de e-commerce com diferentes níveis de acesso. A plataforma tem como principal objetivo permitir que os usuários possam buscar, comprar e vender produtos.

>A API foi desenvolvida utilizando o framework Django e conta com recursos como autenticação de usuários, validação de dados, acesso a banco de dados e gerenciamento de rotas.

<br>
<br>

## **Instalação**

Para instalar as dependências necessárias para rodar a API, siga os passos abaixo:

1. Clone este repositório em seu computador.
2. Crie um ambiente virtual para instalar as dependências do projeto.

```bash
python -m venv venv
```

3. Ative o ambiente virtual.

No Linux:
```bash
source venv/bin/activate
```

No Windows:
```bash
.\venv\Scripts\activate
```

4. Com o ambiente virtual ativado, instale as dependências do projeto.
```bash
pip install -r requirements.txt
```

5. Crie um arquivo .env com as mesmas variáveis do arquivo .env.example para realizar as configurações do banco de dados.

<br>

### **ATENÇÃO:**

Os nomes das variáveis precisam ser iguais aos exemplos do arquivo .env.example.

<br>

6. Para criar as tabelas no banco de dados, rode o seguinte comando no terminal:

```bash
python manage.py migrate
```

<br>

## **Uso**
Para iniciar a aplicação, execute o seguinte comando no terminal:

```bash
python manage.py runserver
```

<br>

A API estará rodando em http://localhost:8000/.

Para visualizar todos os endpoints da aplicação, acesse o link abaixo:

http://localhost:8000/api/docs/swagger-ui/

A API também está disponível online, onde você pode visualizar também todos os endpoints da aplicação nesse link abaixo: 

https://kenzie-commerce-api.onrender.com/api/docs/swagger-ui/

