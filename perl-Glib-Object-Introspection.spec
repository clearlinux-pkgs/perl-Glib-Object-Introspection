#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Glib-Object-Introspection
Version  : 0.050
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-Object-Introspection-0.050.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-Object-Introspection-0.050.tar.gz
Summary  : 'Dynamically create Perl language bindings'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Glib-Object-Introspection-bin = %{version}-%{release}
Requires: perl-Glib-Object-Introspection-license = %{version}-%{release}
Requires: perl-Glib-Object-Introspection-man = %{version}-%{release}
Requires: perl-Glib-Object-Introspection-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Depends)
BuildRequires : perl(ExtUtils::PkgConfig)
BuildRequires : perl(Glib)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gobject-introspection-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Glib::Object::Introspection
===========================
Glib::Object::Introspection uses the gobject-introspection and libffi projects
to dynamically create Perl bindings for a wide variety of libraries.  Examples
include GTK, WebKitGTK, libsoup and many more.

%package bin
Summary: bin components for the perl-Glib-Object-Introspection package.
Group: Binaries
Requires: perl-Glib-Object-Introspection-license = %{version}-%{release}

%description bin
bin components for the perl-Glib-Object-Introspection package.


%package dev
Summary: dev components for the perl-Glib-Object-Introspection package.
Group: Development
Requires: perl-Glib-Object-Introspection-bin = %{version}-%{release}
Provides: perl-Glib-Object-Introspection-devel = %{version}-%{release}
Requires: perl-Glib-Object-Introspection = %{version}-%{release}

%description dev
dev components for the perl-Glib-Object-Introspection package.


%package license
Summary: license components for the perl-Glib-Object-Introspection package.
Group: Default

%description license
license components for the perl-Glib-Object-Introspection package.


%package man
Summary: man components for the perl-Glib-Object-Introspection package.
Group: Default

%description man
man components for the perl-Glib-Object-Introspection package.


%package perl
Summary: perl components for the perl-Glib-Object-Introspection package.
Group: Default
Requires: perl-Glib-Object-Introspection = %{version}-%{release}

%description perl
perl components for the perl-Glib-Object-Introspection package.


%prep
%setup -q -n Glib-Object-Introspection-0.050
cd %{_builddir}/Glib-Object-Introspection-0.050

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Glib-Object-Introspection
cp %{_builddir}/Glib-Object-Introspection-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Glib-Object-Introspection/2139c48f66d66c6d30450a31dcfceb8cb38c7ff6 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/perli11ndoc

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Glib::Object::Introspection.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Glib-Object-Introspection/2139c48f66d66c6d30450a31dcfceb8cb38c7ff6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/perli11ndoc.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
