#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcontacts
Version  : 19.04.2
Release  : 11
URL      : https://download.kde.org/stable/applications/19.04.2/src/kcontacts-19.04.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.2/src/kcontacts-19.04.2.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.2/src/kcontacts-19.04.2.tar.xz.sig
Summary  : Address book API for KDE
Group    : Development/Tools
License  : LGPL-2.1
Requires: kcontacts-data = %{version}-%{release}
Requires: kcontacts-lib = %{version}-%{release}
Requires: kcontacts-license = %{version}-%{release}
Requires: kcontacts-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : pkgconfig(iso-codes)
BuildRequires : qtbase-dev mesa-dev

%description
KContacts - new address book API for KDE
PURPOSE:
KCcontacts provides an API for address book data. This can be used by all
application using data of this type, e.g. KAddressBook, KMail, KOrganizer,
etc.

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
%setup -q -n kcontacts-19.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559886243
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1559886243
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcontacts
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kcontacts/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kcontacts5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kcontacts.categories
/usr/share/xdg/kcontacts.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KContacts/KContacts/Address
/usr/include/KF5/KContacts/KContacts/Addressee
/usr/include/KF5/KContacts/KContacts/AddresseeList
/usr/include/KF5/KContacts/KContacts/CalendarUrl
/usr/include/KF5/KContacts/KContacts/ClientPidMap
/usr/include/KF5/KContacts/KContacts/ContactGroup
/usr/include/KF5/KContacts/KContacts/ContactGroupTool
/usr/include/KF5/KContacts/KContacts/Email
/usr/include/KF5/KContacts/KContacts/Field
/usr/include/KF5/KContacts/KContacts/FieldGroup
/usr/include/KF5/KContacts/KContacts/Gender
/usr/include/KF5/KContacts/KContacts/Geo
/usr/include/KF5/KContacts/KContacts/Impp
/usr/include/KF5/KContacts/KContacts/Key
/usr/include/KF5/KContacts/KContacts/LDIFConverter
/usr/include/KF5/KContacts/KContacts/Lang
/usr/include/KF5/KContacts/KContacts/NickName
/usr/include/KF5/KContacts/KContacts/Note
/usr/include/KF5/KContacts/KContacts/Org
/usr/include/KF5/KContacts/KContacts/PhoneNumber
/usr/include/KF5/KContacts/KContacts/Picture
/usr/include/KF5/KContacts/KContacts/Related
/usr/include/KF5/KContacts/KContacts/ResourceLocatorUrl
/usr/include/KF5/KContacts/KContacts/Role
/usr/include/KF5/KContacts/KContacts/Secrecy
/usr/include/KF5/KContacts/KContacts/SortMode
/usr/include/KF5/KContacts/KContacts/Sound
/usr/include/KF5/KContacts/KContacts/TimeZone
/usr/include/KF5/KContacts/KContacts/Title
/usr/include/KF5/KContacts/KContacts/VCardConverter
/usr/include/KF5/KContacts/KContacts/VCardDrag
/usr/include/KF5/KContacts/kcontacts/address.h
/usr/include/KF5/KContacts/kcontacts/addressee.h
/usr/include/KF5/KContacts/kcontacts/addresseelist.h
/usr/include/KF5/KContacts/kcontacts/calendarurl.h
/usr/include/KF5/KContacts/kcontacts/clientpidmap.h
/usr/include/KF5/KContacts/kcontacts/contactgroup.h
/usr/include/KF5/KContacts/kcontacts/contactgrouptool.h
/usr/include/KF5/KContacts/kcontacts/email.h
/usr/include/KF5/KContacts/kcontacts/field.h
/usr/include/KF5/KContacts/kcontacts/fieldgroup.h
/usr/include/KF5/KContacts/kcontacts/gender.h
/usr/include/KF5/KContacts/kcontacts/geo.h
/usr/include/KF5/KContacts/kcontacts/impp.h
/usr/include/KF5/KContacts/kcontacts/kcontacts_export.h
/usr/include/KF5/KContacts/kcontacts/key.h
/usr/include/KF5/KContacts/kcontacts/lang.h
/usr/include/KF5/KContacts/kcontacts/ldifconverter.h
/usr/include/KF5/KContacts/kcontacts/nickname.h
/usr/include/KF5/KContacts/kcontacts/note.h
/usr/include/KF5/KContacts/kcontacts/org.h
/usr/include/KF5/KContacts/kcontacts/phonenumber.h
/usr/include/KF5/KContacts/kcontacts/picture.h
/usr/include/KF5/KContacts/kcontacts/related.h
/usr/include/KF5/KContacts/kcontacts/resourcelocatorurl.h
/usr/include/KF5/KContacts/kcontacts/role.h
/usr/include/KF5/KContacts/kcontacts/secrecy.h
/usr/include/KF5/KContacts/kcontacts/sortmode.h
/usr/include/KF5/KContacts/kcontacts/sound.h
/usr/include/KF5/KContacts/kcontacts/timezone.h
/usr/include/KF5/KContacts/kcontacts/title.h
/usr/include/KF5/KContacts/kcontacts/vcardconverter.h
/usr/include/KF5/KContacts/kcontacts/vcarddrag.h
/usr/include/KF5/kcontacts_version.h
/usr/lib64/cmake/KF5Contacts/KF5ContactsConfig.cmake
/usr/lib64/cmake/KF5Contacts/KF5ContactsConfigVersion.cmake
/usr/lib64/cmake/KF5Contacts/KF5ContactsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Contacts/KF5ContactsTargets.cmake
/usr/lib64/libKF5Contacts.so
/usr/lib64/qt5/mkspecs/modules/qt_KContacts.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Contacts.so.5
/usr/lib64/libKF5Contacts.so.5.11.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcontacts/COPYING.LIB

%files locales -f kcontacts5.lang
%defattr(-,root,root,-)

