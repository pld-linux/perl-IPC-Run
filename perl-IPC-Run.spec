%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	Run
Summary:	IPC-Run perl module
Summary(pl):	Modu� perla IPC-Run
Name:		perl-IPC-Run
Version:	0.75
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	perl-IO-Tty
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(IO::Pty)'

%description
IPC::Run allows you run and interact with child processes using files, pipes,
and pseudo-ttys.  Both system()-style and scripted usages are supported and
may be mixed.  Likewise, functional and OO API styles are both supported and
may be mixed.

Various redirection operators reminiscent of those seen on common Unix and DOS
command lines are provided.

%description -l pl
IPC::Run pozwala na uruchamianie i interakcj� z procesami potomnymi przy
u�yciu plik�w, potok�w, i pseudo-tty. Obs�uguje zar�wno interfejs w stylu
system(), jak i skryptowy; mo�na tak�e je miesza�. Mo�na stosowa� API
obiektowy i/lub proceduralny.

Udost�pniane s� r�ne operatory przekierowania, podobne do spotykanych
w linii polece� popularnych Uniks�w i DOS-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/IPC/Run.pm
%dir %{perl_sitelib}/IPC/Run
%{perl_sitelib}/IPC/Run/*
%{_mandir}/man3/*
