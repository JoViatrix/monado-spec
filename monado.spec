%global commit a357444
%global datetimever 202602260156a357444

Name: monado
Version: 202602260156a357444
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
* Thu Feb 26 2026 GitHub Actions <actions@github.com> - 202602260156a357444-1
- Auto-update to Monado commit a357444

* Wed Feb 25 2026 GitHub Actions <actions@github.com> - 20260225020144c36d8-1
- Auto-update to Monado commit 44c36d8

* Tue Feb 24 2026 GitHub Actions <actions@github.com> - 2026022401583c18853-1
- Auto-update to Monado commit 3c18853

* Fri Feb 20 2026 GitHub Actions <actions@github.com> - 202602200157c2ddab5-1
- Auto-update to Monado commit c2ddab5

* Thu Feb 19 2026 GitHub Actions <actions@github.com> - 202602190201ee655a9-1
- Auto-update to Monado commit ee655a9

* Wed Feb 18 2026 GitHub Actions <actions@github.com> - 202602180203c775ddd-1
- Auto-update to Monado commit c775ddd

* Tue Feb 17 2026 GitHub Actions <actions@github.com> - 202602170159c11afa5-1
- Auto-update to Monado commit c11afa5

* Sun Feb 15 2026 GitHub Actions <actions@github.com> - 202602150205bfdfdb7-1
- Auto-update to Monado commit bfdfdb7

* Sat Feb 14 2026 GitHub Actions <actions@github.com> - 20260214015509aa619-1
- Auto-update to Monado commit 09aa619

* Fri Feb 13 2026 GitHub Actions <actions@github.com> - 2026021302066b0e2ce-1
- Auto-update to Monado commit 6b0e2ce

* Tue Feb 10 2026 GitHub Actions <actions@github.com> - 2026021002137aa33fc-1
- Auto-update to Monado commit 7aa33fc

* Sun Feb 08 2026 GitHub Actions <actions@github.com> - 2026020802268b46a39-1
- Auto-update to Monado commit 8b46a39

* Sat Feb 07 2026 GitHub Actions <actions@github.com> - 20260207015381b7247-1
- Auto-update to Monado commit 81b7247

* Fri Feb 06 2026 GitHub Actions <actions@github.com> - 202602060156756e5fd-1
- Auto-update to Monado commit 756e5fd

* Thu Feb 05 2026 GitHub Actions <actions@github.com> - 2026020501570877fc2-1
- Auto-update to Monado commit 0877fc2

* Wed Feb 04 2026 GitHub Actions <actions@github.com> - 202602040155457302b-1
- Auto-update to Monado commit 457302b

* Tue Feb 03 2026 GitHub Actions <actions@github.com> - 202602030200cc967a2-1
- Auto-update to Monado commit cc967a2

* Sun Feb 01 2026 GitHub Actions <actions@github.com> - 202602010210c399c3a-1
- Auto-update to Monado commit c399c3a

* Sat Jan 31 2026 GitHub Actions <actions@github.com> - 2026013101500ff2924-1
- Auto-update to Monado commit 0ff2924

* Fri Jan 30 2026 GitHub Actions <actions@github.com> - 20260130015416f43e9-1
- Auto-update to Monado commit 16f43e9

* Thu Jan 29 2026 GitHub Actions <actions@github.com> - 20260129015404adeee-1
- Auto-update to Monado commit 04adeee

* Wed Jan 28 2026 GitHub Actions <actions@github.com> - 2026012801420b5795b-1
- Auto-update to Monado commit 0b5795b

* Tue Jan 27 2026 GitHub Actions <actions@github.com> - 20260127014550d59a5-1
- Auto-update to Monado commit 50d59a5

* Sat Jan 24 2026 GitHub Actions <actions@github.com> - 2026012401286d58eab-1
- Auto-update to Monado commit 6d58eab

* Fri Jan 23 2026 GitHub Actions <actions@github.com> - 202601230139793ae04-1
- Auto-update to Monado commit 793ae04

* Thu Jan 22 2026 GitHub Actions <actions@github.com> - 20260122014249e069a-1
- Auto-update to Monado commit 49e069a

* Wed Jan 21 2026 GitHub Actions <actions@github.com> - 2026012101425b97d91-1
- Auto-update to Monado commit 5b97d91

* Sun Jan 18 2026 GitHub Actions <actions@github.com> - 202601180146fa2f9f5-1
- Auto-update to Monado commit fa2f9f5

* Sat Jan 17 2026 GitHub Actions <actions@github.com> - 202601170126be0b641-1
- Auto-update to Monado commit be0b641

* Fri Jan 16 2026 GitHub Actions <actions@github.com> - 202601160140edecfb2-1
- Auto-update to Monado commit edecfb2

