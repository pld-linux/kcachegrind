Summary:	The most beautiful way to optimize your applications
Name:		kcachegrind
Version:	0.4.4
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://kcachegrind.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	874e78af54a661495cbb29922133ab0f
URL:		http://kcachegrind.sourceforge.net/cgi-bin/show.cgi
Requires:	binutils
Requires:	graphviz
Requires:	valgrind-calltree
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The most beautiful way to optimize your applications.

%prep
%setup -q

%build
%configure
echo "all:" >doc/en/Makefile	# disable docbook documentation building
echo >>doc/en/Makefile
echo "install:" >>doc/en/Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.KDE TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/icons/*
%{_datadir}/mimelnk/application/*
