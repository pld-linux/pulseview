#
%bcond_without	tests
#
Summary:	Qt based logic analyzer GUI for sigrok
Name:		pulseview
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.sigrok.org/download/source/pulseview/%{name}-%{version}.tar.gz
# Source0-md5:	0b462664854f4186c67ce1aae78b6d06
URL:		http://sigrok.org/wiki/PulseView
BuildRequires:	boost-devel
%{?with_tests:BuildRequires:	boost-test}
BuildRequires:	boost-thread
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	libsigrok-devel >= 0.2.0-1
BuildRequires:	libsigrokdecode-devel >= 0.1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt based logic analyzer GUI for sigrok.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DDISABLE_WERROR=ON \
	%{?with_tests:-DENABLE_TESTS=ON} \
	../

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/pulseview.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HACKING README
%attr(755,root,root) %{_bindir}/pulseview
%{_mandir}/man1/pulseview.1*
