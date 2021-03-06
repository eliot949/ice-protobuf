#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# **********************************************************************

import os, sys, traceback, time, threading
import Ice

Ice.loadSlice('Test.ice')
import Test
from Test_pb2 import Message

class MyClassI(Test.MyClass):
    def opMessage(self, m, current=None):
        return (m, m)

    def opMessageAMD_async(self, cb, m, current=None):
        cb.ice_response(m, m);

    def shutdown(self, current=None):
        current.adapter.getCommunicator().shutdown()

def run(args, communicator):
    communicator.getProperties().setProperty("TestAdapter.Endpoints", "default -p 12010:udp")
    adapter = communicator.createObjectAdapter("TestAdapter")
    adapter.add(MyClassI(), communicator.stringToIdentity("test"))
    adapter.activate()
    communicator.waitForShutdown()
    return True

try:
    initData = Ice.InitializationData()
    initData.properties = Ice.createProperties(sys.argv)
    communicator = Ice.initialize(sys.argv, initData)
    status = run(sys.argv, communicator)
except:
    traceback.print_exc()
    status = False

if communicator:
    try:
        communicator.destroy()
    except:
        traceback.print_exc()
        status = False

sys.exit(not status)
