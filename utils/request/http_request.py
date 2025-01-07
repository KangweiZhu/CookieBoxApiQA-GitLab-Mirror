# -*- encoding: utf-8 -*-
"""
    @File    :   http_request.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 12:01    Anicaa (Kangwei Zhu)  1.0      
"""
import json
import logging
from typing import Optional, Any

import requests

from context.context import context
from utils.request.base_request import BaseRequest, url_formatter


class HttpRequest(BaseRequest):

    def _sanitize(self, field: Any) -> Any:
        return BaseRequest.sanitize_data_fields(context, field, self.apitestcase.identifier)

    def send_request(self) -> Optional[requests.Response]:
        apitestcase = self.apitestcase
        request_url = url_formatter(
            **{
                'protocol': apitestcase.protocol,
                'host': apitestcase.host,
                'api': apitestcase.api
            }
        )
        try:
            logging.info(f"Sending {apitestcase.method} request to {request_url}")
            resp = requests.request(
                method=self._sanitize(apitestcase.method),
                url=self._sanitize(request_url),
                headers=self._sanitize(apitestcase.headers),
                params=self._sanitize(apitestcase.params),
                data=self._sanitize(json.dumps(apitestcase.data)),
                timeout=5,
            )
            resp.raise_for_status()
            return resp

        except requests.Timeout:
            logging.error(f"Request to {request_url} timed out.")
        except requests.RequestException as e:
            logging.error(f"Request error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error during request: {e}")

        return None
