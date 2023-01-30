from django.test import TestCase
from django.urls import reverse
from .models import Perusahaan

# Create your tests here.
class PerusahaanTestCase(TestCase):
    def setUp(self):
        self.test_object = Perusahaan.objects.create(
            nama="median")

    def test_sekolah_cek_nama(self):
        smkn2 = Perusahaan.objects.get(nama="median")
        self.assertEqual(smkn2.nama, "median")

    def test_create(self):
        new_object = Perusahaan.objects.create(
        nama="skill")

    def test_read(self):
        obj = Perusahaan.objects.get(nama="median")
        self.assertEqual(obj, self.test_object)

    def test_update(self):
        self.test_object.name = 'median'
        self.test_object.save()
        obj = Perusahaan.objects.get(id=self.test_object.id)
        self.assertEqual(obj.nama, 'median')

    def test_delete(self):
        self.test_object.delete()
        with self.assertRaises(Perusahaan.DoesNotExist):
            Perusahaan.objects.get(id=self.test_object.id)

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)
