from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import json
from .models import Article
from .serializers import *
from .serializer import *
from django.http import JsonResponse


def index(req):
    data = pd.read_csv('data/fahras.csv')
    df = pd.DataFrame(data)
    result = df.to_json(orient='records')
    parsed = json.loads(result)
    #json_list = json.loads(json.dumps(list(DataFrame.T.to_dict().values())))
    #return JsonResponse(json.dumps(parsed),safe=False)
    return JsonResponse(parsed,safe=False)

class ArticleView(APIView):
    def get(self,req):
        data = pd.read_csv('data/births.csv')
        data = pd.DataFrame(data)
        result = data.to_json(orient="split")
        parsed = json.loads(result)

        return json.dumps(parsed, indent=4)

    def get_data(self, request, pk=None):
        if pk:
            article = get_object_or_404(Article.objects.all(), pk=pk)
            serializer = ArticleSerializer(article)
            return Response({"article": serializer.data})
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})


    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
