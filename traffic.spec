Summary:	Traffic Analyzer
Summary(pl):	Analizator ruchu
Name:		traffic
Version:	0.1
Release:	1
License:	Free
Group:		Networking/Utilities
Source0:	http://darkzone.ma.cx/resources/unix/traffic/%{name}-current.tar.gz
# Source0-md5:	b427c393f2b0202d0188af07b4a1c02c
URL:		http://darkzone.ma.cx/resources/unix/traffic/
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-gcc33.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Traffic Analyzer based on libpcap and ncurses.

%description -l pl
Analizator ruchu oparty na libpcap i ncurses.

%prep
%setup -q -n %{name}-current
%patch0 -p1
%patch1 -p1

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
