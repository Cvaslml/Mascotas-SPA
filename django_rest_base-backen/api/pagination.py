from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    """
    Clase de paginación personalizada para definir el tamaño de página por defecto,
    el parámetro para modificarlo y el tamaño máximo permitido.
    """
    page_size = 10  # Tamaño de página por defecto
    page_size_query_param = 'page_size'  # Parámetro para que el cliente pueda cambiar el tamaño
    max_page_size = 100  # Tamaño máximo permitido por página
    page_query_param = 'page'  # Parámetro para el número de página
