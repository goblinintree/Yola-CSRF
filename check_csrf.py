# -*- coding: UTF-8 -*-
import requests
import sys
import sys
reload(sys)
# print sys.geindefaultencoding()
sys.setdefaultencoding("UTF-8")
# from tools import tools,FileRequest,srcrequest,doFile
from tools import tools,srcrequest

fileRequest = tools.get_fileRequest_from_file("./post_form.log")
# print fileRequest.request_parameters

tmp_srcrequest = tools.get_srcrequest_from_fileRequest(fileRequest)
# print tmp_srcrequest.get_url()
# print tmp_srcrequest.get_post_data_str()

# tmp_srcrequest.get_header()
# tmp_srcrequest.get_post_data_str()
# tmp_srcrequest.do_post_request()

# print tools.get_patam_json_from_dict({})
print tmp_srcrequest.out_poc_csrf_html()




