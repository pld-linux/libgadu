#
# Conditional build:
%bcond_without	pthread		# POSIX threads support
%bcond_with	openssl		# use OpenSSL instead of GnuTLS
#
Summary:	libgadu library
Summary(es.UTF-8):	Biblioteca libgadu
Summary(pl.UTF-8):	Biblioteka libgadu
Name:		libgadu
Version:	1.12.0
Release:	1
Epoch:		4
License:	LGPL v2.1
Group:		Libraries
Source0:	http://github.com/wojtekka/libgadu/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e4569a0ed26136c4634fa8c4013910e3
URL:		http://toxygen.net/libgadu/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{!?with_openssl:BuildRequires:	gnutls-devel >= 2.10.0}
BuildRequires:	libtool
%{?with_openssl:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	protobuf-c-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
%{!?with_openssl:Requires:	gnutls >= 2.10.0}
Obsoletes:	libgg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%description -l de.UTF-8
Mit libgadu ist es Ihnen möglich auf einfache Weise Gadu-Gadu
Kommunikations-Unterstützung in Ihre Software einzubinden.

%description -l es.UTF-8
libgadu está pensada para facilitar añadirle comunicación vía
Gadu-Gadu a su software.

%description -l pl.UTF-8
libgadu umożliwia łatwe dodanie do różnych aplikacji komunikacji
bazującej na protokole Gadu-Gadu.

%package devel
Summary:	libgadu development library
Summary(es.UTF-8):	Biblioteca de desarrollo de libgadu
Summary(pl.UTF-8):	Część biblioteki libgadu dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{!?with_openssl:Requires:	gnutls-devel >= 2.10.0}
%{?with_openssl:Requires:	openssl-devel}
Requires:	zlib-devel
Obsoletes:	libgg-devel

%description devel
The libgadu-devel package contains the header files and some
documentation needed to develop application with libgadu.

%description devel -l de.UTF-8
Das libgadu-devel Paket enthält Header-Files (Kopfzeilenordner) und
die Dokumentation die Sie benötigen um mit libgadu Anwendungen zu
entwickeln.

%description devel -l es.UTF-8
El paquete libgadu-devel contiene los ficheros de cabecera, juntos con
una documentación, necesarios para desarrollar aplicaciones que usar
libgadu.

%description devel -l pl.UTF-8
Pakiet libgadu-devel zawiera pliki nagłówkowe i dokumentację,
potrzebne do kompilowania aplikacji korzystających z libgadu.

%package static
Summary:	Static libgadu library
Summary(es.UTF-8):	Biblioteca libgadu estática
Summary(pl.UTF-8):	Statyczna biblioteka libgadu
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libgg-static

%description static
Static libgadu library.

%description static -l de.UTF-8
Statisches libgadu Archiv.

%description static -l es.UTF-8
Biblioteca libgadu estática.

%description static -l pl.UTF-8
Statyczna biblioteka libgadu.

%prep
%setup -q

# force rebuild
%{__rm} include/packets.pb-c.h

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--without-bind \
	%{?with_openssl:--without-gnutls} \
%if %{with pthread}
	--with-pthread \
%else
	--without-pthread \
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgadu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgadu.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgadu.so
%{_includedir}/libgadu.h
%{_pkgconfigdir}/libgadu.pc
%{_libdir}/libgadu.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libgadu.a
