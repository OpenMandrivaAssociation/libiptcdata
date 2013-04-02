%define major 0
%define libname %mklibname iptcdata %major
%define develname %mklibname -d iptcdata
%define _disable_ld_no_undefined 1

Name: libiptcdata
Summary: IPTC tag library
Version: 1.0.4
Release: 6
License: LGPLv2+
Group: System/Libraries
Source: http://prdownloads.sourceforge.net/libiptcdata/%{name}-%{version}.tar.gz
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
%makeinstall
%find_lang %name
%find_lang iptc

rm -f %buildroot%py_platsitedir/*a

%files utils -f iptc.lang
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL TODO
%{_bindir}/*

%files i18n -f %name.lang


%files -n %libname
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata
%{_datadir}/gtk-doc/html/libiptcdata

%files -n python-iptcdata
%py_platsitedir/iptcdata.*




%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdv2011.0
+ Revision: 660264
- mass rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 520872
- rebuilt for 2010.1

* Mon Jul 06 2009 Götz Waschk <waschk@mandriva.org> 1.0.4-1mdv2010.0
+ Revision: 392693
- update to new version 1.0.4

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 1.0.3-2mdv2010.0
+ Revision: 371556
- fix obsoletes

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 368978
- new version
- add -i18n package
- rename devel package

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 222889
- rebuild
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 15 2007 Götz Waschk <waschk@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 26953
- new version


* Wed Mar 21 2007 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdv2007.1
+ Revision: 147184
- new version
- add python bindings

* Sat Oct 14 2006 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2006.0
+ Revision: 64591
- Import libiptcdata

* Sat Oct 14 2006 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2007.1
- initial mdv package

* Mon Feb 28 2005 David Moore <dcm@acm.org>
- Initial version

