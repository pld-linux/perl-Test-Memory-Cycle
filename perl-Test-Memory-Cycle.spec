#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Memory-Cycle
Summary:	Test::Memory::Cycle - Check for memory leaks and circular memory references
Summary(pl.UTF-8):   Test::Memory::Cycle - kontrola wycieków pamięci i zapętlonych odniesień
Name:		perl-Test-Memory-Cycle
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PETDANCE/Test-Memory-Cycle-%{version}.tar.gz
# Source0-md5:	0c51e09f6bc23676ca0112b1a95e129d
URL:		http://search.cpan.org/dist/Test-Memory-Cycle/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Cycle >= 1.07
BuildRequires:	perl-PadWalker
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
BuildRequires:	perl-Test-Simple >= 0.62
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module checks for memory leaks and circular memory references.

%description -l pl.UTF-8
Ten moduł sprawdza występowanie wycieków pamięci i zapętlonych
odniesień.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

mv t/family-array.t{,fail}
mv t/family-scalar.t{,fail}
mv t/family-object.t{,fail}
mv t/family-hash.t{,fail}
mv t/cycle-exists.t{,fail}

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
%doc Changes README
%dir %{perl_vendorlib}/Test/Memory
%{perl_vendorlib}/Test/Memory/*.pm
%{_mandir}/man3/*
