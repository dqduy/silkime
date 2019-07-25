#!/usr/bin/env bash
#@echo off

#Current dir
#Host type
#Build type: all, release, debug

export BUILD_TYPE=release

python3 scripts/build.py $PWD linux $BUILD_TYPE

# Predefined Environment Variables
# JAVA_HOME, ANDROID_HOME, PYTHON3