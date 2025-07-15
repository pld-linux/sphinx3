Summary:	CMU Sphinx III - Speech recognitnion engine
Summary(pl.UTF-8):	CMU Sphinx III - System rozpoznawania mowy
Name:		sphinx3
Version:	0.8
Release:	1
License:	BSD-like
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.bz2
# Source0-md5:	e32bf4c507509b27482adf4cfc467e8f
Patch0:		%{name}-am.patch
Patch1:		%{name}-update.patch
Patch2:		%{name}-format.patch
Patch3:		%{name}-install.patch
Patch4:		%{name}-link.patch
URL:		https://cmusphinx.github.io/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sphinxbase-devel >= 0.8
Requires:	sphinxbase >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of Carnegie Mellon University's open source large vocabulary,
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx3-simple, and test it!

%description -l pl.UTF-8
System rozpoznawania ciągłej mowy, niezależny od mówiącego, z dużym
słownikiem, pochodzący z Carnegie Mellon University.

Podłącz mikrofon, uruchom sphinx3-simple i testuj!

%package devel
Summary:	CMU Sphinx III header files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek CMU Sphinx III
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sphinxbase-devel >= 0.8

%description devel
CMU Sphinx III header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek CMU Sphinx III.

%package static
Summary:	Static CMU Sphinx III libraries
Summary(pl.UTF-8):	Biblioteki statyczne CMU Sphinx III
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of CMU Sphinx III libraries.

%description static -l pl.UTF-8
Statyczne wersje bibliotek CMU Sphinx III.

%package doc
Summary:	Documentation for CMU Sphinx III
Summary(pl.UTF-8):	Dokumentacja pakietu CMU Sphinx III
Group:		Documentation

%description doc
Documentation for CMU Sphinx III.

%description doc -l pl.UTF-8
Dokumentacja pakietu CMU Sphinx III.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

find doc -name .svn | xargs %{__rm} -r

# subdirs install is broken
mkdir -p doc/.hidden
%{__mv} doc/{images,s3,s3-2_files} doc/.hidden

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libs3decoder.la

install -d $RPM_BUILD_ROOT%{_docdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/doc $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/doxygen.{cfg,main}
# remaining files, not handled properly by automake install
cp -pr doc/.hidden/{images,s3,s3-2_files} $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/{images/Makefile,s3-2_files/{Makefile,filelist.xml}}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sphinx3-simple
%attr(755,root,root) %{_bindir}/sphinx3_*
%attr(755,root,root) %{_libdir}/libs3decoder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libs3decoder.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libs3decoder.so
%{_includedir}/sphinx3
%{_pkgconfigdir}/sphinx3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libs3decoder.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}
