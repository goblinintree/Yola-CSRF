# -*- coding: UTF-8 -*-
import urllib
import time
import FileRequest
import doFile
from random import Random
import json
import srcrequest


def get_dict_from_post_log(post_data_str):
    post_data_dict = {}
    if not post_data_str:
        return post_data_dict
    post_param_list = post_data_str.split("&")
    for i, post_param in enumerate(post_param_list):
        # print post_param
        param_key_value = post_param.split("=")
        post_data_dict[param_key_value[0]] = urllib.unquote(param_key_value[1])
        pass
    return post_data_dict

def get_dict_from_get_log(get_data_str):
    get_data_dict = get_dict_from_post_log(get_data_str)
    return get_data_dict

def get_time_for_request():
    t_str = time.time()
    nowTime = int(round(t_str * 1000))
    return str(nowTime)

def get_time_13():
    """ 
    Such As: 1510556369752
    """
    t_str = time.time()
    nowTime = int(round(t_str * 1000))
    return str(nowTime)

def get_patam_str_from_dict(patam_dict):
    tmp_url_str = ""
    tmp_patam_dict = patam_dict
    if tmp_patam_dict:
        for tmp_patam_key in tmp_patam_dict:
            tmp_url_str = tmp_url_str + "&" + tmp_patam_key + "=" + urllib.quote(tmp_patam_dict[tmp_patam_key]) 
            pass
        pass
    return tmp_url_str

def get_patam_json_from_dict(patam_dict):
    patam_dict_json = ""
    # tmp_patam_dict = patam_dict
    tmp_patam_dict = {"AA":"aa", "BB":"bb", "CC":"cc", "DD":"dd"}
    # patam_dict_json = json.load(tmp_patam_dict)
    patam_dict_json = json.dumps(tmp_patam_dict)

    return patam_dict_json
  


def get_fileRequest_from_file(file_path):
    fileRequest = doFile.getFileRequest(file_path)
    return fileRequest

def get_header_dict_from_fileRequest(fileRequest):
    return fileRequest.request_header_dict

def get_parameters_dict_from_fileRequest(fileRequest):
    return fileRequest.request_parameters


def package_parameters_for_multipart(fileRequest):
    fileRequest = get_fileRequest_from_file("../post_form.log")
    fileRequest.request_content_type_boundary = get_boundary_flag()
    return fileRequest


def get_boundary_flag(randomlength=33):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    _str = '' 

    length = len(chars) - 1
    random = Random() 
    for i in range(randomlength): 
        _str+=chars[random.randint(0, length)]

    _str = "----" + _str
    return _str



def get_srcrequest_from_fileRequest(fileRequest):
    tmp_srcrequest = srcrequest.SrcRequest()

    tmp_srcrequest.set_url(fileRequest.request_url)
    tmp_srcrequest.set_method(fileRequest.request_url_method)
    tmp_srcrequest.set_content_type
    tmp_srcrequest.set_header(fileRequest.request_header_dict)

    tmp_srcrequest.set_url(fileRequest.request_url)
    tmp_srcrequest.set_method(fileRequest.request_url_method)
    tmp_srcrequest.set_url_parameters(fileRequest.request_url_parameters)
    if fileRequest.request_url_method == "POST":
        if not fileRequest.request_content_type_boundary:
            tmp_srcrequest.set_content_type("x-www-form-urlencoded")
            pass
        else:
            tmp_srcrequest.set_content_type("form-data")
            tmp_srcrequest.set_content_type_boundary_flag(fileRequest.request_content_type_boundary)
            pass
        pass
    tmp_srcrequest.set_header(fileRequest.request_header_dict) 
    tmp_srcrequest.set_parameters(fileRequest.request_parameters) 
    tmp_srcrequest.set_date_posts(fileRequest.request_date_posts)
    tmp_srcrequest.set_date_gets(fileRequest.request_date_gets)

    return tmp_srcrequest


# fileRequest = get_fileRequest_from_file("../post_form.log")
# print fileRequest.request_parameters
# fileRequest.request_content_type_

# print get_boundary_flag()

# -- ----WebKitFormBoundaryqLsRXIZYATyoQ4IR
# 4 + 33











#   1510198677900
# 1510140054580
# 测试get_dict_from_post_log(post_data_str) 时使用
# post_data_str = "username=m10gys03&password=123456a&pn=miccn&tab=miccn&ticket=undefined&callback=parent.focusSSOController.callFeedback&sucurl=http%3A%2F%2Fmembercenter.cn.made-in-china.com%2Fmember%2Fmain%2F%3F_%3D1&rememberLogUserNameFlag=0&encoding=GBK"
# print get_dict_from_post_log(post_data_str)
# print get_time_for_request()