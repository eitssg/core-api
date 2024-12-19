from ..types import ActionHandlerRoutes
from ..constants import BODY_PARAMETER, QUERY_STRING_PARAMETERS


from core_db.event.actions import EventActions
from core_db.response import Response

from ..actions import ApiActions


class ApiEventActions(ApiActions, EventActions):

    pass


def action_get_event_list(**kwargs) -> Response:
    """
    returns the event for the given prn and timestamp.  Because you
    may leav timestamp blank, there may be more than one event for the prn,
    so, this fuction will always return a list.

    From the query parametrs, you can specify the prn and the earliest_time and latest_time

    Ex:
      event = {
        "queryStringParameters": {
            "prn": "client:portfolio:app:branch:build:component",
            "earliest_time": "2021-01-01T00:00:00",
            "latest_time": "2021-01-02T00:00:00",
            "sort": "ascending",
            "limit": 100,
            "data_paginator": None
      }

    Args:
        event (dict): the event form an http request (lambda event)

    Returns:
        SeccessResponse: a list of all the respones in the SuccessRepsonse body.
    """
    return ApiEventActions.list(**kwargs.get(QUERY_STRING_PARAMETERS, {}))


def action_create_event(**kwargs) -> Response:
    """
    creates a new event

    Ex:
      evnet = {
        "body": {
            "prn": "client:portfolio:app:branch:build:component",
            "timestamp": "2021-01-01T00:00:00",
            "event_type": "status",
            "status": "success",
            "message": "Build success"
        }
      }

    Args:
        event (dict): The event to create from REST API
    """
    return ApiEventActions.create(**kwargs.get(BODY_PARAMETER, {}))


def action_delete_event(**kwargs) -> Response:
    """
    deletes the event for the given prn in the parameters

    Ex:
        event = {
            "queryStringParameters": {
                "prn": "client:portfolio:app:branch:build:component"
            }
        }

    Args:
        eveng (dict): The lambda event
    """
    return ApiEventActions.delete(**kwargs.get(QUERY_STRING_PARAMETERS, {}))


event_actions: ActionHandlerRoutes = {
    "GET:/api/v1/events": action_get_event_list,
    "PUT:/api/v1/event": action_create_event,
    "DELETE:/api/v1/event": action_delete_event,
}
