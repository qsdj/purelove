#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

#模块使用说明

docs = '''

#==============================================================================
#title                  :shellcode hex
#description            :shellcode hex
#author                 :mosin
#date                   :20170709
#version                :0.1
#usage                  :usage:  hex.py file.xxx
#notes                  :
#python_version         :2.7.5
#十六进制转化，shellcode生成器转换,用于将一些exe，dll,java,或者一些汇编代码类型的shellco
#de转化为：\x01\x52\x22,这种类型的，只有一个参数，target，其余参数设置无效
#参数设置：
# ple > set target d:/shellcode.bin
#==============================================================================

'''

from modules.exploit import BGExploit



class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "HEX",  # 该POC的名称
            "product": "HEX",  # 该POC所针对的应用名称,
            "product_version": "1.0",  # 应用的版本号
            "desc": '''
                十六进制转化，shellcode生成器转换
            ''',  # 该POC的描述
            "author": ["mosin"],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: ""},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2017-07-17",  # 漏洞公开时间
            "create_date": "2017-07-17",  # POC 创建时间
        }

        #自定义显示参数
        self.register_option({
            "target": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "文件存在路径",
                "Required":"no"
            },
            "port": {
                "default": "",
                "convert": self.convert.int_field,
                "desc": "端口",
                "Required":""
            },
            "debug": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "用于调试，排查poc中的问题",
                "Required":""
            },
            "mode": {
                "default": "payload",
                "convert": self.convert.str_field,
                "desc": "执行exploit,或者执行payload",
                "Required":""
            }
        })
        
        #自定义返回内容
        self.register_result({
            #检测标志位，成功返回置为True,失败返回False
            "status": False,
            "exp_status":False, #exploit，攻击标志位，成功返回置为True,失败返回False
            #定义返回的数据，用于打印获取到的信息
            "data": {

            },
            #程序返回信息
            "description": "",
            "error": "HEX FALSE"
        })


    def payload(self):
        
        files = self.option.target['default']
        shellcode = "\""
	ctr = 1
	maxlen = 15 #to create rows
	#read file
	try:
            for b in open(files, "rb").read():
                    shellcode += "\\x" + b.encode("hex")
                    if ctr == maxlen:
                            shellcode += "\" \n\""
                            ctr = 0
                    ctr += 1
            shellcode += "\""
            print "Code length: " + str(len(shellcode))
            #search null bytes
            print "Null byte found: " + str(len([n for n in xrange(len(shellcode)) if shellcode.find('\\x00', n) == n]))
            print
            print shellcode
        except:
            print "转换失败，请检查!"


    def exploit(self):
        payload()



#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())