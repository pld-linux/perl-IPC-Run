#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	IPC
%define		pnam	Run
Summary:	IPC::Run - system() and background procs w/ piping, redirs, ptys
Summary(pl.UTF-8):	IPC::Run - uruchamianie procesów z potokami, przekierowaniami i pseudoterminalami
Name:		perl-IPC-Run
Version:	20260402.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/IPC/TODDR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	456c16b50adc600507c14b3326b2fbec
URL:		https://metacpan.org/dist/IPC-Run
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-IO-Tty >= 1.25
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%description -l pl.UTF-8
IPC::Run pozwala na uruchamianie i interakcję z procesami potomnymi
przy użyciu plików, potoków, i pseudoterminali. Obsługuje zarówno
interfejs w stylu system(), jak i skryptowy; można także je mieszać.
Można stosować API obiektowe i/lub proceduralne.

Udostępniane są różne operatory przekierowania, podobne do spotykanych
w linii poleceń popularnych Uniksów i DOS-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog LICENSE
%{perl_vendorlib}/IPC/Run.pm
%dir %{perl_vendorlib}/IPC/Run
%{perl_vendorlib}/IPC/Run/*.pm
%{_mandir}/man3/IPC::Run*.3pm*
