from django.test import TestCase

from appdetreinos.evaluations.forms import EvaluationForm


class EvaluationTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/avaliacao/')

    def test_get(self):
        '''Get /avaliacao/ must return status code 200'''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        '''Must use template evaluations / evaluation_form.html'''
        self.assertTemplateUsed(self.response, 'evaluations/evaluation_form.html')

    #def test_html(self):
    #    '''Html must contain input tags'''
#
 #       self.assertContains(self.response, '<form')
  #      self.assertContains(self.response, '<input', 11)
   #     self.assertContains(self.response, 'type="text"', 4)
    #    self.assertContains(self.response, 'type="number"', 4)
     #   self.assertContains(self.response, 'type="date"', 1)
      #  self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        '''Html must contain csrf '''
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have subscription form'''
        form = self.response.context['form']
        self.assertIsInstance(form, EvaluationForm)

    def test_form_has_fields(self):
        '''Form must have 9 fields'''
        form = self.response.context['form']
        self.assertSequenceEqual([
            'name', 'date', 'age', 'weight', 'height', 'bf', 'pathology', 'objective', 'conditioning'
        ], list(form.fields))
