Summary:	Speech recognitnion engine
Summary(pl):	System rozpoznawania mowy
Name:		sphinx3
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
# Source0-md5:	e01ad40f6f41dfac852cd0a45a170d81
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-names.patch
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
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description devel -l pl
Pliki nag³ówkowe %{name}.

%package static
Summary:	Static sphinx3 libraries
Summary(pl):	Biblioteki statyczne sphinx3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of sphinx3 libraries.

%description static -l pl
Statyczne wersje bibliotek sphinx3.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS ChangeLog LICENSE NEWS README doc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
# no installable headers (yet?)
#%%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
