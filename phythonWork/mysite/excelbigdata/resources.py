from import_export import resources
from .models import ExcelData, ExcelDataSomExe

class ExcelDataResource(resources.ModelResource):
    class meta:
        model = ExcelData

class ExcelDataSomExeResource(resources.ModelResource):
    class meta:
        model = ExcelDataSomExe