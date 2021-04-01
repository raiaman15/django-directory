from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import CompanyPageView, ProductPageView


class CompanyPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('company_page')
        self.response = self.client.get(url)

    def test_companypage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_companypage_template(self):
        self.assertTemplateUsed(self.response, 'pages/company.html')

    def test_companypage_contains_correct_html(self):
        self.assertContains(self.response, 'Company Details Page')

    def test_companypage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_companypage_url_resolves_companypageview(self):
        view = resolve('/company/')
        self.assertEqual(
            view.func.__name__,
            CompanyPageView.as_view().__name__
        )


class ProductPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('product_page')
        self.response = self.client.get(url)

    def test_productpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_productpage_template(self):
        self.assertTemplateUsed(self.response, 'pages/product.html')

    def test_productpage_contains_correct_html(self):
        self.assertContains(self.response, 'All Rights Reserved')

    def test_productpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_productpage_url_resolves_productpageview(self):
        view = resolve('/product/')
        self.assertEqual(
            view.func.__name__,
            ProductPageView.as_view().__name__
        )
