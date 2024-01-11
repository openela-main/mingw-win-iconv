%?mingw_package_header

Name:          mingw-win-iconv
Version:       0.0.6
Release:       9%{?dist}
Summary:       Iconv implementation using Win32 API

License:       Public Domain
Group:         Development/Libraries
URL:           http://code.google.com/p/win-iconv
Source0:       http://win-iconv.googlecode.com/files/win-iconv-%{version}.tar.bz2
BuildArch:     noarch
ExclusiveArch: %{ix86} x86_64

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils

BuildRequires: cmake >= 2.8.0
BuildRequires: dos2unix


%description
MinGW Windows Iconv library


%?mingw_debug_package


# Win32
%package -n mingw32-win-iconv
Summary:       MinGW Windows Iconv library
Obsoletes:     mingw32-iconv < 1.12-14
Provides:      mingw32-iconv = 1.12-14

%description -n mingw32-win-iconv
MinGW Windows cross compiled Iconv library.

%package -n mingw32-win-iconv-static
Summary:       Static version of the MinGW Windows Iconv library
Requires:      mingw32-win-iconv = %{version}-%{release}
Obsoletes:     mingw32-iconv-static < 1.12-14
Provides:      mingw32-iconv-static = 1.12-14

%description -n mingw32-win-iconv-static
Static version of the MinGW Windows Iconv library.

# Win64
%package -n mingw64-win-iconv
Summary:       MinGW Windows Iconv library
Obsoletes:     mingw64-iconv < 1.13.1-2%{?dist}
Provides:      mingw64-iconv = 1.13.1-2%{?dist}

%description -n mingw64-win-iconv
MinGW Windows Iconv library

%package -n mingw64-win-iconv-static
Summary:       Static version of the MinGW Windows Iconv library
Requires:      mingw64-win-iconv = %{version}-%{release}
Obsoletes:     mingw64-iconv-static < 1.13.1-2%{?dist}
Provides:      mingw64-iconv-static = 1.13.1-2%{?dist}

%description -n mingw64-win-iconv-static
Static version of the MinGW Windows Iconv library.


%prep
%setup -q -n win-iconv-%{version}

dos2unix readme.txt
dos2unix ChangeLog
chmod -x readme.txt
chmod -x ChangeLog


%build
%mingw_cmake -DBUILD_STATIC=1


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{mingw32_bindir}/*.exe
rm -rf $RPM_BUILD_ROOT%{mingw64_bindir}/*.exe


%files -n mingw32-win-iconv
%doc ChangeLog readme.txt
%{mingw32_bindir}/iconv.dll
%{mingw32_includedir}/iconv.h
%{mingw32_libdir}/libiconv.dll.a

%files -n mingw32-win-iconv-static
%{mingw32_libdir}/libiconv.a

%files -n mingw64-win-iconv
%doc ChangeLog readme.txt
%{mingw64_bindir}/iconv.dll
%{mingw64_includedir}/iconv.h
%{mingw64_libdir}/libiconv.dll.a

%files -n mingw64-win-iconv-static
%{mingw64_libdir}/libiconv.a


%changelog
* Tue Aug 14 2018 Victor Toso <victortoso@redhat.com> - 0.0.6-9
- ExclusiveArch: i686, x86_64
- Related: rhbz#1615874

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.6-3
- Stop using deprecated MinGW packaging macros

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.6-1
- Update to 0.0.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.0.4-1
- Update to 0.0.4
- Drop upstreamed dllname patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0-3-7
- Added win64 support

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.3-6
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 0.0.3-4
- Rename the shared library to iconv.dll instead of hacking up the
  import library

* Wed Jul  6 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.3-3
- Make sure that the .dll.a import library refers to libiconv.dll
  instead of iconv.dll

* Sun Jul  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.3-2
- Add versioned BR for cmake >= 2.8.0

* Fri Jun  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.3-1
- Update to 0.0.3

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.2-3
- Moved the obsoletes/provides to the proper location
- Bumped the requirement for mingw32-filesystem to >= 68 because of RPM 4.9 support
- Dropped the %%defattr tags
- Dropped the %%{?dist} tag from the obsoletes/provides

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.2-2
- Use the name mingw-win-iconv for the srpm to ease the transition to
  the mingw-w64 based toolchain
- Use the RPM 4.9 dependency generator
- Dropped unnecessary tags

* Thu Feb 17 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.2-1
- Update to version 0.0.2
- Dropped upstreamed patch
- Dropped the win_iconv.exe binary
- Bumped the mingw32-iconv obsoletes

* Thu Sep 30 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.0.1-1
- Initial release
- Obsoletes/provides mingw32-iconv and mingw32-iconv-static

