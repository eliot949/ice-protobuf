// **********************************************************************
//
// Copyright (c) 2003-2015 ZeroC, Inc. All rights reserved.
//
// **********************************************************************

#ifndef HELLO_I_H
#define HELLO_I_H

#include <Hello.h>

class HelloI : public Demo::Hello
{
public:

    virtual void sayHello(const tutorial::Person& p, const Ice::Current&);
    virtual void shutdown(const Ice::Current&);
};

#endif
