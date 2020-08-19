from django.test import TestCase

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


class EvaluationPostTest(TestCase):
    def setUp(self):
        '''Valid POST should redirect to /avaliacao/'''
        data = dict(
            name='Luis Tavares',
            date='17/07/2020',
            age='29',
            weight='97',
            height='1.80',
            bf='30',
            pathology='ombro',
            objective='emagrecer',
            conditioning='fraco'
        )
        self.response = self.client.post('/avaliacao/', data)

class EvalutionInvalidPost(TestCase):
    def test_post(self):
        '''Invalid POST should not redirect'''
        response = self.client.post('/avaliacao/', {})
        self.assertEqual(200, response.status_code)
