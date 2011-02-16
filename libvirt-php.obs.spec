%define		req_libvirt_version 0.6.2

%if 0%{?suse_version} || 0%{?sles_version} 
%define		php_confdir %{_sysconfdir}/php5/conf.d
%define		php_extdir 	%{_libdir}/php5/extensions
%else
%define		php_confdir %{_sysconfdir}/php.d 
%define		php_extdir  %{_libdir}/php/modules
%endif

Name:		libvirt-php
Version:	0.4
Release:	1%{?dist}%{?extra_release}
Summary:	PHP language binding for Libvirt

%if 0%{?suse_version} || 0%{?sles_version} 
Group:		Development/Libraries/PHP
%else
Group:		Development/Libraries
%endif
License:	PHP
URL:		http://libvirt.org/
Source0:	http://libvirt.org/sources/libvirt-php-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	php-devel
BuildRequires:	libvirt-devel >= %{req_libvirt_version}
BuildRequires:	libxml2-devel
%if 0%{?suse_version} || 0%{?sles_version} 
BuildRequires:	xhtml-dtd
%else
BuildRequires:	xhtml1-dtds
%endif
Requires:	libvirt >= %{req_libvirt_version}
%if 0%{?suse_version} || 0%{?sles_version} 
Requires:	php5
%else
Requires:	php
%endif

%description
PHP language bindings for Libvirt API. 
For more details see: http://phplibvirt.cybersales.cz/ http://www.libvirt.org/ http://www.php.net/

%package -n libvirt-php-doc
Summary:	Document of libvirt-php
Group:		Development/Libraries/PHP
Requires:	libvirt-php = %{version}

%description -n libvirt-php-doc
PHP language bindings for Libvirt API. 
For more details see: http://phplibvirt.cybersales.cz/ http://www.libvirt.org/ http://www.php.net/

This package contain the document for libvirt-php.

%prep
%setup -q -n libvirt-php-%{version}

%build
%configure
./configure --with-html-dir=%{_datadir}/doc --with-html-subdir=%{name}-%{version}/html
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{php_extdir}/libvirt-php.so
%config(noreplace) %{php_confdir}/libvirt-php.ini

%files -n libvirt-php-doc
%defattr(-,root,root,-)
%doc
%{_datadir}/doc/%{name}-%{version}/html

%changelog
