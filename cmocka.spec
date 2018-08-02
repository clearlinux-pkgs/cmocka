#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmocka
Version  : 1.1.1
Release  : 4
URL      : https://cmocka.org/files/1.1/cmocka-1.1.1.tar.xz
Source0  : https://cmocka.org/files/1.1/cmocka-1.1.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cmocka-lib
Requires: cmocka-license
BuildRequires : buildreq-cmake
BuildRequires : doxygen

%description
CMOCKA
=======
cmocka is a fork for Google's cmockery unit testing framework to fix bugs and
support it in future.
See https://code.google.com/p/cmockery/

%package dev
Summary: dev components for the cmocka package.
Group: Development
Requires: cmocka-lib
Provides: cmocka-devel

%description dev
dev components for the cmocka package.


%package lib
Summary: lib components for the cmocka package.
Group: Libraries
Requires: cmocka-license

%description lib
lib components for the cmocka package.


%package license
Summary: license components for the cmocka package.
Group: Default

%description license
license components for the cmocka package.


%prep
%setup -q -n cmocka-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533180824
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1533180824
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cmocka
cp COPYING %{buildroot}/usr/share/doc/cmocka/COPYING
cp cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/cmocka/cmake_Modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/cmake/cmocka/cmocka-config-version.cmake
/usr/lib64/cmake/cmocka/cmocka-config.cmake
/usr/lib64/libcmocka.so
/usr/lib64/pkgconfig/cmocka.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcmocka.so.0
/usr/lib64/libcmocka.so.0.4.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/cmocka/COPYING
/usr/share/doc/cmocka/cmake_Modules_COPYING-CMAKE-SCRIPTS
