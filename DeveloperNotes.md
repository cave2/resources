#CAVE2 Developer Notes

This is a starting point for our developer documentation for the CAVE2 platform.

[TOC]

##Omegalib

###Resources
https://groups.google.com/forum/#!forum/omegalib
https://github.com/uic-evl/omegalib/wiki

###C++ Omegalib applications
Follow https://github.com/uic-evl/omegalib/wiki/NewApplication
Recommend using Solution 1, building an external application

Within the standard CAVE2 environment, assuming your CMakeLists.txt is correct,
steps to build your application are:
```
setenv Omegalib_DIR "/cave/omegalib/install"
cmake .
make
```

Example replacement CMakeLists.txt for the **ohello** application allow stand-alone build:
```
cmake_minimum_required(VERSION 2.8.1) 
project(ohello)

find_package(Omegalib)

# Source and header files
SET( srcs 
       ohello.cpp 
    )
SET( headers  
    )

# Setup compile info
include_directories(${OMEGA_INCLUDE_DIRS})
add_executable(ohello ${srcs} ${headers})
target_link_libraries(ohello ${OMEGA_LIB})
#Add other libraries you might need in above line:
#{OMEGA_TOOLKIT_LIB} {OMEGA_OSG_LIB} {OMEGA_CYCLOPS_LIB} {OMEGA_VTK_LIB}
```

###Python Omegalib applications

https://github.com/uic-evl/omegalib/wiki/Python-Reference

###Omegalib tips & tricks
If Omegalib apps segfault when started it is likely you don't have write access to the working directory, particularly **AppName.log** and **_eqcfg.eqc** must be writable.

##SAGE

###Building C/C++ applications for SAGE