* Wed Jan 14 2026 GitHub Actions <actions@github.com> - 2026011401425029446-1
- Auto-update to Monado commit 5029446

* Tue Jan 13 2026 GitHub Actions <actions@github.com> - 20260113012693d5848-1
- Auto-update to Monado commit 93d5848

* Fri Jan 09 2026 GitHub Actions <actions@github.com> - 202601090139a40b4d2-1
- Auto-update to Monado commit a40b4d2

* Sat Jan 03 2026 GitHub Actions <actions@github.com> - 202601030124b58d31a-1
- Auto-update to Monado commit b58d31a

* Fri Jan 02 2026 GitHub Actions <actions@github.com> - 2026010201391b0d1b1-1
- Auto-update to Monado commit 1b0d1b1

* Wed Dec 31 2025 GitHub Actions <actions@github.com> - 202512310128072cdeb-1
- Auto-update to Monado commit 072cdeb

* Tue Dec 30 2025 GitHub Actions <actions@github.com> - 2025123001270a61582-1
- Auto-update to Monado commit 0a61582

* Mon Dec 29 2025 GitHub Actions <actions@github.com> - 202512290144852aaa7-1
- Auto-update to Monado commit 852aaa7

* Sat Dec 27 2025 GitHub Actions <actions@github.com> - 202512270125e43dc19-1
- Auto-update to Monado commit e43dc19

* Sun Dec 21 2025 GitHub Actions <actions@github.com> - 2025122101410d39a0c-1
- Auto-update to Monado commit 0d39a0c

* Fri Dec 12 2025 GitHub Actions <actions@github.com> - 2025121201274e5de8d-1
- Auto-update to Monado commit 4e5de8d

* Thu Dec 11 2025 GitHub Actions <actions@github.com> - 202512110127651a749-1
- Auto-update to Monado commit 651a749

* Wed Dec 10 2025 GitHub Actions <actions@github.com> - 202512100126bbe8c07-1
- Auto-update to Monado commit bbe8c07

* Tue Dec 09 2025 GitHub Actions <actions@github.com> - 202512090125908ed93-1
- Auto-update to Monado commit 908ed93

* Mon Dec 08 2025 GitHub Actions <actions@github.com> - 202512080125bd150b7-1
- Auto-update to Monado commit bd150b7

* Sat Dec 06 2025 GitHub Actions <actions@github.com> - 2025120601210660170-1
- Auto-update to Monado commit 0660170

* Fri Dec 05 2025 GitHub Actions <actions@github.com> - 202512050125f24ee92-1
- Auto-update to Monado commit f24ee92

* Thu Dec 04 2025 GitHub Actions <actions@github.com> - 2025120401249cff76f-1
- Auto-update to Monado commit 9cff76f

* Wed Dec 03 2025 GitHub Actions <actions@github.com> - 2025120301243180b3c-1
- Auto-update to Monado commit 3180b3c

* Tue Dec 02 2025 GitHub Actions <actions@github.com> - 202512020124c62c727-1
- Auto-update to Monado commit c62c727

* Mon Dec 01 2025 GitHub Actions <actions@github.com> - 2025120101472ebbca8-1
- Auto-update to Monado commit 2ebbca8

* Sun Nov 30 2025 GitHub Actions <actions@github.com> - 202511300140c597b20-1
- Auto-update to Monado commit c597b20

* Sat Nov 29 2025 GitHub Actions <actions@github.com> - 20251129012149fb440-1
- Auto-update to Monado commit 49fb440

* Fri Nov 28 2025 GitHub Actions <actions@github.com> - 20251128012135ed3c9-1
- Auto-update to Monado commit 35ed3c9

* Thu Nov 27 2025 GitHub Actions <actions@github.com> - 202511270121962a286-1
- Auto-update to Monado commit 962a286

* Wed Nov 26 2025 GitHub Actions <actions@github.com> - 20251126012300e8419-1
- Auto-update to Monado commit 00e8419

* Mon Nov 24 2025 GitHub Actions <actions@github.com> - 2025112401278fbc390-1
- Auto-update to Monado commit 8fbc390

* Sat Nov 22 2025 GitHub Actions <actions@github.com> - 202511220119a5d8548-1
- Auto-update to Monado commit a5d8548

* Fri Nov 21 2025 GitHub Actions <actions@github.com> - 2025112101212f0d747-1
- Auto-update to Monado commit 2f0d747

* Thu Nov 20 2025 GitHub Actions <actions@github.com> - 202511200121822e93d-1
- Auto-update to Monado commit 822e93d

* Wed Nov 19 2025 GitHub Actions <actions@github.com> - 20251119012361d59ca-1
- Auto-update to Monado commit 61d59ca

* Tue Nov 18 2025 GitHub Actions <actions@github.com> - 2025111801226ddfc57-1
- Auto-update to Monado commit 6ddfc57

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
