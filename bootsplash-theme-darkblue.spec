
%define	theme	darkblue

Summary:	Bootsplash - darkblue theme
Summary(pl.UTF-8):   Bootsplash - motyw darkblue
Name:		bootsplash-theme-%{theme}
Version:	1.2
Release:	2
Epoch:		0
License:	GPL v2
Group:		Themes
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	a5b64219f284ff772a4f3ebcd4f2bc34
URL:		http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-artwork/bootsplash/%{theme}/
Requires:	bootsplash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Darkblue PLD theme for bootsplash.

%description -l pl.UTF-8
Motyw PLD darkblue do bootsplash.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/bootsplash/themes/%{theme}
install -d $THEME_DIR{,/animations,/config,/images}
install %{theme}/animations/*.mng $THEME_DIR/animations
install %{theme}/config/*.cfg $THEME_DIR/config
install %{theme}/images/*.jpeg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/bootsplash/themes/%{theme}
