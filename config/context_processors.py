import os


def export_vars(request):
    data = {}
    data['PRODUCT_NAME'] = os.environ.get("PRODUCT_NAME")
    data['COMPANY_NAME'] = os.environ.get("COMPANY_NAME")
    return data
