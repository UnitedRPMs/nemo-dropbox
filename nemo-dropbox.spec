Summary:    Dropbox extension for nemo
Name:       nemo-dropbox
Version:    3.4.0
Release:    2%{?dist}
License:    GPLv2+ and LGPLv2+ and MIT
URL:        https://github.com/linuxmint/nemo-extensions
Source0:    %url/archive/%{version}.tar.gz#/nemo-extensions-%{version}.tar.gz

ExclusiveArch:  i686 x86_64

BuildRequires:  nemo-devel
BuildRequires:  python2-docutils
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pygobject2-devel
BuildRequires:  pygtk2-devel

Requires:       dropbox 

%description
Dropbox extension for nemo file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%setup -q -n nemo-extensions-%{version}

%build
pushd nemo-dropbox
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build V=1
popd

%install
pushd nemo-dropbox
%make_install
popd

#Remove libtool archives.
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

rm -rf ${RPM_BUILD_ROOT}%{_bindir}
rm -rf ${RPM_BUILD_ROOT}%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc nemo-dropbox/{AUTHORS,ChangeLog,NEWS,README}
%license nemo-dropbox/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-dropbox.so


%changelog

* Mon Jul 03 2016 David Va <davidva AT tutanota DOT com> - 3.4.0-2
- Upstream
- Changed Requires of dropbox, UnitedRPMs does not provides a fool epoch tag of dropbox

* Sun Jul 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0

* Sun Aug 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-2
- rebuilt

* Fri Jun 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0

* Sun Jul 05 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0

* Wed Jan 07 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- use internal version
- add ExclusiveArch

* Tue Dec 16 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-2
- add requires dropbox

* Tue Dec 09 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-1
- First build

