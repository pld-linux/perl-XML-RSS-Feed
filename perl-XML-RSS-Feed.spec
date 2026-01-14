#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	RSS-Feed
Summary:	XML::RSS::Feed - module for RDF Site Summary (RSS) files managment
Summary(pl.UTF-8):	XML::RSS::Feed - moduł do zarządzania plikami RDF Site Summary (RSS)
Name:		perl-XML-RSS-Feed
Version:	2.32
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	50a070684776c05834b42e0e0c4e4668
URL:		http://search.cpan.org/dist/XML-RSS-Feed/
%if %{with tests}
BuildRequires:	perl-Clone
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-URI
BuildRequires:	perl-XML-RSS
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::RSS::Feed - module for RDF Site Summary (RSS) files managment.

%description -l pl.UTF-8
XML::RSS::Feed - moduł do zarządzania plikami RDF Site Summary (RSS).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/XML/RSS/*.pm
%dir %{perl_vendorlib}/XML/RSS/Headline
%{perl_vendorlib}/XML/RSS/Headline/*.pm
%{_mandir}/man3/*
