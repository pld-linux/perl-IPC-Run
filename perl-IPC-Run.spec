#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test fails)
#
%define		pdir	IPC
%define		pnam	Run
Summary:	IPC::Run - system() and background procs w/ piping, redirs, ptys
Summary(pl.UTF-8):	IPC::Run - uruchamianie procesów z potokami, przekierowaniami i pseudoterminalami
Name:		perl-IPC-Run
Version:	0.90
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IPC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fda6bbd9d5e4e738a02230923a41125b
URL:		http://search.cpan.org/dist/IPC-Run/
BuildRequires:	perl-IO-Tty >= 1.08
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.47}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{perl_vendorlib}/IPC/Run.pm
%dir %{perl_vendorlib}/IPC/Run
%{perl_vendorlib}/IPC/Run/*.pm
%{_mandir}/man3/IPC::Run*.3pm*
