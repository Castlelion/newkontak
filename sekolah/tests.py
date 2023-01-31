from django.test import TestCase
from django.urls import reverse
from .models import Sekolah

<<<<<<< HEAD
# Create your tests here.
=======
# # Create your tests here.
>>>>>>> bd23c9c5fc8c54f9d306476961442b5ac213f27d
class SekolahTestCase(TestCase):
    def setUp(self):
        self.test_object = Sekolah.objects.create(
            Nama="SMKN 2 Sukabumi", 
            Status="Negeri")

    def test_sekolah_cek_nama(self):
        """ Cek nama sekolah """
        smkn2 = Sekolah.objects.get(Nama="SMKN 2 Sukabumi")
        self.assertEqual(smkn2.Nama, "SMKN 2 Sukabumi")

    def test_create(self):
        new_object = Sekolah.objects.create(
        Nama="SMKN 1 Sukabumi", 
        Status="Negeri")

    def test_read(self):
        obj = Sekolah.objects.get(Nama="SMKN 2 Sukabumi")
        self.assertEqual(obj, self.test_object)

    def test_update(self):
        self.test_object.name = 'SMKN 2 Sukabumi'
        self.test_object.save()
        obj = Sekolah.objects.get(id=self.test_object.id)
        self.assertEqual(obj.Nama, 'SMKN 2 Sukabumi')

    def test_delete(self):
        self.test_object.delete()
        with self.assertRaises(Sekolah.DoesNotExist):
<<<<<<< HEAD
            Sekolah.objects.get(id=self.test_object.id)
=======
            Sekolah.objects.get(id=self.test_object.id)

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)
>>>>>>> bd23c9c5fc8c54f9d306476961442b5ac213f27d
