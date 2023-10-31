# celery-example

Exemplo de arquitetura Celery.

Exemplos didáticos para a Python Brasil 2023, com o intuito de demonstrar como as filas e tarefas assíncronas funcionam, e formas de implementá-las.

## Aula de base do Dunossauro

<div style="display:flex;flex-direction:row">
<a title="Live de Python #159 - Celery" width="854" height="480" href="https://www.youtube.com/embed/ig9hbt-yKkM" ><img src="https://i.ytimg.com/vi/ig9hbt-yKkM/maxresdefault.jpg"></img></a>
</div>

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
