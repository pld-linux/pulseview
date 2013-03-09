#
%bcond_without	tests
#
%define snap	a7553da
#
Summary:	Qt based logic analyzer GUI for sigrok
Name:		pulseview
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications/Graphics
# Source0:	http://sigrok.org/gitweb/?p=pulseview.git;a=snapshot;h=%{snap};sf=tgz;/%{name}-%{snap}.tar.gz
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	52527a78a1ee676546d63615bf1c1c8d
Patch0:		%{name}-build.patch
URL:		http://sigrok.org/wiki/PulseView
BuildRequires:	boost-devel
%{?with_tests:BuildRequires:	boost-test}
BuildRequires:	boost-thread
BuildRequires:	glib2-devel
BuildRequires:	libsigrok-devel >= 0.2.0
BuildRequires:	libsigrokdecode-devel >= 0.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt based logic analyzer GUI for sigrok.

%prep
%setup -q -n %{name}-%{snap}
%patch0 -p1

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
