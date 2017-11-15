 # -*- coding: UTF-8 -*- 

import re
import os
import urllib
from FileRequest import FileRequest


def getFileRequest(file_path):
    file_request_header_dict = {}
    file_request_url = ""
    file_request_url_parameters = {}
    file_request_parameters = {}
    """包装后的request_parameters可以经过urllib.unquote解码的，但是暂时未解码 """

    file_request_date_posts = ""
    file_request_date_gets = ""
    file_request_url_method = "GET"
    file_request_content_type_boundary = ""
    """
        file_request_content_type post才有，这个决定post data模块的类型。主要有两种类型:
        Content-Type: application/x-www-form-urlencoded
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLY96mLehbhhAYyIj
    """

    params_key = ""
    params_value = ""
    new_param_flag = 0

    file = open(file_path)
    while True:
        none_line_flag = 0
        """none_line_flag 0表示头部部分，1表示当前行为请求头与post数据体之间的空行，2表示数据体"""
        lines = file.readlines(100)
        
        if not lines :
            break
    
        for line in lines:
            strip_line = line.strip()

            if ((not strip_line) and  (0 == none_line_flag)):
                none_line_flag = 1
                continue
                pass
            if ((strip_line) and  (1 == none_line_flag)):
                none_line_flag = 2
                pass
            
            if 0 == none_line_flag:
                """0 表示现在编列时未遇到空行"""
                matchObj_URL = re.match(r".*(\sHTTP/).*", strip_line, re.M|re.I) 
                if matchObj_URL != None:
                    matchObj_URL_method = None
                    matchObj_URL_method = re.match(r"(^GET)\s", strip_line, re.M|re.I) 
                    if matchObj_URL_method != None:
                        # print "URL_method: " + matchObj_URL_method.group(1)
                        file_request_url_method = matchObj_URL_method.group(1)
                        file_request_header_dict["URL_method"] =  matchObj_URL_method.group(1)
                        pass
                    matchObj_URL_value = re.match(r"^GET\s(.*)\sHTTP", strip_line, re.M|re.I) 
                    if matchObj_URL_value != None:
                        # print "URL_value: " + matchObj_URL_value.group(1)
                        file_request_header_dict["URL_value"] =  matchObj_URL_value.group(1)
                        url_data = file_request_header_dict["URL_value"] 
                        # 元组一个元素就是 ?号前面的URL部分
                        # 元组第二个元素就是 ?号后面的参数部分
                        file_request_url = (url_data.partition("?"))[0]
                        file_request_date_gets = (url_data.partition("?"))[2]
                        tmp_params_str = ((url_data.partition("?"))[2]).partition("#")[0]
                        tmp_params_list = str(tmp_params_str).split("&")
                        for tmp_param in tmp_params_list:
                            # print tmp_param
                            if tmp_param.strip():
                                file_request_url_parameters[(tmp_param.strip().partition("="))[0]] = (tmp_param.strip().partition("="))[2]
                                pass
                            pass
                        pass

                    matchObj_URL_method = re.match(r"(^POST)\s", strip_line, re.M|re.I) 
                    if matchObj_URL_method != None:
                        # print "URL_method: " + matchObj_URL_method.group(1)
                        file_request_header_dict["URL_method"] =  matchObj_URL_method.group(1)
                        file_request_url_method = matchObj_URL_method.group(1)
                        pass
                    matchObj_URL_value = re.match(r"^POST\s(.*)\sHTTP", strip_line, re.M|re.I) 
                    if matchObj_URL_value != None:
                        # print "URL_value: " + matchObj_URL_value.group(1)
                        file_request_header_dict["URL_value"] =  matchObj_URL_value.group(1)
                        url_data = file_request_header_dict["URL_value"] 
                        # 元组一个元素就是 ?号前面的URL部分
                        # 元组第二个元素就是 ?号后面的参数部分
                        file_request_url = (url_data.partition("?"))[0]
                        file_request_date_gets = (url_data.partition("?"))[2]
                        tmp_params_str = ((url_data.partition("?"))[2]).partition("#")[0]

                        tmp_params_list = str(tmp_params_str).split("&")

                        # print tmp_params_list
                        for tmp_param in tmp_params_list:
                            # print tmp_param
                            if tmp_param.strip():
                                file_request_url_parameters[(tmp_param.strip().partition("="))[0]] = (tmp_param.strip().partition("="))[2]
                                pass
                            pass
                    pass

                matchObj_Host = re.match(r"(^Host):\s", strip_line, re.M|re.I) 
                if matchObj_Host != None:
                    matchObj_Host_value = re.match(r"^Host:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Host_value: " + matchObj_Host_value.group(1)
                    file_request_header_dict["Host"] =  matchObj_Host_value.group(1)
                    pass

                matchObj_Cache_Control = re.match(r"(^Cache-Control:)\s", strip_line, re.M|re.I) 
                if matchObj_Cache_Control != None:
                    matchObj_Cache_Control_value = re.match(r"^Cache-Control:\s(.*)$", line, re.M|re.I) 
                    # print "Cache_Control_value: " + matchObj_Cache_Control_value.group(1)
                    file_request_header_dict["Cache-Control"] =  matchObj_Cache_Control_value.group(1)
                    pass

                matchObj_Upgrade = re.match(r"(^Upgrade-Insecure-Requests:)\s", strip_line, re.M|re.I) 
                if matchObj_Upgrade != None:
                    matchObj_Upgrade_value = re.match(r"^Upgrade-Insecure-Requests:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Upgrade_value: " + matchObj_Upgrade_value.group(1)
                    file_request_header_dict["Upgrade-Insecure-Requests"] =  matchObj_Upgrade_value.group(1)
                    pass

                matchObj_Agent = re.match(r"(^User-Agent:)\s", strip_line, re.M|re.I) 
                if matchObj_Agent != None:
                    matchObj_Agent_value = re.match(r"^User-Agent:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Agent_value: " + matchObj_Agent_value.group(1)
                    file_request_header_dict["User-Agent"] =  matchObj_Agent_value.group(1)
                    pass

                matchObj_Accept = re.match(r"(^Accept:)\s", strip_line, re.M|re.I) 
                if matchObj_Accept != None:
                    matchObj_Accept_value = re.match(r"^Accept:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Accept_value: " + matchObj_Accept_value.group(1)
                    file_request_header_dict["Accept"] =  matchObj_Accept_value.group(1)
                    pass

                matchObj_Accept_Encoding = re.match(r"(^Accept-Encoding:)\s", strip_line, re.M|re.I) 
                if matchObj_Accept_Encoding != None:
                    matchObj_Accept_Encoding_value = re.match(r"^Accept-Encoding:\s(.*)$", line, re.M|re.I) 
                    # print "Accept-Encoding_value: " + matchObj_Accept_Encoding_value.group(1)
                    file_request_header_dict["Accept-Encoding"] =  matchObj_Accept_Encoding_value.group(1)
                    pass

                matchObj_Accept_Language = re.match(r"(^Accept-Language:)\s", strip_line, re.M|re.I) 
                if matchObj_Accept_Language != None:
                    matchObj_Accept_Language_value = re.match(r"^Accept-Language:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Accept-Language_value: " + matchObj_Accept_Language_value.group(1)
                    file_request_header_dict["Accept-Language"] =  matchObj_Accept_Language_value.group(1)
                    pass

                matchObj_Cookie = re.match(r"(^Cookie:)\s", strip_line, re.M|re.I) 
                if matchObj_Cookie != None:
                    matchObj_Cookie_value = re.match(r"^Cookie:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Cookie_value: " + matchObj_Cookie_value.group(1)
                    file_request_header_dict["Cookie"] =  matchObj_Cookie_value.group(1)
                    pass

                matchObj_Connection = re.match(r"(^Connection:)\s", strip_line, re.M|re.I) 
                if matchObj_Connection != None:
                    matchObj_Connection_value = re.match(r"^Connection:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Connection_value: " + matchObj_Connection_value.group(1)
                    file_request_header_dict["Connection"] =  matchObj_Connection_value.group(1)
                    pass

                matchObj_Proxy_Connection = re.match(r"(^Proxy-Connection:)\s", strip_line, re.M|re.I) 
                if matchObj_Proxy_Connection != None:
                    matchObj_Proxy_Connection_value = re.match(r"^Proxy-Connection:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Proxy-Connection_value: " + matchObj_Proxy_Connection_value.group(1)
                    file_request_header_dict["Proxy-Connection"] =  matchObj_Proxy_Connection_value.group(1)
                    pass
                pass

                matchObj_Referer = re.match(r"(^Referer:)\s", strip_line, re.M|re.I) 
                if matchObj_Referer != None:
                    matchObj_Referer_value = re.match(r"^Referer:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Referer_value: " + matchObj_Referer_value.group(1)
                    file_request_header_dict["Referer"] =  matchObj_Referer_value.group(1)
                    pass
                pass

                matchObj_Content_Type = re.match(r"(^Content-Type:)\s", strip_line, re.M|re.I) 
                if matchObj_Content_Type != None:
                    matchObj_Content_Type_value = re.match(r"^Content-Type:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Content_Type_value: " + matchObj_Content_Type_value.group(1)
                    file_request_header_dict["Content-Type"] =  matchObj_Content_Type_value.group(1)
                    matchObj_file_request_content_type_boundary = re.search(r"boundary=(.*)$", file_request_header_dict["Content-Type"], re.M|re.I)
                    if matchObj_file_request_content_type_boundary: 
                        file_request_content_type_boundary =  matchObj_file_request_content_type_boundary.groups()[0]
                    else:
                        file_request_content_type_boundary = ""
                        pass
                    pass
                    # print file_request_content_type_boundary
                pass

                matchObj_Origin = re.match(r"(^Origin:)\s", strip_line, re.M|re.I) 
                if matchObj_Origin != None:
                    matchObj_Origin_value = re.match(r"^Origin:\s(.*)$", strip_line, re.M|re.I) 
                    # print "Origin_value: " + matchObj_Origin_value.group(1)
                    file_request_header_dict["Origin"] =  matchObj_Origin_value.group(1)
                    pass
                pass

            if (2 == none_line_flag and str(file_request_content_type_boundary) == ""):
                """ 2表示已经经历过空行，那么下面的数据就是post请求的参数部分。 """
                file_request_date_posts = strip_line
                # print "____" + urllib.unquote(file_request_date_posts)
                tmp_params_str = strip_line
                tmp_params_list = str(tmp_params_str).split("&")
                for tmp_param in tmp_params_list:
                    # print tmp_param
                    if tmp_param.strip():
                        file_request_parameters[(tmp_param.strip().partition("="))[0]] = urllib.unquote((tmp_param.strip().partition("="))[2])
                        # file_request_parameters[(tmp_param.strip().partition("="))[0]] = (tmp_param.strip().partition("="))[2]
                        pass
                    pass 
                pass

            if (2 == none_line_flag and str(file_request_content_type_boundary) != ""):
                """ 2表示已经经历过空行，那么下面的数据就是post请求的参数部分。 """
                # print "none_line_flag >> "+  str(none_line_flag), "file_request_content_type_boundary >> "+ file_request_content_type_boundary
                # print strip_line
                matchObj_boundary_flag = re.match(r"^--("+file_request_content_type_boundary+ ")$", strip_line, re.M|re.I) 
                if matchObj_boundary_flag:
                    new_param_flag = 0
                    pass
                else:
                    new_param_flag = new_param_flag + 1
                    if new_param_flag == 1:
                        # print "##" + str(new_param_flag)
                        matchObj_params_key = re.search(r"form-data; name=\"(.*)\"$", strip_line, re.M|re.I)
                        if matchObj_params_key:
                            params_key = matchObj_params_key.groups()[0]
                            # print "params_key >> " + params_key
                            pass
                        pass
                    if new_param_flag == 2:
                        # print "##" + str(new_param_flag)
                        pass
                    if new_param_flag == 3:
                        # print "##" + str(new_param_flag)
                        if strip_line:
                            params_value = strip_line.decode("utf-8")
                        new_param_flag = 0
                        # print "params_value >> " + params_value
                        file_request_parameters[params_key] = params_value
                        params_key = params_value = ""
                        pass
                    pass

    # print str("request_header_dict").center(120, '=');
    # print request_header_dict;
    # print file_request_url_parameters
    fileRequest = FileRequest(file_request_header_dict)
    fileRequest.request_url = file_request_url
    fileRequest.request_url_parameters = file_request_url_parameters
    fileRequest.request_url_method = file_request_url_method
    fileRequest.request_content_type_boundary = file_request_content_type_boundary
    fileRequest.request_parameters = file_request_parameters
    fileRequest.request_date_gets = file_request_date_gets
    fileRequest.request_date_posts = file_request_date_posts


    return fileRequest
