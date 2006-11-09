Summary:	Speech recognitnion engine
Summary(pl):	System rozpoznawania mowy
Name:		sphinx3
Version:	0.5
Release:	1
License:	BSD-like
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
# Source0-md5:	71a98518b740f2e80aec86c58148d8c0
Patch0:		%{name}-names.patch
URL:		http://www.speech.cs.cmu.edu/sphinx/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of Carnegie Mellon University's open source large vocabulary,
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx3-simple, and test it!

%description -l pl
System rozpoznawania ci±g³ej mowy, niezale¿ny od mówi±cego, z du¿ym
s³ownikiem, pochodz±cy z Carnegie Mellon University.

Pod³±cz mikrofon, uruchom sphinx3-simple i testuj!

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
%{name} header files.

%description devel -l pl
Pliki nag³ówkowe %{name}.

%package static
Summary:	Static sphinx3 libraries
Summary(pl):	Biblioteki statyczne sphinx3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of sphinx3 libraries.

%description static -l pl
Statyczne wersje bibliotek sphinx3.

%prep
%setup -q
%patch0 -p1

find doc -name CVS | xargs rm -rf

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

# hmm, name may conflict
rm -f $RPM_BUILD_ROOT%{_bindir}/batch.csh

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
rm -f doc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
# no installable headers (yet?)
#%%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
