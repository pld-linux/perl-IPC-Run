#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test fails)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Run
Summary:	IPC::Run - system() and background procs w/ piping, redirs, ptys
Summary(pl):	IPC::Run - uruchamianie procesów z potokami, przekierowaniami i pseudoterminalami
Name:		perl-IPC-Run
Version:	0.80
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a867e694862afd4a3c429124618fc15e
BuildRequires:	perl-IO-Tty >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(IO::Pty)'

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%description -l pl
IPC::Run pozwala na uruchamianie i interakcjê z procesami potomnymi
przy u¿yciu plików, potoków, i pseudoterminali. Obs³uguje zarówno
interfejs w stylu system(), jak i skryptowy; mo¿na tak¿e je mieszaæ.
Mo¿na stosowaæ API obiektowe i/lub proceduralne.

Udostêpniane s± ró¿ne operatory przekierowania, podobne do spotykanych
w linii poleceñ popularnych Uniksów i DOS-a.

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
%{perl_vendorlib}/IPC/Run/*
%{_mandir}/man3/*
