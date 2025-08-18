from portfolio.models import PortfolioConfig
import json

def portfolio_config(request):
    config = {}
    for item in PortfolioConfig.objects.all():
        if item.block not in config:
            config[item.block] = {}
        try:
            config[item.block][item.key] = json.loads(item.value)
        except json.JSONDecodeError:
            config[item.block][item.key] = item.value
    return {'portfolio': config}