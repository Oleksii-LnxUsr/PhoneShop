from .models import Brands


def brands_context(request):
    context_brands = Brands.objects.all()
    return {'context_brands': context_brands}
    