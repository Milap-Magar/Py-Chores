from import_export import resources
from .models import Questions

class QuestionResources(resources.ModelResource):
    class Meta:
        model = Questions