
Summary:	Bootsplash - darkblue theme
Summary(pl):	Bootsplash - motyw darkblue
Name:		bootsplash-theme-darkblue
Version:	1.2
Release:	1
Epoch:		0
License:	GPL v2
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	a5b64219f284ff772a4f3ebcd4f2bc34
URL:		http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-artwork/bootsplash/darkblue/
Requires:	bootsplash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Darkblue PLD theme for bootsplash.

%description -l pl
Motyw PLD darkblue do bootsplash.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/bootsplash/themes/darkblue
install -d $THEME_DIR{,/animations,/config,/images}
install darkblue/animations/*.mng $THEME_DIR/animations
install darkblue/config/*.cfg $THEME_DIR/config
install darkblue/images/*.jpeg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/bootsplash/themes/darkblue/
%dir %{_sysconfdir}/bootsplash/themes/darkblue/animations
%{_sysconfdir}/bootsplash/themes/darkblue/animations/*
%dir %{_sysconfdir}/bootsplash/themes/darkblue/config
%{_sysconfdir}/bootsplash/themes/darkblue/config/*
%dir %{_sysconfdir}/bootsplash/themes/darkblue/images
%{_sysconfdir}/bootsplash/themes/darkblue/images/*
