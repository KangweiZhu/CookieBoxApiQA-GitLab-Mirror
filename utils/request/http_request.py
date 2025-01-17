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

from context.context import application_context
from utils.request.base_request import BaseRequest, url_formatter


class HttpRequest(BaseRequest):

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
                method=self.sanitize_data_fields(application_context, apitestcase.method),
                url=self.sanitize_data_fields(application_context, request_url),
                headers=self.sanitize_data_fields(application_context, apitestcase.headers),
                params=self.sanitize_data_fields(application_context, apitestcase.params),
                data=self.sanitize_data_fields(application_context, json.dumps(apitestcase.data), is_json_str=True),
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
