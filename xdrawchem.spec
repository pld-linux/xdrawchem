Summary:	XDrawChem - a chemical drawing program
Summary(pl):	XDrawChem - program do rysunk�w chemicznych
Name:		xdrawchem
Version:	1.9.2
Release:	1
License:	BSD-like
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/xdrawchem/%{name}-%{version}.tar.gz
# Source0-md5:	c0c230e3e2f87f0d7ac4c54b21a305ef
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-ac.patch
Patch1:		%{name}-qt_path.patch
Patch2:		%{name}-lib64.patch
URL:		http://xdrawchem.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openbabel-devel >= 1.100.2
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDrawChem is a program for drawing chemical structures and reactions.
It can also predict 13C NMR and IR spectra, calculate empirical
formulas, and estimate elemental analysis.

%description -l pl
XDrawChem jest programem do rysowania chemicznych struktur i reakcji.
Mo�e tak�e przewidzie� widma NMR (13C i 1H) oraz IR, oblicza� wzory 
empiryczne oraz sk�ad pierwiastkowy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if "%{_lib}" == "lib64"
%patch2 -p1
%endif

rm -rf autom4te.cache

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} automoc
%configure \
	--with-qtdir=%{_prefix}
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
