%define major 0

%define libname	%mklibname %{name} %{major}
%define libusbname %mklibname %{name}-libusb %{major}
%define devname	%mklibname -d %{name}

Name:           hidapi
Version:        0.14.0
Release:        2
Summary:        Simple library for communicating with USB and Bluetooth HID devices
License:        GPL-3.0 or BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/libusb/hidapi
Source:         https://github.com/libusb/hidapi/archive/%{name}-%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libudev)

%description
HIDAPI is a library which allows an application to interface with USB and Bluetooth HID-Class devices.
While it can be used to communicate with standard HID devices like keyboards, mice, and Joysticks. 
It is most useful when used with custom (Vendor-Defined) HID devices.

%package -n %{devname}
Summary:        Development libraries and header files for hidapi
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       %{libname} = %{EVRD}
Requires:       %{libusbname} = %{EVRD}
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(libusb-1.0)

Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the header files and libraries for building
programs using the hidapi library.

%package -n %{libname}
Summary:        Simple library for communicating with USB and Bluetooth HID devices
Group:          System/Libraries

%description -n %{libname}
HIDAPI is a library which allows an application to interface with USB and Bluetooth HID-Class devices.
While it can be used to communicate with standard HID devices like keyboards, mice, and Joysticks.
It is most useful when used with custom (Vendor-Defined) HID devices.

%package -n %{libusbname}
Summary:        Simple library for communicating with USB and Bluetooth HID devices
Group:          System/Libraries

%description -n %{libusbname}
HIDAPI is a library which allows an application to interface with USB and Bluetooth HID-Class devices.
While it can be used to communicate with standard HID devices like keyboards, mice, and Joysticks. 
It is most useful when used with custom (Vendor-Defined) HID devices.

%prep
%setup -qn %{name}-%{name}-%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files -n %{devname}
%defattr(-,root,root)
%doc README.md AUTHORS.txt HACKING.txt
%{_includedir}/hidapi
%{_libdir}/pkgconfig/*
%{_libdir}/libhidapi-*.so
%{_libdir}/cmake/hidapi/

%files -n %{libname}
%defattr(-,root,root)
%license LICENSE*
%{_libdir}/libhidapi-hidraw.so.%{major}*

%files -n %{libusbname}
%defattr(-,root,root)
%license LICENSE*
%{_libdir}/libhidapi-libusb.so.%{major}*
