Summary:	Metacity window manager configuration program
Summary(pl):	Program konfiguracyjny zarz�dcy okien Metacity
Name:		metacity-setup
Version:	0.6
Release:	4
License:	GPL
Group:		X11/Window Managers
Source0:	%{name}-%{version}.tar.bz2
URL:		http://plastercast.tzo.com/~plastercast/Projects/
BuildRequires:	libgnomeui2-devel
Requires:	metacity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
metacity-setup is simply a much easier way to configure Metacity then
having to use gconftool or gconf-editor. It allows you to change
themes, focus settings, and the number of workspaces.

%description -l pl
U�ycie metacity-setup jest du�o prostszym sposobem na skonfigurowanie
Metacity ni� u�ywanie gconftoola lub gconf-editora. metacity-setup
pozwala na zmian� motyw�w, ustawie� focusa i liczby ekran�w
wirtualnych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{_bindir}/%name" icon="%{_datadir}/pixmaps/metacity-setup-icon.png" longtitle="Metacity Window Manager Properties" title="Metacity-Setup" needs=gnome section="Configuration/GNOME"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{_bindir}/metacity-setup
%{_pixmapsdir}/metacity-setup-icon.png
%dir %{_datadir}/metacity-setup
%dir %{_datadir}/metacity-setup/pixmaps
%{_datadir}/metacity-setup/pixmaps/metacity-setup-icon.png
%{_datadir}/control-center-2.0/capplets/metacity-setup.desktop
%{_menudir}/%{name}
