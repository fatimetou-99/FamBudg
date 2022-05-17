from operator import imod
from django.urls import resolve,reverse
from api.views import RegisterAPI,Dashboard, categoryCreate, categoryDelete, categoryList, categoryUpdate, login, salaryList,salaryCreate,salaryUpdate,salaryDelete,depencyList,depencyDetail,depencyAdd
from django.test import SimpleTestCase

class TestUrls(SimpleTestCase):

    # Salary

    def test_salary_list(self):
        url = reverse('salary-list')
        self.assertEquals(resolve(url).func, salaryList)

    def test_salary_create(self):
        url = reverse('salary-create')
        self.assertEquals(resolve(url).func, salaryCreate)

    def test_salary_update(self):
        url = reverse('salary-update', args=['pk'])
        self.assertEquals(resolve(url).func, salaryUpdate)    

    def test_salary_delete(self):
        url = reverse('salary-delete', args=['pk'])
        self.assertEquals(resolve(url).func, salaryDelete)  

    # Category

    def test_category_list(self):
        url = reverse('category-list')
        self.assertEquals(resolve(url).func, categoryList)

    def test_category_create(self):
        url = reverse('category-create')
        self.assertEquals(resolve(url).func, categoryCreate)

    def test_category_update(self):
        url = reverse('category-update', args=['pk'])
        self.assertEquals(resolve(url).func, categoryUpdate)    

    def test_category_delete(self):
        url = reverse('category-delete', args=['pk'])
        self.assertEquals(resolve(url).func, categoryDelete)  

    # Depency

    def test_depency_list(self):
        url = reverse('depency-list')
        self.assertEquals(resolve(url).func, depencyList)

    def test_depency_add(self):
        url = reverse('depency-add')
        self.assertEquals(resolve(url).func, depencyAdd)

    def test_depency_detail(self):
        url = reverse('depency-detail', args=['pk'])
        self.assertEquals(resolve(url).func, depencyDetail)    

    # Authentication
    
    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, RegisterAPI)

    # Dashboard

    def test_dashboard(self):
        url = reverse('dashbord.get')
        self.assertEquals(resolve(url).func, Dashboard)    