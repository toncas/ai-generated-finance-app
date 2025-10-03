"""
Celery configuration
"""
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

app = Celery('personal_finance_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Schedule
app.conf.beat_schedule = {
    'process-recurring-transactions': {
        'task': 'apps.transactions.tasks.process_recurring_transactions',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
    },
    'check-budget-alerts': {
        'task': 'apps.budgets.tasks.check_budget_alerts',
        'schedule': crontab(hour='*/6'),  # Every 6 hours
    },
}
