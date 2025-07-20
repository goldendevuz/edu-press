from django_filters import rest_framework as filters
from django_filters import CharFilter
from django.db import models
from .models import ArticleCategory, Article


# Field types we allow for filtering
FILTERABLE_FIELD_TYPES = (
    models.BooleanField,
    # models.DateField,
    # models.DateTimeField,
    models.IntegerField,
    models.FloatField,
    models.DecimalField,
    models.CharField,  # but only if it has choices
)

def is_filterable_field(field: models.Field) -> bool:
    if isinstance(field, FILTERABLE_FIELD_TYPES):
        if isinstance(field, models.CharField) and not field.choices:
            return False  # exclude plain CharFields without choices
        return True
    return False

def get_filterable_fields(model):
    """
    Returns a dict of field names -> ['exact'] for all safe fields to filter.
    """
    return {
        field.name: ['exact']
        for field in model._meta.get_fields()
        if isinstance(field, models.Field) and is_filterable_field(field)
    }


class BaseAutoFilterSet(filters.FilterSet):
    class Meta:
        abstract = True
        filter_overrides = {
            models.ImageField: {
                'filter_class': CharFilter,
                'extra': lambda f: {'lookup_expr': 'exact'},
            }
        }


class ArticleFilter(BaseAutoFilterSet):
    class Meta(BaseAutoFilterSet.Meta):
        model = Article
        fields = get_filterable_fields(Article)