def _respond(status, data, httpCode):
    response = {
        'status': status,
        'data': data
    }
    return response, httpCode


def success(data):
    return _respond('success', data, 200)


def failure(data, httpCode):
    return _respond('failure', data, httpCode)
