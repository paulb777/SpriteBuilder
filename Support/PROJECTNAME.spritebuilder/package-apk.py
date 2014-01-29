#! /usr/bin/env python

#  package-apk.py
#  PROJECTNAME
#
#  Created by Paul Beusterien on 1/27/14.
#  Copyright (c) 2014 Apportable. All rights reserved.


# Should be a Build post-action

import zipfile
import os
import datetime

home = os.environ['HOME'];

os.system('touch ' + home + '/tmp/fooo')

sdk = home + "/.apportable/"
appName = "PROJECTNAME"
tmpdir = os.path.join('/tmp', datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(tmpdir)

# TODO this list should be generated from specified libs
sos = ["libFoundation.so", "libv.so", "libcxx.so", "libSystem.so", "libffi.so", "libBridgeKit.so", "libOpenAL.so", "libfreetype.so", "libCoreGraphics.so", "libCoreText.so", "libCommonCrypto.so", "libcrypto_1_01f.so", "libssl_1_01f.so", "libSecurity.so", "libicu.so", "libCFNetwork.so", "libCoreFoundation.so", "libSystemConfiguration.so", "libCoreAudio.so", "libAudioFile.so", "libAudioUnit.so", "libAudioToolbox.so"]

try:
    product_dir = os.environ['SYMROOT'] + "/Debug-iphonesimulator/PROJECTNAME-android.app"
except KeyError:
    # running from command line
    product_dir = os.environ['HOME'] + '/Library/Developer/Xcode/DerivedData/PROJECTNAME-hirkszrbtaozdbbjailjglgjifsj/Build/Products/Debug-iphonesimulator/PROJECTNAME-android.app'

libverde = product_dir + "/PROJECTNAME-android"
gdbserver = sdk + "toolchain/macosx/gdb/share/remote/android/arm/gdbserver"

# TODO transform Spin-Info.plist to Info.plist
os.system('touch ' + home + '/tmp/fooo4')
attribution = sdk + 'SDK/System/ATTRIBUTION.txt'

try:
    os.system('touch ' + home + '/tmp/foooea')
    os.remove('/Users/paulbeusterien/tmp/PROJECTNAME-unaligned.apk')
    os.system('touch ' + home + '/tmp/foooeb')
except OSError as e:
    pass

os.system('touch ' + home + '/tmp/fooo5')

target_dir = '/Users/paulbeusterien/ppp-unzip'
zip = zipfile.ZipFile('/Users/paulbeusterien/tmp/' + appName + '-unaligned.apk', 'w', zipfile.ZIP_DEFLATED)
rootlen = len(target_dir) + 1
for base, dirs, files in os.walk(target_dir):
    for fi in files:
        fn = os.path.join(base, fi)
        zip.write(fn, fn[rootlen:])

for so in sos:
    zip.write(sdk + "SDK/sysroot/android/armeabi/usr/lib/" + so, "lib/armeabi/" + so)

rootlen = len(product_dir) + 1
for base, dirs, files in os.walk(product_dir):
    for file in files:
        #        print 'file is ' + file
        if file == 'Info.plist':
           zip.write('/Users/paulbeusterien/.apportable/SDK/Build/android-armeabi-debug/PeevedPenguinsPaul/tmp/assets/Info.plist', "assets/Info.plist")
        elif file.endswith('.nib'):
            print "nibs not yet supported"
            zip.write('/Users/paulbeusterien/backup/assets-save/SpinViewController.xib', "assets/SpinViewController.xib")
        elif file != 'PROJECTNAME-android' and file != 'PkgInfo':
            fn = os.path.join(base, file)
            zip.write(fn, "assets/" + fn[rootlen:])

os.system('echo ' + gdbserver + ' > ' + home + '/tmp/fooo1')

zip.write(gdbserver, "lib/armeabi/gdbserver")
zip.write(libverde, "lib/armeabi/libverde.so")
#zip.write('/Users/paulbeusterien/.apportable/SDK/Build/android-armeabi-debug/PROJECTNAME/tmp/lib/armeabi/libverde.so', "lib/armeabi/libverde.so")
os.system('touch ' + home + '/tmp/fooo12')
zip.write(attribution, "ATTRIBUTION.txt")
os.system('touch ' + home + '/tmp/fooo13')
zip.close()
os.system('touch ' + home + '/tmp/fooo14')
os.system('touch ' + home + '/tmp/fooo2')
jarsigner = ['jarsigner', '-sigalg', 'MD5withRSA', '-digestalg', 'SHA1', '-storepass', 'android', '-keystore', home + '/.android/debug.keystore', home + '/tmp/' + appName + '-unaligned.apk', 'androiddebugkey']
os.system(' '.join(jarsigner))
os.system('touch ' + home + '/tmp/fooo3')
# TODO real spot for apk file for here and run script - use a directory available from env
zipalign = [home + '/.apportable/SDK/toolchain/macosx/android-sdk/tools/zipalign', '-f', '4', home + '/tmp/' + appName + '-unaligned.apk', home + '/tmp/' + appName + '-debug.apk']
os.system(' '.join(zipalign))
os.system('touch ' + home + '/tmp/fooo4')
