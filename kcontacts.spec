#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kcontacts
Version  : 6.0.0
Release  : 71
URL      : https://download.kde.org/stable/frameworks/6.0/kcontacts-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kcontacts-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kcontacts-6.0.0.tar.xz.sig
Summary  : Address book API for KDE
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 MIT Unicode-DFS-2016
Requires: kcontacts-data = %{version}-%{release}
Requires: kcontacts-lib = %{version}-%{release}
Requires: kcontacts-license = %{version}-%{release}
Requires: kcontacts-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KContacts
Support for vCard contacts
## Introduction
KContact provides an API for contacts/address book data following the
vCard standard (RFC 2425 / RFC 2426).

%package data
Summary: data components for the kcontacts package.
Group: Data

%description data
data components for the kcontacts package.


%package dev
Summary: dev components for the kcontacts package.
Group: Development
Requires: kcontacts-lib = %{version}-%{release}
Requires: kcontacts-data = %{version}-%{release}
Provides: kcontacts-devel = %{version}-%{release}
Requires: kcontacts = %{version}-%{release}

%description dev
dev components for the kcontacts package.


%package lib
Summary: lib components for the kcontacts package.
Group: Libraries
Requires: kcontacts-data = %{version}-%{release}
Requires: kcontacts-license = %{version}-%{release}

%description lib
lib components for the kcontacts package.


%package license
Summary: license components for the kcontacts package.
Group: Default

%description license
license components for the kcontacts package.


%package locales
Summary: locales components for the kcontacts package.
Group: Default

%description locales
locales components for the kcontacts package.


%prep
%setup -q -n kcontacts-6.0.0
cd %{_builddir}/kcontacts-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709309517
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709309517
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcontacts
cp %{_builddir}/kcontacts-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcontacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcontacts-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcontacts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcontacts-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcontacts/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcontacts-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kcontacts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/kcontacts-%{version}/LICENSES/Unicode-DFS-2016.txt %{buildroot}/usr/share/package-licenses/kcontacts/561dfb2bb911e1d346abe66027b594bd2a400d27 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcontacts6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kcontacts.categories
/usr/share/qlogging-categories6/kcontacts.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KContacts/KContacts/Address
/usr/include/KF6/KContacts/KContacts/AddressFormat
/usr/include/KF6/KContacts/KContacts/Addressee
/usr/include/KF6/KContacts/KContacts/AddresseeList
/usr/include/KF6/KContacts/KContacts/CalendarUrl
/usr/include/KF6/KContacts/KContacts/ClientPidMap
/usr/include/KF6/KContacts/KContacts/ContactGroup
/usr/include/KF6/KContacts/KContacts/ContactGroupTool
/usr/include/KF6/KContacts/KContacts/Email
/usr/include/KF6/KContacts/KContacts/FieldGroup
/usr/include/KF6/KContacts/KContacts/Gender
/usr/include/KF6/KContacts/KContacts/Geo
/usr/include/KF6/KContacts/KContacts/Impp
/usr/include/KF6/KContacts/KContacts/Key
/usr/include/KF6/KContacts/KContacts/LDIFConverter
/usr/include/KF6/KContacts/KContacts/Lang
/usr/include/KF6/KContacts/KContacts/Namespace
/usr/include/KF6/KContacts/KContacts/NickName
/usr/include/KF6/KContacts/KContacts/Note
/usr/include/KF6/KContacts/KContacts/Org
/usr/include/KF6/KContacts/KContacts/PhoneNumber
/usr/include/KF6/KContacts/KContacts/Picture
/usr/include/KF6/KContacts/KContacts/Related
/usr/include/KF6/KContacts/KContacts/ResourceLocatorUrl
/usr/include/KF6/KContacts/KContacts/Role
/usr/include/KF6/KContacts/KContacts/Secrecy
/usr/include/KF6/KContacts/KContacts/Sound
/usr/include/KF6/KContacts/KContacts/TimeZone
/usr/include/KF6/KContacts/KContacts/Title
/usr/include/KF6/KContacts/KContacts/VCardConverter
/usr/include/KF6/KContacts/KContacts/VCardDrag
/usr/include/KF6/KContacts/kcontacts/address.h
/usr/include/KF6/KContacts/kcontacts/addressee.h
/usr/include/KF6/KContacts/kcontacts/addresseelist.h
/usr/include/KF6/KContacts/kcontacts/addressformat.h
/usr/include/KF6/KContacts/kcontacts/calendarurl.h
/usr/include/KF6/KContacts/kcontacts/clientpidmap.h
/usr/include/KF6/KContacts/kcontacts/contactgroup.h
/usr/include/KF6/KContacts/kcontacts/contactgrouptool.h
/usr/include/KF6/KContacts/kcontacts/email.h
/usr/include/KF6/KContacts/kcontacts/fieldgroup.h
/usr/include/KF6/KContacts/kcontacts/gender.h
/usr/include/KF6/KContacts/kcontacts/geo.h
/usr/include/KF6/KContacts/kcontacts/impp.h
/usr/include/KF6/KContacts/kcontacts/kcontacts_export.h
/usr/include/KF6/KContacts/kcontacts/key.h
/usr/include/KF6/KContacts/kcontacts/lang.h
/usr/include/KF6/KContacts/kcontacts/ldifconverter.h
/usr/include/KF6/KContacts/kcontacts/namespace.h
/usr/include/KF6/KContacts/kcontacts/nickname.h
/usr/include/KF6/KContacts/kcontacts/note.h
/usr/include/KF6/KContacts/kcontacts/org.h
/usr/include/KF6/KContacts/kcontacts/phonenumber.h
/usr/include/KF6/KContacts/kcontacts/picture.h
/usr/include/KF6/KContacts/kcontacts/related.h
/usr/include/KF6/KContacts/kcontacts/resourcelocatorurl.h
/usr/include/KF6/KContacts/kcontacts/role.h
/usr/include/KF6/KContacts/kcontacts/secrecy.h
/usr/include/KF6/KContacts/kcontacts/sound.h
/usr/include/KF6/KContacts/kcontacts/timezone.h
/usr/include/KF6/KContacts/kcontacts/title.h
/usr/include/KF6/KContacts/kcontacts/vcardconverter.h
/usr/include/KF6/KContacts/kcontacts/vcarddrag.h
/usr/include/KF6/KContacts/kcontacts_version.h
/usr/lib64/cmake/KF6Contacts/KF6ContactsConfig.cmake
/usr/lib64/cmake/KF6Contacts/KF6ContactsConfigVersion.cmake
/usr/lib64/cmake/KF6Contacts/KF6ContactsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Contacts/KF6ContactsTargets.cmake
/usr/lib64/libKF6Contacts.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Contacts.so.6.0.0
/usr/lib64/libKF6Contacts.so.6
/usr/lib64/libKF6Contacts.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcontacts/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcontacts/561dfb2bb911e1d346abe66027b594bd2a400d27
/usr/share/package-licenses/kcontacts/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcontacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcontacts/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3

%files locales -f kcontacts6.lang
%defattr(-,root,root,-)

