def smoke_check(function):
    def wrapped(self, hero_id):
        response = function(self, hero_id)
        assert response.status_code == 200
        assert response.json()['response'] == 'success'

    return wrapped
