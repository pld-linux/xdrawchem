Summary:	XDrawChem - A chemical drawing program
Summary(pl):	XDrawChem - Program do rysunków chemicznych
Name:		xdrawchem
Version:	1.5
Release:	1
License:	BSD-like
Group:		X11/Applications/Science
Source0:	http://www.prism.gatech.edu/~gte067k/xdrawchem/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-qmake.patch
URL:		http://www.prism.gatech.edu/~gte067k/xdrawchem/
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
%{__make} \
	QMAKECONF="%{_datadir}/qt/mkspecs/linux-g++/qmake.conf" \
	MOC="moc" \
	INCPATH="-I/usr/X11R6/include/qt" \
	RINGDIR="%{_datadir}/xdrawchem" all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Chemistry

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	QMAKECONF="%{_datadir}/qt/mkspecs/linux-g++/qmake.conf" \
	RINGDIR="%{_datadir}/xdrawchem" \
	BINDIR="%{_bindir}" install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Chemistry

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.txt HISTORY.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/xdrawchem
%dir %{_datadir}/xdrawchem
%{_datadir}/xdrawchem/*
%{_applnkdir}/Scientific/Chemistry/*.desktop
