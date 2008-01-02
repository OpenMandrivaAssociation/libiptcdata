%define major 0
%define libname %mklibname iptcdata %major

Name: libiptcdata
Summary: IPTC tag library
Version: 1.0.2
Release: %mkrel 1
License: LGPL
Group: System/Libraries
Source: http://prdownloads.sourceforge.net/libiptcdata/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python-devel
URL: http://sourceforge.net/projects/libiptcdata/

%description
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package utils
Summary: IPTC tag library
Group: System/Libraries

%description utils
libiptcdata is a library for parsing, editing, and saving IPTC data.


%package -n %libname
Summary: IPTC tag library
Group: System/Libraries

%description -n %libname
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package -n %libname-devel
Summary: The files needed for libiptcdata application development
Group: Development/C
Requires: %{libname} = %{version}
Provides: %name-devel = %version-%release

%description -n %libname-devel
This package contains the libraries and include files
that you can use to develop libiptcdata applications.

%package -n python-iptcdata
Summary: IPTC tag library
Group: Development/Python

%description -n python-iptcdata
python-iptcdata is a library for parsing, editing, and saving IPTC data.

%prep
%setup -q

%build
%configure2_5x --enable-python
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

rm -f %buildroot%py_platsitedir/*a

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files utils
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL TODO
%{_bindir}/*

%files -n %libname
%{_libdir}/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata
%{_datadir}/gtk-doc/html/libiptcdata

%files -n python-iptcdata
%defattr(-,root,root)
%py_platsitedir/iptcdata.*


