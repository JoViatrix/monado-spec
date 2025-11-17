%global commit 9e61ac2
%global datetimever 2025111701239e61ac2

Name: monado
Version: 2025111701239e61ac2
Release: 1%{?dist}
Summary: Monado - XR Runtime (XRT)

License: bsl-1.0
URL: https://monado.freedesktop.org/
Source0: https://gitlab.freedesktop.org/monado/monado/-/archive/%{commit}/monado-%{commit}.tar.gz

BuildRequires: cmake >= 3.13
BuildRequires: gcc-c++
BuildRequires: python3 >= 3.6
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(eigen3)
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(openhmd) >= 0.3.0
BuildRequires: pkgconfig(opencv)
BuildRequires: pkgconfig(libuvc)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(realsense2)
BuildRequires: pkgconfig(libcjson)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libonnxruntime)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: glslc
BuildRequires: pkgconfig(glslang)
BuildRequires: hidapi-devel
BuildRequires: libv4l-devel
BuildRequires: libsurvive-devel
BuildRequires: pkgconfig(percetto)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(openvr)
BuildRequires: dbus-devel
BuildRequires: libbsd-devel

Requires: opencv-videoio >= 4.11.0
Requires: basalt-monado

Conflicts: monado-constellation


%description
Monado is an open source XR runtime delivering immersive experiences such as VR
and AR on on mobile, PC/desktop, and any other device
(because gosh darn people come up with a lot of weird hardware).
Monado aims to be a complete and conforming implementation of the OpenXR API made by Khronos.
The project currently is being developed for GNU/Linux and aims to support other operating
systems in the near future.
"Monado" has no specific meaning and is just a name.

%prep
%autosetup -n %{name}-%{commit}

%build
%cmake -DBUILD_DOC:BOOL=OFF
%cmake_build

%install
%cmake_install


%check


%files
%license
%doc

%dir %{_includedir}/monado
%dir %{_datadir}/openxr
%dir %{_datadir}/steamvr-monado

/usr/lib/systemd/user/monado.service
/usr/lib/systemd/user/monado.socket

%{_bindir}/monado-cli
%{_bindir}/monado-ctl
%{_bindir}/monado-service
%{_bindir}/monado-gui

