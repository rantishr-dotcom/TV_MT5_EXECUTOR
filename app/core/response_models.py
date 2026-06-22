def success_response(data=None):

    return {
        "success": True,
        "data": data
    }


def error_response(message):

    return {
        "success": False,
        "message": message
    }