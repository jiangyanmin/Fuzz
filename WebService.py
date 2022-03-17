# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import sys


if "IronPython" in str(sys.version):
    def http_check(ctx):
        fault_code = ""
        fault_string = ""
        if os.path.exists("temp/rest/check.properties"):
            with open("temp/rest/check.properties", "r") as f:
                for line in f:
                    strings = line.strip().split("=")
                    if strings[0].strip() == "fault_code":
                        fault_code = strings[1].strip()
                    elif strings[1].strip() == "fault_string":
                        fault_string = strings[1].strip()
        if ctx.dataModel.find('RespCode'):
            response_code = str(ctx.dataModel.find('RespCode').DefaultValue)
            for code in fault_code.split("|"):
                if code != "":
                    if response_code.find(code) >= 0:
                        return False
        if ctx.dataModel.find('Payload'):
            payload = str(ctx.dataModel.find('Payload').DefaultValue)
            # payload
            for str_ in fault_string.split("|"):
                if str_ != "":
                    if payload.find(str_) >= 0:
                        return False
        return True

else:
    def http_check(ctx):
        fault_code = ""
        fault_string = ""
        if os.path.exists("../../../temp/rest/check.properties"):
            with open("../../../temp/rest/check.properties", "r") as f:
                for line in f:
                    strings = line.strip().split("=")
                    if strings[0].strip() == "fault_code":
                        fault_code = strings[1].strip()
                    elif strings[1].strip() == "fault_string":
                        fault_string = strings[1].strip()
        if ctx.dataModel.find('RespCode'):
            response_code = str(ctx.dataModel.find('RespCode').value)
            for code in fault_code.split("|"):
                if code != "":
                    if response_code.find(code) >= 0:
                        return False
        if ctx.dataModel.find('Payload'):
            payload = str(ctx.dataModel.find('Payload').value)
            # payload
            for str_ in fault_string.split("|"):
                if str_ != "":
                    if payload.find(str_) >= 0:
                        return False
        return True


def set_to_store_g(ctx, **kwarg):
    for k, v in kwarg.items():
        ctx.parent.parent.parent.context.stateStore[k] = v
        return True


def get_store_val_g(ctx, name):
    if name in ctx.parent.parent.parent.context.stateStore:
        return ctx.parent.parent.parent.context.stateStore[name]
    else:
        return False
