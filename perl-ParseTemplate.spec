%define upstream_name    ParseTemplate
%define upstream_version 3.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Processor for templates containing Perl expressions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Symbol)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'Parse::Template' class evaluates Perl expressions placed within a
text. This class can be used as a code generator, or a generator of
documents in various document formats (HTML, XML, RTF, etc.).

The principle of template-based text generation is simple. A template
consists of a text which includes expressions to be evaluated.
Interpretation of these expressions generates text fragments which are
substituted in place of the expressions. In the case of 'Parse::Template'
the expressions to be evaluated are Perl expressions placed within two
'%%'.

Evaluation takes place within an environment in which, for example, you can
place data structures which will serve to generate the parts to be
completed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


