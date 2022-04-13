from datetime import datetime
from random import choice
from random import randrange

from choochoo_app.models import Train
from django.views.generic import TemplateView

from .forms import OrderForm


class LoadingView(TemplateView):
    template_name = "loading/loading.html"

    def get_context_data(self, **kwargs):
        context = super(LoadingView, self).get_context_data(**kwargs)  # mostly useless
        data = {
            "id": {
                "time": datetime.now(),
                "materials": [
                    (randrange(1_000_000_000, 10_000_000_000), randrange(1, 100))
                    for _ in range(randrange(20))
                ],
                "name": choice(
                    "Honza Pepa Ivan Vašek Roman Tomáš Radek Hynek Vojta Vítek Kamil".split()
                ),
            }
            for _ in range(10)
        }
        context["data"] = data
        trains_to_load = Train.trains_to_be_loaded()
        data = {}
        for train in trains_to_load:
            data[train.human_id] = train.get_orders()

        return context


class StationView(TemplateView):
    template_name = "station/station.html"

    def get_context_data(self, **kwargs):
        context = super(StationView, self).get_context_data(**kwargs)  # mostly useless
        context["form"] = OrderForm()

        return context
