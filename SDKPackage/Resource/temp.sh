#!/usr/bin/env bash
cd /Users/huangjian/Documents/GitLab/GFSDKMainland_Main/GFSDKMainLand/DerivedData/Build/Products/Release-iphoneos/
shopt -s extglob
rm -rf !(GameFriendSDK.framework)
cd GameFriendSDK.framework
rm -rf !(GameFriendSDK|Headers|SDKResource.bundle)