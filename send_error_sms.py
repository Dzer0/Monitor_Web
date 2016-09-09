# -*- coding: utf-8 -*-
import top.api
 
req = top.api.AlibabaAliqinFcSmsNumSendRequest('gw.api.taobao.com',80)
req.set_app_info(top.appinfo('key','短信API'))

def send_sms(phone,projectname,errorcode):
    req.extend = ""
    req.sms_type = "normal"
    req.sms_free_sign_name = "医生助手"
    req.sms_param = "{arg0:" + projectname + ",arg1:"+ errorcode + "}"
    req.rec_num = phone
    req.sms_template_code = "短信模板id"
    try :
         resp = req.getResponse()
         print(resp)
         if 'success' in resp:
            print('短信已经下发')
         return 'success'
    except Exception,e:
         print (e)
         return e

if __name__ == '__main__':
    status = send_sms('phonenumber','第三方开放平台1.0','data不匹配')
    print status
