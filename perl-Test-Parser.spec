%define module  Test-Parser
%define name    perl-%{module}
%define version 1.9
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Base class for parsing log files from test runs, and displays in an XML syntax 
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XML::Twig)
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
This module serves as a common base class for test log parsers. These tools are
intended to be able to parse output from a wide variety of tests - including
non-Perl tests.

The parsers also write the test data into the 'Test Result Publication
Interface' (TRPI) XML schema, developed by SpikeSource.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README
%{perl_vendorlib}/Test
%{_mandir}/*/*
%{_bindir}/*


