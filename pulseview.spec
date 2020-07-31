# TODO: ENABLE_FLOW (BR: gstreamermm-devel >= 1.8.0, libsigrokflow-devel >= 0.1.0)
#
# Conditional build:
%bcond_with	tests	# "make test" call (requires functional libusb, i.e. accessible USB subsystem)
#
Summary:	Qt based logic analyzer GUI for sigrok
Summary(pl.UTF-8):	Oparty na Qt graficzny interfejs analizatora logicznego dla szkieletu sigrok
Name:		pulseview
Version:	0.4.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://sigrok.org/download/source/pulseview/%{name}-%{version}.tar.gz
# Source0-md5:	108a5f095f06a9485d31a0349ea38243
URL:		https://sigrok.org/wiki/PulseView
BuildRequires:	Qt5Core-devel >= 5.3
BuildRequires:	Qt5Gui-devel >= 5.3
BuildRequires:	Qt5Svg-devel >= 5.3
BuildRequires:	Qt5Widgets-devel >= 5.3
BuildRequires:	boost-devel >= 1.55
%{?with_tests:BuildRequires:	boost-test >= 1.53}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	glibmm-devel >= 2.28.0
BuildRequires:	libsigrok-c++-devel >= 0.5.1
BuildRequires:	libsigrok-devel >= 0.5.1
BuildRequires:	libsigrokdecode-devel >= 0.5.2
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5.3
BuildRequires:	qt5-linguist >= 5.3
BuildRequires:	qt5-qmake >= 5.3
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	Qt5Gui-platform-xcb
Requires:	glib2 >= 1:2.28.0
Requires:	glibmm >= 2.28.0
Requires:	hicolor-icon-theme
Requires:	libsigrok >= 0.5.1
Requires:	libsigrok-c++-devel >= 0.5.1
Requires:	libsigrokdecode >= 0.5.2
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/pulseview
%{_mandir}/man1/pulseview.1*
%{_desktopdir}/org.sigrok.PulseView.desktop
%{_iconsdir}/hicolor/*x*/apps/pulseview.png
%{_iconsdir}/hicolor/scalable/apps/pulseview.svg
%{_datadir}/metainfo/org.sigrok.PulseView.appdata.xml
