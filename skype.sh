#!/bin/sh

export LD_PRELOAD=/usr/lib/libGL.so.1
exec skype-bin "$@"
