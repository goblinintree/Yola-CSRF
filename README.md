"# CSRF" 
"# Yola-CSRF" 
"# Yola-CSRF" 

## FOR EXAMPLE

    fileRequest = tools.get_fileRequest_from_file("./post_form.log")
    # print fileRequest.request_parameters

    tmp_srcrequest = tools.get_srcrequest_from_fileRequest(fileRequest)
    # print tmp_srcrequest.get_url()
    # print tmp_srcrequest.get_post_data_str()

    # tmp_srcrequest.get_header()
    # tmp_srcrequest.get_post_data_str()
    tmp_srcrequest.do_post_request()