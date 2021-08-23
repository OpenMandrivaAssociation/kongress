#define snapshot 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		kongress
Version:	21.07
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Companion application for conference attendees
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/kongress/-/archive/v%{version}/kongress-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)

%description
Companion application for conference attendees

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

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
%{_datadir}/knotifications5/kongressac.notifyrc
