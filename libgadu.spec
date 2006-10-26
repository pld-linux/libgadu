%bcond_without	pthread		# build with POSIX threads support

Summary:	libgadu library
Summary(es):	Biblioteca libgadu
Summary(pl):	Biblioteka libgadu
Name:		libgadu
Version:	1.7.0
Release:	1
Epoch:		4
License:	LGPL v2.1
Group:		Libraries
Source0:	http://toxygen.net/libgadu/files/%{name}-%{version}.tar.gz
# Source0-md5:	152180afbbad584017592a3021aac97a
URL:		http://toxygen.net/libgadu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7d
Obsoletes:	libgg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%description -l de
Mit libgadu ist es Ihnen möglich auf einfache Weise Gadu-Gadu
Kommunikations-Unterstützung in Ihre Software einzubinden.

%description -l es
libgadu está pensada para facilitar añadirle comunicación vía
Gadu-Gadu a su software.

%description -l pl
libgadu umo¿liwia ³atwe dodanie do ró¿nych aplikacji komunikacji
bazuj±cej na protokole Gadu-Gadu.

%package -n libgadu-devel
Summary:	libgadu development library
Summary(es):	Biblioteca de desarrollo de libgadu
Summary(pl):	Czê¶æ biblioteki libgadu dla programistów
License:	LGPL v2.1
Group:		Development/Libraries
Requires:	libgadu = %{epoch}:%{version}-%{release}
Requires:	openssl-devel
Obsoletes:	libgg-devel

%description -n libgadu-devel
The libgadu-devel package contains the header files and some
documentation needed to develop application with libgadu.

%description -n libgadu-devel -l de
Das libgadu-devel Paket enthält Header-Files (Kopfzeilenordner) und
die Dokumentation die Sie benötigen um mit libgadu Anwendungen zu
entwickeln.

%description -n libgadu-devel -l es
El paquete libgadu-devel contiene los ficheros de cabecera, juntos con
una documentación, necesarios para desarrollar aplicaciones que usar
libgadu.

%description -n libgadu-devel -l pl
Pakiet libgadu-devel zawiera pliki nag³ówkowe i dokumentacjê,
potrzebne do kompilowania aplikacji korzystaj±cych z libgadu.

%package -n libgadu-static
Summary:	Static libgadu library
Summary(es):	Biblioteca libgadu estática
Summary(pl):	Statyczna biblioteka libgadu
License:	LGPL v2.1
Group:		Development/Libraries
Requires:	libgadu-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libgg-static

%description -n libgadu-static
Static libgadu library.

%description -n libgadu-static -l de
Statisches libgadu Archiv.

%description -n libgadu-static -l es
Biblioteca libgadu estática.

%description -n libgadu-static -l pl
Statyczna biblioteka libgadu.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dynamic \
	--enable-shared \
	--enable-static \
%if %{with pthread}
	--with-pthread \
%else
	--without-pthread \
	--without-bind
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
%attr(755,root,root) %{_libdir}/libgadu.so.*.*

%files -n libgadu-devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgadu.so
%{_includedir}/libgadu.h
%{_pkgconfigdir}/libgadu.pc

%files -n libgadu-static
%defattr(644,root,root,755)
%{_libdir}/libgadu.a
