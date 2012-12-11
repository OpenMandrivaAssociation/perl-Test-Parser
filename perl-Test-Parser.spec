%define module  Test-Parser

Name:		perl-%{module}
Version:	1.9
Release:	3
Summary:	Base class for parsing log files from test runs, and displays in an XML syntax 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(XML::Twig)

%description 
This module serves as a common base class for test log parsers. These tools are
intended to be able to parse output from a wide variety of tests - including
non-Perl tests.

The parsers also write the test data into the 'Test Result Publication
Interface' (TRPI) XML schema, developed by SpikeSource.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc ChangeLog INSTALL README
%{perl_vendorlib}/Test
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.9-2mdv2010.0
+ Revision: 430599
- rebuild

* Fri Jul 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdv2009.0
+ Revision: 233678
- update to new version 1.9

* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdv2008.1
+ Revision: 175989
- new version

* Wed Feb 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdv2008.1
+ Revision: 175718
- new version
  drop test patch (merged upstream)
  new patch for fixing object type

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-1mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2007.1
+ Revision: 143528
- fix build dependencies
- Imported perl-Test-Parser-1.5-1mdv2007.1 into SVN repository.

* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2007.1
- first mdv release

