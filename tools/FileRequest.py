# -*- coding: UTF-8 -*-

class FileRequest:
    """自定义的Request对象，有file文件中获取参数并赋值给它"""
    request_header_dict = {}
    """
        request_header_dict[URL_method]
        request_header_dict[URL_value]
        request_header_dict[Host]
        request_header_dict[Content-Length]
        request_header_dict[Cache-Control]
        request_header_dict[Origin]
        request_header_dict[Upgrade-Insecure-Requests]
        request_header_dict[User-Agent]
        request_header_dict[Content-Type]
        request_header_dict[Accept]
        request_header_dict[Referer]
        request_header_dict[Accept-Encoding]
        request_header_dict[Accept-Language]
        request_header_dict[Cookie]
        request_header_dict[Connection]
    """
    request_url=""
    """ request_url 存储request的URL部分"""
    request_url_parameters={}
    """ request_url_parameters 存储request的URL部分的参数"""

    request_parameters={}
    """ 记录请求中的参数部分，get和post都放在里面"""
    request_date_posts=""
    """
       记录请求中的post参数串放在里面。
       形如： n2612mL76ok0oC2kn76=6&076ok0oDplZ20o=sss&075526o=ssss
    """
    request_date_gets=""
    """
       记录请求中的get参数串放在里面。
       形如： subaction=hunt&style=b&mode=and&code=0
    """
    request_url_method="GET"
    """
       请求的类型。其值可以包含(GET|POST)
       默认给值为GET
    """
    request_content_type_boundary = ""
    """
        file_request_content_type post才有，这个决定post data模块的类型。主要有两种类型:
        Content-Type: application/x-www-form-urlencoded
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLY96mLehbhhAYyIj
    """

    def __init__(self, request_header_dict):
        """ 使用字典按键值对的方式，接受对应的参数。"""
        self.request_header_dict = request_header_dict
        


     