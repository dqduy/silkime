@echo off

rem Current dir
rem	Host type
rem Build type: all, release, debug

set BUILD_TYPE=release

python scripts/build.py %CD% windows %BUILD_TYPE%

rem Notice 
rem JAVA_HOME, PYTHON, ANDROID_HOME