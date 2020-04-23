import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    #Тесты для класса AnonymousSurvey

    def test_store_single_response(self):
        #Проверяет, что один ответ сохранён правильно.
        question = 'Какой у вас первый язык?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('русский')
        self.assertIn('русский', my_survey.responses)

    def test_store_three_responses(self):
        #Проверяет, что 3 ответа были сохранены правильно
        question = 'Какой у вас первый язык?'
        my_survey = AnonymousSurvey(question)
        responses = ['русский', 'англ', 'китай']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()

print()



