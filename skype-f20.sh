#!/bin/sh

export LD_PRELOAD=/usr/lib/libGL.so.1
export PULSE_LATENCY_MSEC=30
exec skype-bin
