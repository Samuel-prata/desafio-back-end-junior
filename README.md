<h1 style='text-align:center'>Projeto Escola</h1>

![Django Rest](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Sobre o projeto
Este repositório contém o código-fonte para um **Sistema de Matrículas para Cursos.**

## Endpoints criados

### Courses
- **/courses/:** Retorna todos os cursos
![get-courses](./images-docs/get-courses.png)

- **/courses/new:** Adiciona mais um curso ao banco de dados
![new-course](./images-docs/new-course.png)

- **/courses/int:course_id/students/:** Retorna os dados dos estudantes matriculados em um curso

### Students
- **/students/:** Retorna os dados dos alunos
![get-students](./images-docs/get-students.png)
- **/students/uuid:student_id/:** Retorna os dados de um usuário especifíco 
![detail-student](./images-docs/detail-student.png)
- **/students/register:** Registro um novo estudante
![register-student](./images-docs/register-student.png)

### Enrollments
- **/enrollments/**: Retorna todas as matriculas
- **/enrollments/do-enrollment:** Realiza a matricula de um aluno em um curso
![do-enrollment](./images-docs/do-enrollment.png)

### Documentação
- **/swagger:** Gera a interface da documentação do Swagger
- **/redoc:** Gera a documentação mais leve

## Generics
Apesar das rotas estarem definidas, há a possibilidade de testes diretos com o Generics através dos endpoints:

- **/courses/test_generics/:** GET e POST para adicionar um novo curso
- **/students/test_generics/:** GET e POST para adicionar um novo estudante
- **/enrollments/test_generics:** GET e POST para fazer uma matricula


## Banco de dados
O banco de dados utilizado é o PostgreSQL. Iniciado com um imagem docker e suas configurações HardCoded. (Redução de complexidade), portanto, para ter acesso ao banco de dados com algum editor, utilize as credenciais inicializadas no docker-compose.

### Diagrama
![Diagrama do Banco de dados](./images-docs/School_diagram.png)




## Como rodar
Vamos rodar a aplicação a partir do Docker-compose, portanto, certifique-se de o ter instalado.

As demais configurações como Variáveis para conexão do banco de dados e Variaveis para execução de imagens estão como hardcoded (Definidas no docker-compose) excluindo a necessidade de criar um arquivo .env e configurá-lo.

Faça um clone desse repositório através do comando:

```bash
git clone [URL_REPO]
```

E execute o comando:

```bash
docker-compose up -d
```

No navegador ou postman, faça requisições para o dominio:
```
http://localhost:8000/[URLS DEFINIDAS]
```