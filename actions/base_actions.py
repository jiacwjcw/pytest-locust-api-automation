import json
import requests
import allure
from configs.config import get_environment


env = get_environment()
host_url = env.get("host_url")


def get(path, **kwargs):
    """Http GET method"""
    result = requests.get(host_url + path, **kwargs)
    save_request_details(result.request)
    save_response_details(result)
    return result


def post(path, **kwargs):
    """Http POST method"""
    result = requests.post(host_url + path, **kwargs)
    save_request_details(result.request)
    save_response_details(result)
    return result


def put(path, **kwargs):
    """Http PUT method"""
    result = requests.put(host_url + path, **kwargs)
    save_request_details(result.request)
    save_response_details(result)
    return result


def delete(path, **kwargs):
    """Http DELETE method"""
    result = requests.delete(host_url + path, **kwargs)
    save_request_details(result.request)
    save_response_details(result)
    return result


def patch(path, **kwargs):
    """Http PATCH method"""
    result = requests.patch(host_url + path, **kwargs)
    save_request_details(result.request)
    save_response_details(result)
    return result


def save_request_details(request):
    """Attach request details to test report"""
    allure.attach(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "-----------Request----------->",
            request.method + " " + request.url,
            "\n".join("{}: {}".format(k, v) for k, v in request.headers.items()),
            request.body,
        ),
        "Request details",
    )


def save_response_details(response):
    if response.text:
        parser = json.loads(response.text)
    """Attach response details to test report"""
    allure.attach(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "<-----------Response-----------",
            "Status code:" + str(response.status_code),
            "\n".join("{}: {}".format(k, v) for k, v in response.headers.items()),
            json.dumps(parser, indent=4, sort_keys=True) if response.text else "(empty)",
        ),
        "Response details",
    )
