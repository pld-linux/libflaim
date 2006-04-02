#
# spec file for package libflaim (Version 4.8.61)
#
# Copyright (c) 2006 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://support.novell.com
#

# neededforbuild  gcc-c++ libstdc++ libstdc++-devel

BuildRequires:  aaa_base acl attr bash bind-utils bison bzip2 coreutils cpio cpp cracklib cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel gettext-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv klogd less libacl libattr libcom_err libgcc libnscd libselinux libstdc++ libxcrypt libzio m4 make man mktemp module-init-tools ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-modules patch permissions popt procinfo procps psmisc pwdutils rcs readline sed strace sysvinit tar tcpd texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils gcc gcc-c++ gdbm gettext libstdc++-devel libtool perl rpm

Name:           libflaim
URL:            http://forge.novell.com/modules/xfmod/project/?flaim
%define prefix /usr
Summary:        Embeddable cross-platform database engine
Version:        4.8.61
Release:        1
License:        GPL
Group:          Development/Libraries/C and C++
Source:         libflaim-4.8.61.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine used
by Novell eDirectory. It has proven to be highly scalable, reliable,
and robust. It is available on a wide variety of 32 bit and 64 bit
platforms.



Authors:
--------
    Daniel Sanders
    Andrew Hodgkinson

%package devel
Summary:        Embeddable cross-platform database engine
Group:          Development/Libraries/C and C++
Provides:       libflaim-devel

%description devel
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine used
by Novell eDirectory. It has proven to be highly scalable, reliable,
and robust. It is available on a wide variety of 32 bit and 64 bit
platforms.



Authors:
--------
    Daniel Sanders
    Andrew Hodgkinson

%prep
%setup -q

%build
make lib_dir_name=%{_lib} libs

%install
make rpm_build_root=$RPM_BUILD_ROOT install_prefix=%{prefix} lib_dir_name=%{_lib} install
rm -rf build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING VERSION
%{prefix}/%{_lib}/libflaim-4.8.61.so
%{prefix}/%{_lib}/libflaim-4.8.so
%{prefix}/%{_lib}/libflaim-4.so
%{prefix}/%{_lib}/libflaim.so

%files devel
%{prefix}/%{_lib}/libflaim.a
%{prefix}/%{_lib}/pkgconfig/libflaim.pc
%{prefix}/include/flaim.h

%changelog -n libflaim
* Fri Feb 03 2006 - dsanders@novell.com
- Fixed libflaim.pc to specify includedir and Cflags:
- Also changed name: to Name:
- Modified Makefile to use macros for outputting $ and %% characters
* Fri Feb 03 2006 - dsanders@novell.com
- Added support for PowerPC architectures
- Changed so that revision number for RPMs will match version number
- in SVN repository.
* Wed Feb 01 2006 - dsanders@novell.com
- Initial submission
