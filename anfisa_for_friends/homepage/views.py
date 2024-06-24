from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Возьмём нужное. А ненужное не возьмём:
    ice_cream_list = IceCream.objects.values(
            'id', 'title', 'description'
            # Верни те объекты, у которых в поле is_on_main True:
        ).filter(is_on_main=True, is_published=True)
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
