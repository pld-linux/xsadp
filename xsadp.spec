Summary:	Sing Along Disc Player
Summary:	¦piewaj Sam - Odtwarzacz P³yt CD
Name:		xsadp
Version:	3.1.5d
Release:	3
License:	custom
Group:		Applications/Sound
Source0:	http://www.geocities.com/xsadp/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.alphalink.com.au/~michg/ace/sadp/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-driver-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRequires:	xforms-devel >= 0.88
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
SADP is and advanced CD player for Linux X11. Features: spectrum
analyser, oscillator, on-board mixer, shuffle mode, multiple play
lists and skip lists. Maintains local data base and provides access to
remote CD data bases over the Internet. Features: compressed fast
access data base, multiple preference sets, optional storing mixer
volumes for each disc. SADP can port data from Workman and xmcd data
bases (the later is also used by CDDB-1, and some CDDB-aware
applications). Other SADP features include CD-TEXT and CD-Extra
support, CD multichanger support, interactive icon and docking
facilities with Window Maker. Supports Linux Sound Driver, Open Sound
System and Advanced Linux Sound Architecture. Sound driver and
internet support are essential but not mandatory. SADP can be
customized for a particular brand of CD through time-out options.
Special support for SCSI CD ROM and IDE SCSI emulation is provided.
Available in console mode (ncurses 3+, 5.0 recommended) and GUI mode.

%description -l pl
SADP jest zaawansowan± odtwarzark± p³yt CD dla Linux X11. Jego zalety
to analizator spektrum, oscyloskop, mikser, tryb mieszania (shuffle),
wiele list odtwarzania oraz listy pomijania utworów. SADP zarz±dza
lokaln± baz± oraz daje mo¿liwo¶c dostêpu do zdalnych baz danych o
p³ytach CD poprzez Internet. Zalety w tym przypadku to: skompresowane,
szybkie bazy danych, ustawienia preferencji, opcjonalne zapisywanie
ustawieñ miksera dla ka¿dego dysku. SADP potrafi korzystaæ z baz
danych Workmana oraz xmcd. Inne zalety SAPD to obs³uga CD-TEXT oraz
CD-Extra, obs³uga zmieniarek CD, interaktywna ikona oraz dokowanie w
WindowMakerze.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	CPPFLAGS="-I/usr/include/ncurses" \
	CFLAGS="-I/usr/include/ncurses" \
	--with-rpm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_libdir}/X11/app-defaults}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install *.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/XSadp
install icons/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.1ST.OLD COPYRIGHT Readme.install xsadp.lsm documentation/CDExtension.txt
%doc documentation/DataBase.txt documentation/KernelMisc.txt documentation/MiniWindow.txt
%doc documentation/MouseWheel.txt documentation/ALSA.txt documentation/xmcd_database.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sadp
%{_pixmapsdir}/*
%{_mandir}/man?/*
%{_libdir}/X11/app-defaults/XSadp
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/rcddb.sites
