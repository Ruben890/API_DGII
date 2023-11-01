from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RNC_Serializer
from ..models import RNC
from ..src.main import main
from rest_framework.filters import SearchFilter  
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class UpdateRNCDataFromCSV(APIView):
    """
    API view for updating RNC data from a CSV file.
    """
    def get(self, request):
        """
        Execute the main function to update RNC data from a CSV file.

        :param request: The HTTP request object.
        :return: Response indicating the update status.
        """
        main()  # Asegúrate de que la función main acepte un argumento con la ruta del archivo si es necesario

        # Return a response with a success message
        return Response({'message': 'RNC data has been updated from the source.'}, status=status.HTTP_200_OK)




class CustomPagination(PageNumberPagination):
    page_size = 10  # Adjust this value to your desired page size
    page_size_query_param = 'page_size'
    max_page_size = 100

class Views(viewsets.ModelViewSet):
    serializer_class = RNC_Serializer
    queryset = RNC.objects.all()
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['rnc', 'nombre_apellido']
    