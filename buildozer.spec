[app]

# (str) Title of your application
title = Lunaro AI

# (str) Package name
package.name = lunaroai

# (str) Package domain (needed for android/ios packaging)
package.domain = com.lunaro

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,pillow
android.permissions = INTERNET

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (str) Icon of the application
icon.filename = icon.png

# (str) Presplash of the application
presplash.filename = presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# For 32-bit only (most compatible):
# android.archs = armeabi-v7a

# For 64-bit only:
# android.archs = arm64-v8a

# For both 32-bit and 64-bit (universal, larger file):
 android.archs = armeabi-v7a,arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Skip byte compile for .py files
android.no-byte-compile-python = False

# (str) XML file for additional android manifest entries
# android.manifest.intent_filters = 

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
# android.whitelist = 

# (str) Path to a custom whitelist file
# android.whitelist_src = 

# (str) Path to a custom blacklist file
# android.blacklist_src = 

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) The Android arch to build for, in the format "architecture_ABI"
# where architecture is one of: x86, armeabi-v7a, arm64-v8a, x86_64
# and ABI is the Android ABI. The default is armeabi-v7a.
# Note that some older Android versions do not support all architectures.
# android.arch = armeabi-v7a


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#    [app@demo]
#    title = My Application (demo)
#
#    [app:source.exclude_patterns@demo]
#    images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#    buildozer --profile demo android debug
