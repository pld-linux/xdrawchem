Summary:	XDrawChem - a chemical drawing program
Summary(pl.UTF-8):   XDrawChem - program do rysunków chemicznych
Name:		xdrawchem
Version:	1.9.9
Release:	1
License:	BSD-like
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/sourceforge/xdrawchem/%{name}-%{version}.tar.gz
# Source0-md5:	6343d031b3ea19a6606831c89b8006b2
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://xdrawchem.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openbabel-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDrawChem is a program for drawing chemical structures and reactions.
It can also predict 13C NMR and IR spectra, calculate empirical
formulas, and estimate elemental analysis.

%description -l pl.UTF-8
XDrawChem jest programem do rysowania chemicznych struktur i reakcji.
Może także przewidzieć widma NMR (13C i 1H) oraz IR, obliczać wzory
empiryczne oraz skład pierwiastkowy.

%prep
%setup -q

# don't try to use qt-st
sed -i -e 's/libqt\./nolibqt\./' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} automoc
%configure \
	--with-qtdir=%{_prefix} \
	--with-qtlibdir=%{_libdir}
%{__make}

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
%{_datadir}/xdrawchem/xdrawchem*.png
%lang(da) %{_datadir}/xdrawchem/xdrawchem_da.qm
%lang(de) %{_datadir}/xdrawchem/xdrawchem_de.qm
%lang(en) %{_datadir}/xdrawchem/xdrawchem_en.qm
%lang(es) %{_datadir}/xdrawchem/xdrawchem_es.qm
%lang(fr) %{_datadir}/xdrawchem/xdrawchem_fr.qm
%lang(it) %{_datadir}/xdrawchem/xdrawchem_it.qm
%lang(nl) %{_datadir}/xdrawchem/xdrawchem_nl.qm
%lang(pl) %{_datadir}/xdrawchem/xdrawchem_pl.qm
%lang(ru) %{_datadir}/xdrawchem/xdrawchem_ru.qm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
