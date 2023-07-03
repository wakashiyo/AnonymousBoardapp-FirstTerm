from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Comment

# Create your tests here.

class CommentIndexTests(TestCase):
    def test_comment_index(self):
        """
        Comment index のテスト
        """
        response = self.client.get(reverse('comments:index'))
        self.assertEqual(response.status_code, 200)

    def test_comment_show(self):
        """
        Comment の詳細ページ
        """
        comment = Comment.objects.create(
            title="test title",
            body="test body",
            created_at=timezone.now(),
            updated_at=timezone.now())
        url = reverse('comments:show', args=(comment.id,))
        response = self.client.get(url)
        self.assertContains(response, "test title")