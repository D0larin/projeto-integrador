# Documentação

* Compreenda o projeto.
* Escolha uma tarefa.
* Configure seu ambiente.
* Faça um fork do repositório.
* Desenvolva sua contribuição e faça testes.
* Submeta um pull request explicativo.
* Revise e ajuste conforme o feedback.
* Mantenha-se envolvido.

## Instruções de deploy

Para fazer o deploy de um projeto web Python e Django, é necessário configurar o ambiente de produção, gerenciar dependências, coletar arquivos estáticos e configurar servidores web e de banco de dados. Testes, monitoramento e medidas de segurança são vitais, assim como planejar a escalabilidade e manter atualizações regulares.

Sugestões de serviços de hospedagem para pesquisar:
* Vercell
* PythonAnywhere
* AWS Elastic Beanstalk (não recomendamos o uso deste serviço sem supervisão, pois pode gerar cobranças inesperadas)

## Modelagem de banco de dados

Esse Projeto Contêm 4 Bancos de dados :
* Pessoa(login) -> É um banco de dados responsável por armazenar apenas dados de cadastro para login
* Professor -> É o banco de dados responsável por armazenar o dado do nome dos Professores
* Aluno -> É o banco de dados responsável por armazenar os dados dos nomes dos professores e dos alunos 
* Sala -> é um banco de dados responsável por armazear dados do número das salas 
