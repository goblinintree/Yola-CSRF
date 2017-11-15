# -*- coding: UTF-8 -*-
import requests
import tools
import cookielib
from bs4 import BeautifulSoup


class SrcRequest:
    request_url = ""
    request_url_method = ""
    request_url_parameters = {}
    request_content_type = ""
    request_content_type_boundary_flag = ""
    request_header_content_type = {}
    

    request_header_dict = {}
    request_parameters = {}

    request_date_posts = ""
    request_date_gets = ""
    request_sealed = {}



    def __init__(self,url_method="GET", request_content_type=""):
        """
        url_method 默认 GET,其值可以为 GET | POST \n
        request_content_type,其值包含： x-www-form-urlencoded | form-data
        """
        self.request_url_method = url_method
        self.request_content_type = request_content_type

        self.request_sealed["set"] = False
        self.request_sealed["boundary"] = False
        pass

    def set_file_request(self, fileRequest):
        """set request_url """
        if not self.request_sealed["set"]:
            self.request_url = fileRequest.request_url
            self.request_url_method = fileRequest.request_url_method
            self.request_url_parameters = fileRequest.request_url_parameters
            if fileRequest.request_url_method == "POST":
                if not fileRequest.file_request_content_type_boundary:
                    self.request_content_type = "x-www-form-urlencoded"
                    pass
                else:
                    self.request_content_type = "form-data"
                    self.request_content_type_boundary_flag = fileRequest.file_request_content_type_boundary
                    pass
                pass
            self.request_header_dict = fileRequest.request_header_dict
            self.request_parameters = fileRequest.request_parameters
            self.request_date_posts = fileRequest.request_date_posts
            self.request_date_gets = fileRequest.request_date_gets
            pass
        pass

    def set_url(self, url_str):
        """set request_url """
        if not self.request_sealed["set"]:
            self.request_url = url_str
            pass
        pass

    def set_method(self, method_str):
        """set request_url_method """
        if not self.request_sealed["set"]:
            self.request_url_method = method_str
            pass
        pass

    def set_url_parameters(self, url_parameters_dict):
        """set request_url_method """
        if not self.request_sealed["set"]:
            self.request_url_parameters = url_parameters_dict
            pass
        pass

    def set_content_type(self, content_type_str):
        """
            set request_content_type,其值包含： x-www-form-urlencoded | form-data
            request_url_method post才有，这个决定post data模块的类型。主要有两种类型:
            Content-Type: application/x-www-form-urlencoded
            Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLY96mLehbhhAYyIj
         """
        if not self.request_sealed["set"]:
            self.request_content_type = content_type_str
            pass
        pass

    def set_content_type_boundary_flag(self, content_type_boundary_flag):
        """set request_content_type_boundary_flag """
        if not self.request_sealed["set"]:
            self.request_content_type_boundary_flag = content_type_boundary_flag
            pass
        pass

    def set_header_content_type(self, header_content_type_dict):
        """set request_header_content_type """
        if not self.request_sealed["set"]:
            self.request_header_content_type = header_content_type_dict
            pass
        pass

    def set_header(self, header_dict):
        """set request_header_dict """
        if not self.request_sealed["set"]:
            self.request_header_dict = header_dict
            pass
        pass

    def set_parameters(self, parameters_dict):
        """set request_parameters """
        if not self.request_sealed["set"]:
            self.request_parameters = parameters_dict 
            pass
        pass

    def set_date_posts(self, date_posts_str):
        """set request_date_posts """
        if not self.request_sealed["set"]:
            self.request_date_posts = date_posts_str
            pass
        pass

    def set_date_gets(self, date_gets_str):
        """set request_date_gets """
        if not self.request_sealed["set"]:
            self.request_date_gets = date_gets_str
            pass
        pass

    def get_src_get_request(self):
        if self.request_url_method == "GET" :
            self.request_sealed["set"] = True
            src_request = requests.post(self.request_url, data=None, header={})
        return src_request
    

    def get_url(self):
        self.request_sealed["set"] = True

        url_str = ""
        tmp_request_url_str =  self.request_url
        tmp_request_url_parameters = self.request_url_parameters

        if tmp_request_url_parameters:
            """ URL中有参数时，根据类型封装"""
            tmp_request_url_parameters_str =  tools.get_patam_str_from_dict(tmp_request_url_parameters)

            if self.request_url_method == "POST" :
                """"封装 POST"""
                if str(tmp_request_url_str).find("?") > -1:
                    """当前URL中包含参数"""

                    url_str = tmp_request_url_str + tmp_request_url_parameters_str
                    pass
                else:
                    """当前URL中不包含参数"""
                    url_str = tmp_request_url_str + "?" + tmp_request_url_parameters_str
                    pass
                pass
            else:
                """"封装 GET"""
                if str(tmp_request_url_str).find("?") > -1:
                    """当前URL中包含参数"""
                    url_str = tmp_request_url_str + tmp_request_url_parameters_str
                    pass
                else:
                    """当前URL中不包含参数"""
                    url_str = tmp_request_url_str + "?" + tmp_request_url_parameters_str + self.get_get_params_str()
                    pass
                pass
            pass
          
        else:
            """ URL中无参数时，直接返回当前的URL"""
            url_str = tmp_request_url_str
            pass
        return url_str
    
    def get_get_params_str(self):
        self.request_sealed["set"] = True
        get_params_str = ""
        tmp_request_parameters = self.request_parameters

        if tmp_request_parameters:
            """ URL中有参数时，根据类型封装"""
            tmp_request_parameters_str =  tools.get_patam_str_from_dict(tmp_request_parameters)

            if self.request_url_method == "GET" :
                """"封装 GET"""
                get_params_str = get_params_str + tmp_request_parameters_str
                pass
            pass
          
        else:
            """ URL中无参数时，直接返回当前的URL"""
            pass
        return get_params_str

    def get_post_data_str(self):
        self.request_sealed["set"] = True
        post_data_str = ""
        tmp_request_parameters = self.request_parameters

        if tmp_request_parameters:
            """ URL中有参数时，根据类型封装"""
            tmp_request_parameters_str =  ""

            if self.request_url_method == "POST" and self.request_content_type == "x-www-form-urlencoded" :
                """"封装 POST的 x-www-form-urlencoded 格式数据 """
                tmp_request_parameters_str =  tools.get_patam_str_from_dict(tmp_request_parameters)
                post_data_str = post_data_str + tmp_request_parameters_str
                pass
            elif self.request_url_method == "POST" and self.request_content_type == "form-data" :
                # print  self.request_sealed["boundary"] 
                if not self.request_sealed["boundary"]:
                    tmp = tools.get_boundary_flag()
                    self.request_content_type_boundary_flag  = tmp 
                    self.request_sealed["boundary"] = True
                    # print  self.request_sealed["boundary"] 
                    pass
                tmp_request_content_type_boundary_flag = self.request_content_type_boundary_flag

                # self.get_header()
                tmp_line_feed_flag = "\n"
                tmp_form_data_format = "Content-Disposition: form-data; "
                if tmp_request_parameters:
                    # print str(tmp_request_parameters)
                    for tmp_patam_key in tmp_request_parameters:
                        tmp_request_parameters_str = (tmp_request_parameters_str + "--" + tmp_request_content_type_boundary_flag 
                        + tmp_line_feed_flag)

                        tmp_form_data_format_line = (tmp_form_data_format + "name=\""+ tmp_patam_key +"\""
                        + tmp_line_feed_flag
                        + tmp_line_feed_flag)
                        tmp_request_parameters_str = (tmp_request_parameters_str + tmp_form_data_format_line)
                        str_p = tmp_request_parameters[tmp_patam_key]
                        # print str_p
                        # print str(str_p).encode("gbk")
                        # print str(str_p).encode("utf-8")
                        # print str(str_p).encode("raw_unicode_escape")

                        # print str(str_p).decode("gbk")
                        # print str(str_p).decode("utf-8")
                        # print str(str_p).decode("raw_unicode_escape")

                        
                        tmp_request_parameters_str = (tmp_request_parameters_str 
                        + str_p 
                        + tmp_line_feed_flag)
                        pass
                    tmp_request_parameters_str = (tmp_request_parameters_str + "--" + tmp_request_content_type_boundary_flag 
                    + tmp_line_feed_flag)
                    pass
                # self.request_content_type_boundary_flag = tmp_request_content_type_boundary_flag
                post_data_str = tmp_request_parameters_str
                pass
            else:
                post_data_str = tmp_request_parameters_str + "ERROR=ERROR"
                pass
            pass
        else:
            """ URL中无参数时，直接返回当前的URL"""
            pass
        return post_data_str
    

    def get_post_data_json(self):
        self.request_sealed["set"] = True
        post_data_json = ""
        tmp_request_parameters = self.request_parameters

        if tmp_request_parameters:
            """ URL中有参数时，根据类型封装"""
            tmp_request_parameters_str =  ""

            if self.request_url_method == "POST" and self.request_content_type == "x-www-form-urlencoded" :
                """"封装 POST的 x-www-form-urlencoded 格式数据 """
                post_data_json = tmp_request_parameters

                tmp_request_parameters_str =  tools.get_patam_str_from_dict(tmp_request_parameters)
                post_data_str = post_data_str + tmp_request_parameters_str
                pass
            elif self.request_url_method == "POST" and self.request_content_type == "form-data" :
                # print  self.request_sealed["boundary"] 
                if not self.request_sealed["boundary"]:
                    tmp = tools.get_boundary_flag()
                    self.request_content_type_boundary_flag  = tmp 
                    self.request_sealed["boundary"] = True
                    # print  self.request_sealed["boundary"] 
                    pass
                tmp_request_content_type_boundary_flag = self.request_content_type_boundary_flag

                # self.get_header()
                tmp_line_feed_flag = "\n"
                tmp_form_data_format = "Content-Disposition: form-data; "
                if tmp_request_parameters:
                    # print str(tmp_request_parameters)
                    for tmp_patam_key in tmp_request_parameters:
                        tmp_request_parameters_str = (tmp_request_parameters_str + "--" + tmp_request_content_type_boundary_flag 
                        + tmp_line_feed_flag)

                        tmp_form_data_format_line = (tmp_form_data_format + "name=\""+ tmp_patam_key +"\""
                        + tmp_line_feed_flag
                        + tmp_line_feed_flag)
                        tmp_request_parameters_str = (tmp_request_parameters_str + tmp_form_data_format_line)
                        str_p = tmp_request_parameters[tmp_patam_key]
                        # print str_p
                        # print str(str_p).encode("gbk")
                        # print str(str_p).encode("utf-8")
                        # print str(str_p).encode("raw_unicode_escape")

                        # print str(str_p).decode("gbk")
                        # print str(str_p).decode("utf-8")
                        # print str(str_p).decode("raw_unicode_escape")

                        
                        tmp_request_parameters_str = (tmp_request_parameters_str 
                        + str_p 
                        + tmp_line_feed_flag)
                        pass
                    tmp_request_parameters_str = (tmp_request_parameters_str + "--" + tmp_request_content_type_boundary_flag 
                    + tmp_line_feed_flag)
                    pass
                # self.request_content_type_boundary_flag = tmp_request_content_type_boundary_flag
                post_data_str = tmp_request_parameters_str
                pass
            else:
                post_data_str = tmp_request_parameters_str + "ERROR=ERROR"
                pass
            pass
        else:
            """ URL中无参数时，直接返回当前的URL"""
            pass
        return post_data_str
    

    def get_header(self):
        self.request_sealed["set"] = True
        self.get_post_data_str()
        # print "get_header >> " +self.request_content_type_boundary_flag

        if self.request_url_method == "POST" and self.request_content_type == "form-data" :
            if self.request_content_type_boundary_flag:
                tmp_request_header_dict = self.request_header_dict
                tmp_request_content_type_boundary_flag = self.request_content_type_boundary_flag
                tmp_request_header_content_type = {}
                tmp_request_header_content_type = tmp_request_header_dict["Content-Type"]
                tmp_request_header_content_type ={ "Content-Type":"multipart/form-data; boundary=" + tmp_request_content_type_boundary_flag}

                self.request_header_content_type = tmp_request_header_content_type
                tmp_request_header_dict.update(tmp_request_header_content_type)
                self.request_header_dict = tmp_request_header_dict
                pass
            pass
        pass

        return self.request_header_dict


    def do_post_request(self):
        self.request_sealed["set"] = True
        print 1

        src_request = None
        if self.request_url_method == "POST" :
            # src_request = requests.post(self.get_url(), data=None, header={})
            tmp_body_data =  self.get_post_data_str()
            # print body_data.encode("UTF-8")
            # src_response = requests.post(self.get_url(), data=body_data, headers=(self.get_header()))
            # src_response = requests.post(self.get_url(), json=tools.get_patam_json_from_dict(self.request_parameters), headers=(self.get_header()))
            tmp_header = self.get_header()
            tmp_url = self.get_url()
            tmp_header.update({"Origin":"null", "Referer":"", "Cookie":""})
            sion = requests.session()
            print tmp_url
            print tmp_header
            print tmp_body_data

            src_response = sion.post(tmp_url, data=tmp_body_data, headers=tmp_header)
            # src_response = requests.post(self.get_url(), data=body_data, )
            """
            """
            # src_response = sion.get("http://cn.made-in-china.com/inquiry.do?xcase=inquiryComplete&sourceId=qMrnSsRuXhYb&sourceType=shrom&receiverComId=qMrnSsRuXhYb&encryptSuss=0&senderMail=1825000322@qq.com&comIdentity=0&offerType=&senderCom=CSRF%C3%A5%26%23174%3B%A1%EB%C3%A5%A1%AD%A1%A7%C3%A6%C2%B5%26%238249%3B%C3%A8%A1%A5%26%238226%3B6&senderName=CSRF%C3%A5%26%23174%3B%A1%EB%C3%A5%A1%AD%A1%A7%C3%A6%C2%B5%26%238249%3B%C3%A8%A1%A5%26%238226%3B6&senderSex=1")
            print 4  
            pass
        else:
            """ 从这里获得GET请求 """
            src_request = requests.get(self.get_url(), params=None, header={})
            pass
        return src_request



    def get_src_request(self, abc):
        self.request_sealed["set"] = True

        src_request = None
        if self.request_url_method == "POST" :
            src_request = requests.post(self.get_url(), data=None, header={})
            pass
        else:
            """ 从这里获得GET请求 """
            src_request = requests.get(self.get_url(), params=None, header={})
            pass
        return src_request


    def out_poc_csrf_html(self):
        out_file_name = "csrf_" + tools.get_time_13() + ".html"
        print out_file_name # TO do something you wan't to do 
        csrf_html_context = ""
        soup = BeautifulSoup(out_file_name)
        soup

        return out_file_name

