from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title = "pickle",
            description = "rick",
            purchaser = self.user,
        )
    def test_content(self):
        self.assertEqual(f"{self.snack.title}", "pickle")
        self.assertEqual(f"{self.snack.description}", "rick")
        self.assertEqual(f'{self.snack.purchaser}', 'tester')

    def test_list_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_status_code(self):
        url = reverse("snack_detail", args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_status_code(self):
        url = reverse("snack_update", args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_status_code(self):
        url = reverse("snack_delete", args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_status_code(self):
        url = reverse("snack_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
