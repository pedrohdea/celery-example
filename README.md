# celery-example

Exemplo de arquitetura Celery.

Exemplos didáticos para a Python Brasil 2023, com o intuito de demonstrar como as filas e tarefas assíncronas funcionam, e formas de implementá-las.

### Para subir o projeto e começar a botar a mão na massa, você precisa de:
- ambiente virtual Python (venv)
- docker e docker-compose

### Comandos para inicar venv

>python3.9 -m venv venv

>. venv/bin/activate

>pip install -r requirements.txt

### Comandos para iniciar o RabbitMQ

>docker compose up --build

### Comando para rodar Flower (monitoramento e gerenciamento)

>. contrib/flower.sh

### Comando para rodar Celery Worker (trabalhador celery)

>. contrib/worker.sh
