import time

from celery import Task, chain
from loguru import logger

from example.tasks import ola_mundo, vezes_quatro, mais_y, task_enviar_email, task_validar_email
ola_mundo: Task
vezes_quatro: Task
mais_y: Task
task_enviar_email: Task
task_validar_email: Task

email = 'pedrohassumpcao@gmail.com'

task_validar_email.delay(*[email])
task_enviar_email.apply_async(email=email)

# ola_foi_feito = ola_mundo.delay()
# logger.success(ola_foi_feito)

# time.sleep(2)

# ola_mundo.apply_async()
# ola_mundo.apply_async()
# ola_mundo.apply_async()
# ola_mundo.apply_async()

# time.sleep(2)

# chain(vezes_quatro.s(1), mais_y.s(2))()
