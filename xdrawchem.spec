Summary:	XDrawChem - a chemical drawing program
Summary(pl):	XDrawChem - program do rysunków chemicznych
Name:		xdrawchem
Version:	1.8
Release:	2
License:	BSD-like
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/xdrawchem/%{name}-%{version}.tgz
# Source0-md5:	03b43d3c6fc403b4463658ab1bfdccf9
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac.patch
URL:		http://xdrawchem.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openbabel-devel >= 1.100.2
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDrawChem is a program for drawing chemical structures and reactions.
It can also predict 13C NMR and IR spectra, calculate empirical
formulas, and estimate elemental analysis.

%description -l pl
XDrawChem jest programem do rysowania chemicznych struktur i reakcji.
Mo¿e tak¿e przewidzieæ widma 13C NMR oraz IR, przeliczaæ empiryczne
formu³y, a tak¿e robiæ przybli¿on± analizê sk³adu pierwiastkowego.

%prep
%setup -q
%patch0 -p1

rm -rf autom4te.cache

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} automoc
%configure
%{__make} \
	AM_CXXFLAGS=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.txt HISTORY.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/xdrawchem
%dir %{_datadir}/xdrawchem
%{_datadir}/xdrawchem/[!x]*
%{_datadir}/xdrawchem/xdrawchemrc
%lang(da) %{_datadir}/xdrawchem/xdrawchem_da.qm
%lang(de) %{_datadir}/xdrawchem/xdrawchem_de.qm
%lang(en) %{_datadir}/xdrawchem/xdrawchem_en.qm
%lang(es) %{_datadir}/xdrawchem/xdrawchem_es.qm
%lang(fr) %{_datadir}/xdrawchem/xdrawchem_fr.qm
%lang(it) %{_datadir}/xdrawchem/xdrawchem_it.qm
%lang(nl) %{_datadir}/xdrawchem/xdrawchem_nl.qm
%lang(pl) %{_datadir}/xdrawchem/xdrawchem_pl.qm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
