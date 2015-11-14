#
# Conditional build:
%bcond_with	tests	# "make test" call (requires functional libusb, i.e. accessible USB subsystem)
#
Summary:	Qt based logic analyzer GUI for sigrok
Summary(pl.UTF-8):	Oparty na Qt graficzny interfejs analizatora logicznego dla szkieletu sigrok
Name:		pulseview
Version:	0.2.0
Release:	6
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	http://sigrok.org/download/source/pulseview/%{name}-%{version}.tar.gz
# Source0-md5:	fe5586212671226afafe9d8d80ed10c6
URL:		http://sigrok.org/wiki/PulseView
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	boost-devel >= 1.42
%{?with_tests:BuildRequires:	boost-test >= 1.42}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libsigrok-devel >= 0.3.0
BuildRequires:	libsigrokdecode-devel >= 0.3.0
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake >= 4
Requires:	libsigrok >= 0.3.0
Requires:	libsigrokdecode >= 0.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt based logic analyzer GUI for sigrok.

%description -l pl.UTF-8
Oparty na Qt graficzny interfejs analizatora logicznego dla szkieletu
sigrok.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DDISABLE_WERROR=ON \
	%{?with_tests:-DENABLE_TESTS=ON}

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -D contrib/pulseview.desktop $RPM_BUILD_ROOT%{_desktopdir}/pulseview.desktop
install -D icons/sigrok-logo-notext.png $RPM_BUILD_ROOT%{_pixmapsdir}/sigrok-logo-notext.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/pulseview
%{_mandir}/man1/pulseview.1*
%{_desktopdir}/pulseview.desktop
%{_pixmapsdir}/sigrok-logo-notext.png
