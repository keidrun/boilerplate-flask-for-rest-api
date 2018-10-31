from utils import response


class TestResponse(object):

    def test_return_success(self):
        data = {
            'name': 'Steve Jobs',
            'age': 30,
            'gender': "male",
            'email': "steve@jobs.com"
        }
        r, httpCode = response.success(data)
        assert r == {
            'status': 'success',
            'data': data
        }
        assert httpCode == 200

    def test_return_failure(self):
        data = {
            'errors': {
                'message': 'ERROR'
            }
        }
        r, httpCode = response.failure(data, 400)
        assert r == {
            'status': 'failure',
            'data': data
        }
        assert httpCode == 400
