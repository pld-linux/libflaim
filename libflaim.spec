#
# TODO:
# - correct linking:
#   Unresolved symbols found in libflaim.so.4.1:
#     keypad halfdelay meta
# - remove ldconfig invocation

Summary:	Embeddable cross-platform database engine
Summary(pl.UTF-8):	Osadzalny, wieloplatformowy silnik baz danych
Name:		libflaim
Version:	4.9.989
Release:	1
License:	(L?)GPL
Group:		Libraries
Source0:	http://forgeftp.novell.com/flaim/development/flaim/downloads/source/%{name}-%{version}.tar.gz
# Source0-md5:	cbd0caf6239cffb7640391eda7551d4a
Patch0:		%{name}-fix.patch
URL:		http://forge.novell.com/modules/xfmod/project/?flaim
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine
used by Novell eDirectory. It has proven to be highly scalable,
reliable, and robust. It is available on a wide variety of 32 bit and
64 bit platforms.

%description -l pl.UTF-8
FLAIM to osadzalny, wieloplatformowy silnik baz danych udostępniający
bogaty, potężny i łatwy w użyciu zbiór możliwości. Jest to silnik baz
danych używany przez Novell eDirectory. Sprawdził się jako wysoko
skalowalny, pewny i silny. Jest dostępny na wiele platform 32- i
64-bitowych.

%package devel
Summary:	Header files for libflaim library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libflaim
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libflaim library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libflaim.

%package static
Summary:	Static libflaim library
Summary(pl.UTF-8):	Statyczna biblioteka libflaim
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libflaim library.

%description static -l pl.UTF-8
Statyczna biblioteka libflaim.

%prep
%setup -q
%patch0 -p0
sed 's/ccflags += \(.*ccdefine.*ccinclude\)/ccflags += $(OPTCXXFLAGS) \1/' -i Makefile

%build
%{__make} libs \
	OSTYPE=%{_os} \
	HOSTTYPE=%{_arch} \
	ec= \
	compiler="%{__cxx}" exe_linker="%{__cxx}" shared_linker="%{__cxx}" \
	OPTCXXFLAGS="-Wall -fPIC %{rpmcxxflags}" \

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	OSTYPE=%{_os} \
	HOSTTYPE=%{_arch} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING VERSION
%attr(755,root,root) %{_libdir}/libflaim.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libflaim.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflaim.so
%{_includedir}/*.h
%{_pkgconfigdir}/libflaim.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libflaim.a
