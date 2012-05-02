%define major 0
%define libname %mklibname iptcdata %major
%define develname %mklibname -d iptcdata

Name: libiptcdata
Summary: IPTC tag library
Version: 1.0.4
Release: %mkrel 4
License: LGPLv2+
Group: System/Libraries
Source: http://prdownloads.sourceforge.net/libiptcdata/%{name}-%{version}.tar.gz
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

%package i18n
Summary: Translations of the IPTC tag library
Group: System/Libraries

%description i18n
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package -n %libname
Summary: IPTC tag library
Group: System/Libraries
Requires: %name-i18n >= %version

%description -n %libname
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package -n %develname
Summary: The files needed for libiptcdata application development
Group: Development/C
Requires: %{libname} = %{version}
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d iptcdata 0

%description -n %develname
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
rm -rf %{buildroot}
%makeinstall
%find_lang %name
%find_lang iptc


rm -f %buildroot%py_platsitedir/*a

%clean
rm -rf %{buildroot}

%files utils -f iptc.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL TODO
%{_bindir}/*

%files i18n -f %name.lang


%files -n %libname
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata
%{_datadir}/gtk-doc/html/libiptcdata

%files -n python-iptcdata
%defattr(-,root,root)
%py_platsitedir/iptcdata.*


