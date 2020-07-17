# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:21:41 2019

@author: 13716
"""

# =============================================================================
# import requests
# 
# 
# 
# 
# 

# 
# url = "https://nlp.tencentcloudapi.com/?Action=TextCorrection&Text={}&Version=2019-04-08&Region=ap-guangzhou".format(text)
# 
# response = requests.get(url)
# 
# print(response.text)
# =============================================================================

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.nlp.v20190408 import nlp_client, models 
try: 
    cred = credential.Credential("AKIDnZPRjFokphQnESLpRvFPSK8xfDlHBiK8", "2124RuToO2dYxKF5kKl5EIFHQOfoxzuo") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile) 

    req = models.TextCorrectionRequest()
    params = '{"Text": "人生并不是那么美好的技乞"}'
    req.from_json_string(params)

    resp = client.TextCorrection(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 