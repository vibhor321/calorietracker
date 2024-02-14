from rest_framework.response import Response


def custom_response(data=None, message=None, status_code=200):
    """
    Helper function to generate JSON response.

    Args:
        data (dict): Data to include in the response.
        message (str): Optional message to include in the response.
        status_code (int): HTTP status code for the response.

    Returns:
        Response: DRF Response object.
    """
    response_data = {"data": data, "message": message}

    return Response(response_data, status=status_code)
