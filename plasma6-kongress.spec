%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		plasma6-kongress
Version:	24.08.0
Release:	%{?git:0.%{git}.}1
Summary:	Companion application for conference attendees
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kongress/-/archive/%{gitbranch}/kongress-%{gitbranchd}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kongress-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KOSMIndoorMap)

%description
Companion application for conference attendees

%prep
%autosetup -p1 -n kongress-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kongress --all-name

%files -f kongress.lang
%{_bindir}/kongress
%{_datadir}/applications/org.kde.kongress.desktop
%{_datadir}/metainfo/org.kde.kongress.appdata.xml
%{_bindir}/kongressac
%{_datadir}/dbus-1/services/org.kde.kongressac.service
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kongress.svg
%{_datadir}/knotifications6/kongressac.notifyrc
