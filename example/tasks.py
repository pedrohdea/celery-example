import re
import time

from celery import current_app, Task
from celery.contrib import rdb
from loguru import logger


@current_app.task(queue='hello')
def ola_mundo():
    time.sleep(3)
    logger.success('log: olá mundo')
    return 'olá mundo'


@current_app.task(queue='matematica')
def vezes_quatro(x):
    time.sleep(1)
    resultado = x * 4
    logger.success(f'vezes_quatro = {resultado}')
    return resultado


@current_app.task(queue='matematica')
def mais_y(x, y):
    time.sleep(1)
    resultado = x + y
    logger.success(f'mais_y = {resultado}')
    return resultado


@current_app.task(bind=True, queue='mail')
def task_validar_email(self: Task, email):
    try:
        logger.info('validando e-mail...')
        validado = re.match(
            r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$', email
        )
        if not validado:
            raise ValueError('e-mail inválido')
    except Exception as exc:
        if self.request.retries == self.max_retries:
            logger.warning('e-mail invalido')

        raise self.retry(exc=exc, countdown=5)


# https://docs.celeryq.dev/en/stable/userguide/tasks.html#task-inheritance
class MyTask(Task):
    autoretry_for = (Exception,)
    max_retries = 3
    default_retry_delay = 5
    retry_backoff = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.critical('on failure')
        return super().on_failure(exc, task_id, args, kwargs, einfo)


@current_app.task(queue='mail', base=MyTask)
def task_enviar_email(email: str):
    logger.info(f'e-mail recebido {email}')
    time.sleep(1)
    logger.warning('Implemente envio de e-mail')
    raise NotImplementedError('Implemente envio de e-mail')


# https://docs.celeryq.dev/en/main/userguide/debugging.html


@current_app.task(bind=True, queue='mail')
def task_testar_email(self, email):
    logger.info(f'e-mail recebido {email}')
    rdb.set_trace()
