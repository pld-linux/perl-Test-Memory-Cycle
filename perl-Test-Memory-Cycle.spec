#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Memory-Cycle
Summary:	Test::Memory::Cycle - Check for memory leaks and circular memory references
Summary(pl.UTF-8):	Test::Memory::Cycle - kontrola wycieków pamięci i zapętlonych odniesień
Name:		perl-Test-Memory-Cycle
Version:	1.06
Release:	2
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Memory-Cycle-%{version}.tar.gz
# Source0-md5:	397e709ba33d3883b5fb2bc49e3a70b0
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
Requires:	perl-Devel-Cycle >= 1.07
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module checks for memory leaks and circular memory references.

%description -l pl.UTF-8
Ten moduł sprawdza występowanie wycieków pamięci i zapętlonych
odniesień.

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
%doc Changes README.md
%dir %{perl_vendorlib}/Test/Memory
%{perl_vendorlib}/Test/Memory/Cycle.pm
%{_mandir}/man3/Test::Memory::Cycle.3pm*
