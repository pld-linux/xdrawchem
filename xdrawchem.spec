Summary:	XDrawChem - a chemical drawing program
Summary(pl):	XDrawChem - program do rysunków chemicznych
Name:		xdrawchem
Version:	1.5.2
Release:	3
License:	BSD-like
Group:		X11/Applications/Science
Source0:	http://www.prism.gatech.edu/~gte067k/xdrawchem/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-no_inclueded_openbabel.patch
URL:		http://www.prism.gatech.edu/~gte067k/xdrawchem/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openbabel-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XDrawChem is a program for drawing chemical structures and reactions.
It can also predict 13C NMR and IR spectra, calculate empirical
formulas, and estimate elemental analysis.

%description -l pl
XDrawChem jest programem do rysowania chemicznych struktur i reakcji.
Mo¿e tak¿e przewidzieæ 13C NMR oraz IR spectra, przeliczaæ empiryczne
formu³y, a tak¿e robiæ przybli¿on± analizê pierwiastków.

%prep
%setup -q
%patch0 -p1

%build
QTDIR=%{_prefix} ; export QTDIR
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific/Chemistry,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Chemistry
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.txt HISTORY.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/xdrawchem
%dir %{_datadir}/xdrawchem
%{_datadir}/xdrawchem/*
%{_applnkdir}/Scientific/Chemistry/*.desktop
%{_pixmapsdir}/*
