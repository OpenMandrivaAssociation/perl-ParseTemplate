%define upstream_name    ParseTemplate
%define upstream_version 3.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Processor for templates containing Perl expressions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Symbol)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.70.0-2mdv2011.0
+ Revision: 656957
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.70.0-1mdv2011.0
+ Revision: 596638
- update to 3.07

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 3.50.0-1mdv2011.0
+ Revision: 569951
- update to 3.05

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 3.30.0-1mdv2011.0
+ Revision: 532157
- update to 3.03

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 3.20.0-2mdv2010.1
+ Revision: 528117
- rebuild
- import perl-ParseTemplate


* Sat Mar 27 2010 cpan2dist 3.02-1mdv
- initial mdv release, generated with cpan2dist
