#
# Conditional build:
%bcond_with	qt4	# use Qt 4 instead of Qt 5
%bcond_with	tests	# "make test" call (requires functional libusb, i.e. accessible USB subsystem)
#
Summary:	Qt based logic analyzer GUI for sigrok
Summary(pl.UTF-8):	Oparty na Qt graficzny interfejs analizatora logicznego dla szkieletu sigrok
Name:		pulseview
Version:	0.4.0
Release:	2
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	http://sigrok.org/download/source/pulseview/%{name}-%{version}.tar.gz
# Source0-md5:	122ded293913ec773cd34cb68b93e0f9
URL:		http://sigrok.org/wiki/PulseView
BuildRequires:	boost-devel >= 1.53
%{?with_tests:BuildRequires:	boost-test >= 1.53}
BuildRequires:	cmake >= 2.8.6
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libsigrok-c++-devel >= 0.5.0
BuildRequires:	libsigrok-devel >= 0.5.0
BuildRequires:	libsigrokdecode-devel >= 0.5.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtSvg-devel >= 4
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
%else
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Svg-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
Requires:	Qt5Gui-platform-xcb
%endif
Requires:	libsigrok >= 0.4.0
Requires:	libsigrok-c++-devel >= 0.4.0
Requires:	libsigrokdecode >= 0.5.0
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
	%{?with_tests:-DENABLE_TESTS=ON} \
	%{?with_qt4:-DFORCE_QT4=ON}

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/pulseview
%{_mandir}/man1/pulseview.1*
%{_desktopdir}/org.sigrok.PulseView.desktop
%{_iconsdir}/hicolor/*/apps/pulseview.png
%{_iconsdir}/hicolor/*/apps/pulseview.svg
%{_datadir}/metainfo/org.sigrok.PulseView.appdata.xml