%{_includedir}/monado/*

%{_libdir}/libmonado.so*
%{_libdir}/libopenxr_monado.so

%{_datadir}/openxr/*
%{_datadir}/steamvr-monado/*


%changelog
* Mon Nov 17 2025 GitHub Actions <actions@github.com> - 2025111701239e61ac2-1
- Auto-update to Monado commit 9e61ac2

* Sat Nov 15 2025 GitHub Actions <actions@github.com> - 2025111501207d5fa81-1
- Auto-update to Monado commit 7d5fa81

* Fri Nov 14 2025 GitHub Actions <actions@github.com> - 202511140123ac54132-1
- Auto-update to Monado commit ac54132

* Thu Nov 13 2025 GitHub Actions <actions@github.com> - 202511130123b8916b8-1
- Auto-update to Monado commit b8916b8

* Wed Nov 12 2025 GitHub Actions <actions@github.com> - 20251112012219335a8-1
- Auto-update to Monado commit 19335a8

* Tue Nov 11 2025 GitHub Actions <actions@github.com> - 202511110123719bcd4-1
- Auto-update to Monado commit 719bcd4

* Sat Nov 08 2025 GitHub Actions <actions@github.com> - 2025110801183704210-1
- Auto-update to Monado commit 3704210

* Fri Nov 07 2025 GitHub Actions <actions@github.com> - 2025110701227039af8-1
- Auto-update to Monado commit 7039af8

* Thu Nov 06 2025 GitHub Actions <actions@github.com> - 202511060122ddb446f-1
- Auto-update to Monado commit ddb446f

* Sat Nov 01 2025 GitHub Actions <actions@github.com> - 20251101012535348e6-1
- Auto-update to Monado commit 35348e6

* Thu Oct 30 2025 GitHub Actions <actions@github.com> - 202510300123e8eb2ed-1
- Auto-update to Monado commit e8eb2ed

* Wed Oct 29 2025 GitHub Actions <actions@github.com> - 20251029012471b786a-1
- Auto-update to Monado commit 71b786a

* Tue Oct 28 2025 GitHub Actions <actions@github.com> - 20251028011857a9631-1
- Auto-update to Monado commit 57a9631

* Fri Oct 24 2025 GitHub Actions <actions@github.com> - 20251024011644aecfc-1
- Auto-update to Monado commit 44aecfc

* Wed Oct 22 2025 GitHub Actions <actions@github.com> - 2025102201222f95723-1
- Auto-update to Monado commit 2f95723

* Sun Oct 19 2025 GitHub Actions <actions@github.com> - 2025101901274d64649-1
- Auto-update to Monado commit 4d64649

* Sat Oct 18 2025 GitHub Actions <actions@github.com> - 20251018011427d6760-1
- Auto-update to Monado commit 27d6760

* Thu Oct 09 2025 GitHub Actions <actions@github.com> - 202510090117bf6080c-1
- Auto-update to Monado commit bf6080c

* Tue Oct 07 2025 GitHub Actions <actions@github.com> - 20251007011606e62fc-1
- Auto-update to Monado commit 06e62fc

* Sat Oct 04 2025 GitHub Actions <actions@github.com> - 2025100401133c3587a-1
- Auto-update to Monado commit 3c3587a

* Fri Oct 03 2025 GitHub Actions <actions@github.com> - 202510030115a00c833-1
- Auto-update to Monado commit a00c833

* Thu Oct 02 2025 GitHub Actions <actions@github.com> - 20251002011568c3300-1
- Auto-update to Monado commit 68c3300

* Wed Oct 01 2025 GitHub Actions <actions@github.com> - 202510010125b129e4b-1
- Auto-update to Monado commit b129e4b

* Tue Sep 30 2025 GitHub Actions <actions@github.com> - 202509300118eaa3797-1
- Auto-update to Monado commit eaa3797

* Sun Sep 28 2025 GitHub Actions <actions@github.com> - 2025092801241cafc3a-1
- Auto-update to Monado commit 1cafc3a

* Sat Sep 27 2025 GitHub Actions <actions@github.com> - 2025092701147eb1ea9-1
- Auto-update to Monado commit 7eb1ea9

* Fri Sep 26 2025 GitHub Actions <actions@github.com> - 2025092601179952e77-1
- Auto-update to Monado commit 9952e77

* Thu Sep 25 2025 GitHub Actions <actions@github.com> - 20250925011710c5cdd-1
- Auto-update to Monado commit 10c5cdd

* Wed Sep 24 2025 GitHub Actions <actions@github.com> - 202509240116ba579e4-1
- Auto-update to Monado commit ba579e4

* Tue Sep 23 2025 GitHub Actions <actions@github.com> - 202509230116620f3c7-1
- Auto-update to Monado commit 620f3c7

* Tue Sep 16 2025 GitHub Actions <actions@github.com> - 2025091601158a31838-1
- Auto-update to Monado commit 8a31838

* Wed Sep 10 2025 GitHub Actions <actions@github.com> - 202509100115d575234-1
- Auto-update to Monado commit d575234

* Thu Sep 04 2025 GitHub Actions <actions@github.com> - 2025090401157905300-1
- Auto-update to Monado commit 7905300

* Sat Aug 30 2025 GitHub Actions <actions@github.com> - 20250830011452a2b84-1
- Auto-update to Monado commit 52a2b84

* Fri Aug 29 2025 GitHub Actions <actions@github.com> - 2025082901181244d50-1
- Auto-update to Monado commit 1244d50

* Thu Aug 28 2025 GitHub Actions <actions@github.com> - 202508280118e4931a4-1
- Auto-update to Monado commit e4931a4

* Wed Aug 27 2025 GitHub Actions <actions@github.com> - 2025082701182ed83e8-1
- Auto-update to Monado commit 2ed83e8

* Tue Aug 26 2025 GitHub Actions <actions@github.com> - 20250826012108ec900-1
- Auto-update to Monado commit 08ec900

* Thu Aug 21 2025 GitHub Actions <actions@github.com> - 20250821011976577fe-1
- Auto-update to Monado commit 76577fe

* Sat Aug 16 2025 GitHub Actions <actions@github.com> - 2025081601229abe461-1
- Auto-update to Monado commit 9abe461

* Fri Aug 15 2025 GitHub Actions <actions@github.com> - 2025081501268a823e8-1
- Auto-update to Monado commit 8a823e8

* Thu Aug 14 2025 GitHub Actions <actions@github.com> - 2025081401262bc8034-1
- Auto-update to Monado commit 2bc8034

* Sat Aug 09 2025 GitHub Actions <actions@github.com> - 2025080901256ba8ba8-1
- Auto-update to Monado commit 6ba8ba8

* Fri Aug 08 2025 GitHub Actions <actions@github.com> - 20250808014282706e4-1
- Auto-update to Monado commit 82706e4

* Thu Aug 07 2025 GitHub Actions <actions@github.com> - 2025080701425c137fe-1
- Auto-update to Monado commit 5c137fe

* Thu Jul 31 2025 GitHub Actions <actions@github.com> - 2025073101410d51322-1
- Auto-update to Monado commit 0d51322

* Tue Jul 29 2025 GitHub Actions <actions@github.com> - 202507290151c3717b0-1
- Auto-update to Monado commit c3717b0

* Thu Jul 24 2025 GitHub Actions <actions@github.com> - 20250724013971e3356-1
- Auto-update to Monado commit 71e3356

* Wed Jul 23 2025 GitHub Actions <actions@github.com> - 2025072301404f121e0-1
- Auto-update to Monado commit 4f121e0

* Tue Jul 22 2025 GitHub Actions <actions@github.com> - 202507220139c02a640-1
- Auto-update to Monado commit c02a640

* Fri Jul 18 2025 GitHub Actions <actions@github.com> - 202507181005723fa68-1
- Auto-update to Monado commit 723fa68

%autochangelog
