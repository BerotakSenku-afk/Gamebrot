# buildozer.spec - Brick Blaster Game
# Sudah diperbaiki dan dioptimasi untuk GitHub Actions CI/CD
# ============================================================

[app]

# (str) Judul aplikasi
title = Brick Blaster

# (str) Nama package (huruf kecil, tanpa spasi)
package.name = brickblaster

# (str) Domain package
package.domain = org.game

# (str) Lokasi source code (dimana main.py berada)
source.dir = .

# (list) Ekstensi file yang diikutkan dalam build
# PERBAIKAN: Ditambah ttf, ogg, wav, mp3 untuk font & audio
source.include_exts = py,png,jpg,kv,atlas,ttf,ogg,wav,mp3

# (list) File/folder yang dikecualikan dari build
source.exclude_dirs = tests, bin, venv, .buildozer, .git, __pycache__

# (str) Versi aplikasi
version = 0.1

# (list) Requirements / dependensi aplikasi
requirements = python3,kivy

# (str) Gambar presplash (layar loading)
# PENTING: Pastikan file ini benar-benar ada di repo!
presplash.filename = %(source.dir)s/data/ikon.png

# (str) Icon aplikasi
# PENTING: Pastikan file ini benar-benar ada di repo!
icon.filename = %(source.dir)s/data/ikon.png

# (list) Orientasi layar
orientation = portrait

# (bool) Fullscreen atau tidak
fullscreen = 0

# (str) Warna background presplash
android.presplash_color = #000000


# ============================================================
# ANDROID SPECIFIC
# ============================================================

# (list) Permission yang dibutuhkan aplikasi
android.permissions = android.permission.INTERNET, android.permission.VIBRATE, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)

# (int) Target Android API (setinggi mungkin)
android.api = 33

# (int) Minimum API yang didukung
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
# PERBAIKAN: 25b = NDK 25.2.9519653 (stabil & match dengan workflow)
android.ndk = 25b

# (str) Versi build tools
# PERBAIKAN: Diganti ke 33.0.2 (lebih stabil dari 33.0.1)
android.build_tools_version = 33.0.2

# (int) Android NDK API (biasanya sama dengan minapi)
android.ndk_api = 21

# (bool) PERBAIKAN KRITIS: Hapus spasi di depan baris ini!
# Spasi di depan = buildozer mengabaikan setting ini!
android.accept_sdk_license = True

# (list) Arsitektur yang didukung
# arm64-v8a = HP modern 64-bit
# armeabi-v7a = HP lama 32-bit
android.archs = arm64-v8a, armeabi-v7a

# (bool) Skip update SDK (set True untuk mempercepat CI/CD)
# android.skip_update = False

# (bool) Izinkan auto backup Android
android.allow_backup = True

# (str) Entrypoint Android (default ok untuk Kivy)
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android logcat filter untuk debugging
#android.logcat_filters = *:S python:D

# (str) Warna latar splash screen (opsional)
#android.presplash_color = #FFFFFF

# (str) Format output debug (apk atau aar)
# android.debug_artifact = apk

# (str) Format output release (aab atau apk)
# android.release_artifact = aab

# (str) Launch mode activity
#android.manifest.launch_mode = standard


# ============================================================
# PYTHON FOR ANDROID (p4a)
# ============================================================

# (str) Branch p4a yang digunakan
#p4a.branch = master

# (str) Bootstrap yang digunakan (sdl2 = default untuk Kivy)
# p4a.bootstrap = sdl2


# ============================================================
# OSX SPECIFIC (abaikan jika tidak build untuk macOS)
# ============================================================
osx.kivy_version = 2.2.0


# ============================================================
# iOS SPECIFIC (abaikan jika tidak build untuk iOS)
# ============================================================
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
ios.codesign.allowed = false


# ============================================================
# BUILDOZER SETTINGS
# ============================================================

[buildozer]

# (int) Level log: 0=error saja, 1=info, 2=debug lengkap
log_level = 2

# (int) Tampilkan warning jika dijalankan sebagai root
warn_on_root = 1

# (str) Folder output build artifacts
# build_dir = ./.buildozer

# (str) Folder output APK/AAB
# bin_dir = ./bin
