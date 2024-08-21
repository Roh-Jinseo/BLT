from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment, Like, CommentLike

'''
게시물 파트
'''

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 생각해보니 애초에 작성자가 아니면 삭제버튼이 나타나지 않으니 조건문 필요없음
        # if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'PUT':
        print(request.data)
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    

# 게시물 좋아요 파트

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    like, created = Like.objects.get_or_create(user=user, article=article)

    if created:
        article.likes_count += 1
        article.save()
        return Response({'message': 'Liked'}, status=status.HTTP_201_CREATED)
    else:
        like.delete()
        article.likes_count -= 1
        article.save()
        return Response({'message': 'Unliked'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_if_liked(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    is_liked = Like.objects.filter(user=user, article=article).exists()
    return Response({'is_liked': is_liked}, status=status.HTTP_200_OK)
'''
댓글 파트
'''

@api_view(['GET', 'DELETE', 'PUT'])
def comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == comment.author:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'사용자만 삭제가 가능합니다.'})
    elif request.method == 'PUT':
        if request.user == comment.author:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'사용자만 수정이 가능합니다.'})


@api_view(['GET'])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()  # 해당 게시물의 모든 댓글 가져오기
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message':'왜 안되냐ㅏ'})


# 댓글 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    like, created = CommentLike.objects.get_or_create(user=user, comment=comment)
    if not created:
        like.delete()
        comment.likes_count -= 1
        comment.save()
        return Response({'message': '좋아요 취소'}, status=status.HTTP_204_NO_CONTENT)
    comment.likes_count += 1
    comment.save()
    return Response({'message': '좋아요'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    is_liked = CommentLike.objects.filter(user=user, comment=comment).exists()
    return Response({'is_liked': is_liked}, status=status.HTTP_200_OK)