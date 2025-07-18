"""
Test for django admin modification
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """Test for django admin modification"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = "admin@example.com",
            password = "password123"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email = "test@example.com",
            password = "password123",
            name = "Test User"
        )


    def test_users_list(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


    def test_edit_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self .assertEqual(res.status_code, 200)


    def test_cerate_user_pagfe(self):

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
