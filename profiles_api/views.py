from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API Views """

    def get(self, request, format=None):
        """Returns a list of api view functions"""
        an_apiview = [
            'Uses HTTP methods as funtion (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over application logic',
            'Is mapped manuallly to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
