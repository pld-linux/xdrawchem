Summary:	XDrawChem - A chemical drawing program
Summary(pl):	XDrawChem - Program do rysunków chemicznych
Name:		xdrawchem
Version:	1.3.2
Release:	0.5
License:	Modified BSD
Group:		X11/Applications/Science
Source0:	http://www.prism.gatech.edu/~gte067k/xdrawchem/%{name}-%{version}.tgz
Patch0:		%{name}-includes.patch
BuildRequires:	qt-devel >= 2.3
URL:		http://www.prism.gatech.edu/~gte067k/xdrawchem/
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
QTDIR=%{_includedir}/qt ; export QTDIR
%{__make} -f Makefile.RPM all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf HISTORY.txt README.txt TODO.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xdrawchem
%dir %{_libdir}/xdrawchem
%{_libdir}/xdrawchem/*
