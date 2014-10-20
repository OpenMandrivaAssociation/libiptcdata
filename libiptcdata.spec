%define _disable_ld_no_undefined 1

%define major	0
%define libname	%mklibname iptcdata %major
%define devname	%mklibname -d iptcdata

Summary:	IPTC tag library
Name:		libiptcdata
Version:	1.0.4
Release:	12
License:	LGPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/libiptcdata/
Source0:	http://prdownloads.sourceforge.net/libiptcdata/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)

%description
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package utils
Summary:	IPTC tag library
Group:		System/Libraries

%description utils
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package i18n
Summary:	Translations of the IPTC tag library
Group:		System/Libraries
BuildArch:	noarch

%description i18n
This package contains the translations for %{name}.

%package -n %{libname}
Summary:	IPTC tag library
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}

%description -n %{libname}
libiptcdata is a library for parsing, editing, and saving IPTC data.

%package -n %{devname}
Summary:	The files needed for libiptcdata application development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the libraries and include files
that you can use to develop libiptcdata applications.

%package -n python-iptcdata
Summary:	IPTC tag library
Group:		Development/Python

%description -n python-iptcdata
python-iptcdata is a library for parsing, editing, and saving IPTC data.

%prep
%setup -q

%build
export PYTHON=%__python2
%configure \
	--enable-python
%make

%install
%makeinstall
%find_lang %{name}
%find_lang iptc

%files utils -f iptc.lang
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL TODO
%{_bindir}/*

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libiptcdata.so.%{major}*

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libiptcdata
%{_datadir}/gtk-doc/html/libiptcdata

%files -n python-iptcdata
%py2_platsitedir/iptcdata.*

