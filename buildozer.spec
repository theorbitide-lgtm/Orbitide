[app]
title = ORBITIDE
package.name = orbitide
package.domain = org.orbitide

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True`

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
