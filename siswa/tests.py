from django.test import TestCase
from django.urls import reverse
from .models import Siswa

class SiswaTestCase(TestCase):
    def setUp(self):
        self.test_object = Siswa.objects.create(
            Nama="Aldi")

    def test_sekolah_cek_nama(self):
        smkn2 = Siswa.objects.get(Nama="Aldi")
        self.assertEqual(smkn2.Nama, "Aldi")

    def test_create(self):
        new_object = Siswa.objects.create(
        NISN="1234567890",
        Nama="Adli")

    def test_read(self):
        obj = Siswa.objects.get(Nama="Aldi")
        self.assertEqual(obj, self.test_object)

    def test_update(self):
        self.test_object.name = 'Aldi'
        self.test_object.save()
        obj = Siswa.objects.get(id=self.test_object.id)
        self.assertEqual(obj.Nama, 'Aldi')

    def test_delete(self):
        self.test_object.delete()
        with self.assertRaises(Siswa.DoesNotExist):
            Siswa.objects.get(id=self.test_object.id)
