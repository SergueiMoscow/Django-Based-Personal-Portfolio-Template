import yaml
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from portfolio.models import PortfolioConfig

class Command(BaseCommand):
    help = 'Initialize portfolio configuration from user_setup.yaml'

    def handle(self, *args, **kwargs):
        setup_file = settings.BASE_DIR / 'user_setup.yaml'
        if not setup_file.exists():
            self.stdout.write(self.style.ERROR('user_setup.yaml not found! Please create it based on user_setup_example.yaml'))
            return

        with setup_file.open('r') as f:
            config = yaml.safe_load(f)

        if not config or 'portfolio_config' not in config:
            self.stdout.write(self.style.ERROR('Invalid user_setup.yaml format!'))
            return

        for block, items in config['portfolio_config'].items():
            for key, value in items.items():
                if isinstance(value, list):
                    value = json.dumps(value)
                PortfolioConfig.objects.update_or_create(
                    block=block,
                    key=key,
                    defaults={'value': str(value)}
                )
                self.stdout.write(self.style.SUCCESS(f'Added/Updated {block}: {key} = {value}'))

        self.stdout.write(self.style.SUCCESS('Portfolio configuration initialized successfully!'))