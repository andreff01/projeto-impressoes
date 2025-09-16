# Sistema de Gerenciamento de Impressões

Este projeto é um sistema web desenvolvido em Django para gerenciar solicitações de impressão feitas por professores, com administração centralizada e controle de tarefas manuais.

## Objetivo
Facilitar o envio, acompanhamento e controle de impressões acadêmicas, otimizando o fluxo entre professores, bolsistas e administradores.

## Funcionalidades
- Cadastro e login de usuários (professor e administrador)
- Envio de solicitações de impressão com opções (frente/verso, grampear, tipo de impressão)
- Upload de arquivos para impressão
- Painel do professor: acompanhamento dos pedidos
- Painel do administrador: controle de todas as impressões, tarefas manuais (grampear/envelopar), relatórios
- Notificações por e-mail (a implementar)
- Relatórios de tarefas pendentes e totais

## Estrutura do Projeto
- `usuarios/`: gerenciamento de usuários e autenticação
- `impressoes/`: envio e controle de impressões
- `config/`: configurações globais do Django
- `templates/`: templates HTML base e específicos

## Como rodar o projeto
1. Clone o repositório:
   ```
   git clone https://github.com/andreff01/projeto-impressoes.git
   cd projeto-impressoes
   ```
2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```
   pip install django
   ```
4. Execute as migrações:
   ```
   python manage.py migrate
   ```
5. Crie um superusuário (opcional):
   ```
   python manage.py createsuperuser
   ```
6. Inicie o servidor:
   ```
   python manage.py runserver
   ```
7. Acesse em [http://localhost:8000](http://localhost:8000)

## Protótipo Visual
O protótipo das telas foi desenvolvido em ferramenta digital e está disponível nos slides de apresentação.

## Modelo Lógico
O diagrama do banco de dados está disponível na documentação e nos slides.

## Autores
André Ferreira Farias e Larisse Pessoa Reis

---
Projeto acadêmico de P.I - 2025
