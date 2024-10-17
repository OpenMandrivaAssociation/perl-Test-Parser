%define module  Test-Parser
%define debug_package %{nil}

Name:		perl-%{module}
Version:	1.9
Release:	6
Summary:	Base class for parsing log files from test runs, and displays in an XML syntax 
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{module}
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
