[Package Name]
Name=oglib_dictionary
Version=1.1
Release=1

[Description]
Description="The dictionary package contains a library for key-value sets."
Summary="OpenG Dictionary"
License=BSD
Copyright="2005 Jim Kring"
Distribution="OpenG Toolkit"
Icon=dictionary.bmp
Vendor=OpenG.org
URL=http://opengtoolkit.sourceforge.net/array
Packager="Jim Kring <jim@jimkring.com>"

[Platform]
Exclusive_LabVIEW_Version=>=6.1
Exclusive_LabVIEW_System=All
Exclusive_OS=All

[Script VIs]
Source Dir=""
PreInstall=""
PostInstall=""
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""

[Dependencies]
AutoReqProv=FALSE
Requires="ogrsc_dynamicpalette>=2.0, nirsc_html_help_common>=1.0"
Conflicts=""

[Files]
Num File Groups=5

[File Group 0]
Source Dir=built/dictionary
Target Dir=<OpenG.lib>/dictionary
Replace Mode=Always

Num Files=41

File 0=dictionary.llb/Dictionary - VI Tree__ogtk.vi
File 1=dictionary.llb/Dictionary Clear__ogtk.vi
File 2=dictionary.llb/Dictionary Close Object Reference__ogtk.vi
File 3=dictionary.llb/Dictionary Copy__ogtk.vi
File 4=dictionary.llb/Dictionary Core - VI Tree__ogtk.vi
File 5=dictionary.llb/Dictionary Create__ogtk.vi
File 6=dictionary.llb/Dictionary Data Core__ogtk.vi
File 7=dictionary.llb/Dictionary Data Store VI Name__ogtk.vi
File 8=dictionary.llb/Dictionary Data__ogtk.ctl
File 9=dictionary.llb/Dictionary Default Data__ogtk.vi
File 10=dictionary.llb/Dictionary Delete Element__ogtk.vi
File 11=dictionary.llb/Dictionary Delete__ogtk.vi
File 12=dictionary.llb/Dictionary Destroy__ogtk.vi
File 13=dictionary.llb/Dictionary Flatten Object to File__ogtk.vi
File 14=dictionary.llb/Dictionary Get Data to Modify__ogtk.vi
File 15=dictionary.llb/Dictionary Get Data__ogtk.vi
File 16=dictionary.llb/Dictionary Get Instance Semaphore RefNum__ogtk.vi
File 17=dictionary.llb/Dictionary Get Items__ogtk.vi
File 18=dictionary.llb/Dictionary Get Keys__ogtk.vi
File 19=dictionary.llb/Dictionary Get Status__ogtk.vi
File 20=dictionary.llb/Dictionary Get Value__ogtk.vi
File 21=dictionary.llb/Dictionary Get Values__ogtk.vi
File 22=dictionary.llb/Dictionary Has Key__ogtk.vi
File 23=dictionary.llb/Dictionary Key Value Pair Cluster__ogtk.ctl
File 24=dictionary.llb/Dictionary New__ogtk.vi
File 25=dictionary.llb/Dictionary Not a Dictionary__ogtk.vi
File 26=dictionary.llb/Dictionary Object Data Core Task Enum__ogtk.ctl
File 27=dictionary.llb/Dictionary Object Data Store VI Ref Type__ogtk.vi
File 28=dictionary.llb/Dictionary Object Data Store__ogtk.vi
File 29=dictionary.llb/Dictionary Object Ref Type__ogtk.vi
File 30=dictionary.llb/Dictionary Object RefNum - Enum__ogtk.ctl
File 31=dictionary.llb/Dictionary Object RefNum__ogtk.ctl
File 32=dictionary.llb/Dictionary Open Object Reference__ogtk.vi
File 33=dictionary.llb/Dictionary Pop Item__ogtk.vi
File 34=dictionary.llb/Dictionary Set Modified Data__ogtk.vi
File 35=dictionary.llb/Dictionary Unflatten Object from File__ogtk.vi
File 36=dictionary.llb/Dictionary Update (by reference)__ogtk.vi
File 37=dictionary.llb/Dictionary Update (by scalar value)__ogtk.vi
File 38=dictionary.llb/Dictionary Update (by value)__ogtk.vi
File 39=dictionary.llb/Dictionary Update (poly)__ogtk.vi
File 40=dictionary.llb/Dictionary Update__ogtk.vi


[File Group 1]
Source Dir="Dynamic Palette MNUs"
Target Dir=<user.lib>/_dynamicpalette_dirs/adv
Replace Mode=Always
Num Files=1
File 0=oglib_dictionary.mnu

[File Group 2]
Source Dir="Dynamic Palette MNUs"
Target Dir=<user.lib>/_dynamicpalette_dirs/OpenG
Replace Mode=Always
Num Files=1
File 0=oglib_dictionary.mnu

[File Group 3]
Source Dir=built/help
Target Dir=<help>/OpenG/dictionary
Replace Mode=Always
Num Files=1
File 0=*.*

[File Group 4]
Source Dir=Examples
Target Dir=<application>/examples/OpenG/dictionary
Replace Mode=Always
Num Files=1
File 0=*.*