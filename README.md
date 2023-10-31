# celery-example

Exemplo de arquitetura Celery.

Exemplos didáticos para a Python Brasil 2023, com o intuito de demonstrar como as filas e tarefas assíncronas funcionam, e formas de implementá-las.

### Aula de base do Dunossauro
[![YouTube video player](https://www.youtube.com/embed/ig9hbt-yKkM?si=LHCwnRCt8RJjiNVv)](https://www.youtube.com/embed/ig9hbt-yKkM?si=LHCwnRCt8RJjiNVv)

<div style="display:flex;flex-direction:row">
<iframe width="560" height="315" src="https://www.youtube.com/embed/ig9hbt-yKkM?si=LHCwnRCt8RJjiNVv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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
