# TODO
# - cflags & g++
Summary:	Embeddable cross-platform database engine
Summary(pl):	Osadzalny, wieloplatformowy silnik baz danych
Name:		libflaim
Version:	4.8.143
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://forgeftp.novell.com/flaim/flaim/downloads/source/%{name}-%{version}.tar.gz
# Source0-md5:	de23c05fe8ec5ded79ca01700058e5b8
URL:		http://forge.novell.com/modules/xfmod/project/?flaim
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLAIM is an embeddable cross-platform database engine that provides a
rich, powerful, easy-to-use feature set. It is the database engine
used by Novell eDirectory. It has proven to be highly scalable,
reliable, and robust. It is available on a wide variety of 32 bit and
64 bit platforms.

%description -l pl
FLAIM to osadzalny, wieloplatformowy silnik baz danych udostêpniaj±cy
bogaty, potê¿ny i ³atwy w u¿yciu zbiór mo¿liwo¶ci. Jest to silnik baz
danych u¿ywany przez Novell eDirectory. Sprawdzi³ siê jako wysoko
skalowalny, pewny i silny. Jest dostêpny na wiele platform 32- i
64-bitowych.

%package devel
Summary:	Header files for libflaim library
Summary(pl):	Pliki nag³ówkowe biblioteki libflaim
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libflaim library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki libflaim.

%package static
Summary:	Static libflaim library
Summary(pl):	Statyczna biblioteka libflaim
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libflaim library.

%description static -l pl
Statyczna biblioteka libflaim.

%prep
%setup -q

%build
%{__make} libs \
	OSTYPE=%{_os} \
	HOSTTYPE=%{_arch}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	OSTYPE=%{_os} \
	HOSTTYPE=%{_arch} \
	DESTDIR=$RPM_BUILD_ROOT

ln -s libflaim.so.1.2 $RPM_BUILD_ROOT%{_libdir}/libflaim.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING VERSION
%attr(755,root,root) %{_libdir}/libflaim.so.1.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflaim.so
%{_includedir}/flaim.h
%{_pkgconfigdir}/libflaim.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libflaim.a
