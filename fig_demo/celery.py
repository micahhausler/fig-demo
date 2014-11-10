from __future__ import absolute_import
import logging
import os
from celery import Celery, Task

LOG = logging.getLogger(__name__)


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fig_demo.settings')

project_celery = Celery('fig_demo', task_cls='fig_demo.celery:FigDemoTask')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
project_celery.config_from_object('django.conf:settings')
project_celery.conf.update(
    CELERY_IMPORTS=[
        'fig_demo.apps.page.tasks',
    ]
)


class FigDemoTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Error handler.

        This is run by the worker when the task fails.

        :param exc: The exception raised by the task.
        :param task_id: Unique id of the failed task.
        :param args: Original arguments for the task that failed.
        :param kwargs: Original keyword arguments for the task
                       that failed.

        :keyword einfo: :class:`~billiard.einfo.ExceptionInfo`
                        instance, containing the traceback.

        The return value of this handler is ignored.

        """
        LOG.error(exc)
        LOG.error(einfo)
