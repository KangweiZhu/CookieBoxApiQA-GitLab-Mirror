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
from typing import Optional

import requests

from context.response_context import context
from utils.request.base_request import BaseRequest, protocol_formatter

class HttpRequest(BaseRequest):

    def send_request(self) -> Optional[requests.Response]:
        apitestcase = self.apitestcase
        request_url = protocol_formatter(apitestcase.protocol) + apitestcase.host + apitestcase.api
        print(self.sanitize_headers(context, apitestcase.headers))
        try:
            logging.info(f"Sending {apitestcase.method} request to {request_url}")

            resp = requests.request(
                method=apitestcase.method,
                url=request_url,
                headers=self.sanitize_headers(context, apitestcase.headers),
                params=apitestcase.params,
                data=json.dumps(apitestcase.data),
                timeout=5
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

