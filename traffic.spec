Summary:	Traffic Analyzer
Summary(pl.UTF-8):   Analizator ruchu
Name:		traffic
Version:	0.1
%define		_rc	rc4
Release:	0.%{_rc}.1
License:	Free
Group:		Networking/Utilities
Source0:	http://darkzone.ma.cx/resources/unix/traffic/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	f8f1473639e24e8c9ff74eb457014b31
URL:		http://darkzone.ma.cx/resources/unix/traffic/
Patch0:		%{name}-ncurses.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Traffic Analyzer based on libpcap and ncurses.

%description -l pl.UTF-8
Analizator ruchu oparty na libpcap i ncurses.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install traffic $RPM_BUILD_ROOT%{_bindir}
install man/traffic.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog LICENSE README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
