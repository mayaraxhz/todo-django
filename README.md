Integrante: Mayara Evelyn Nunes

Visão geral do sistema AcheIF:
Sistema de gerenciamento de achados e perdidos 

O sistema será responsável por gerenciar os achados e perdidos do IFRN, incluindo o controle de objetos, e terá apenas um nível de usuário, chamado administrador. 
Os registros e devoluções de objetos serão registrados, permitindo o controle de cada item, desde o momento em que é encontrado até sua devolução ao dono. O sistema possibilitará o acesso à informações detalhadas sobre os objetos cadastrados, devolvidos ou não. 
O sistema deverá oferecer uma maneira simples de consultar os objetos perdidos, com acesso ao local em que foram encontrados, tipo de objeto e status (devolvido ou não). Somente o administrador terá acesso ao sistema, podendo realizar o cadastro de novos objetos, editar etc. 
Este sistema deverá cobrir as necessidades do setor de achados e perdidos do IFRN, garantindo mais organização, praticidade e controle na gestão dos objetos perdidos.


### Passos para instalação

1. **Clone o repositório**

```bash
git clone https://github.com/mayaraxhz/todo-django.git
```

2. **Crie um ambiente virtual**

```bash
python -m venv venv
```

3. **Ative o ambiente virtual**

```bash
venv\Scripts\activate
```

4. **Instale as dependências do projeto**

```bash
pip install django
```

5. **Execute as migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Inicie o servidor**

```bash
python manage.py runserver
```

Agora, o sistema estará disponível em `http://localhost:8000`.