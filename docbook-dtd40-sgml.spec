Summary:	DocBook 4.0 SGML - DTD for technical documentation
Summary(pl.UTF-8):	DocBook 4.0 SGML - DTD przeznaczone do pisania dokumentacji technicznej
%define ver	4.0
%define sver	40
Name:		docbook-dtd%{sver}-sgml
Version:	1.0
Release:	1
Vendor:		OASIS
License:	Free
Group:		Applications/Publishing/SGML
Source0:	http://www.oasis-open.org/docbook/sgml/%{ver}/docbk%{sver}.zip
# Source0-md5:	fabcf7dd1d88b94797b7e5344389eab9
URL:		http://www.oasis-open.org/docbook/
BuildRequires:	unzip
Requires(post,postun):	sgml-common >= 0.5
Requires:	sgmlparser
Requires:	sgml-common >= 0.5
Provides:	docbook-dtd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docbook%{sver}-dtd
Obsoletes:	docbook-sgml-%{ver}

%description
DocBook 4.0 SGML - DTD for technical documentation.

%description -l pl.UTF-8
DocBook DTD jest zestawem definicji dokumentów przeznaczonych do
tworzenia dokumentacji programistycznej. Stosowany jest do pisania
podręczników systemowych, instrukcji technicznych jak i wielu innych
ciekawych rzeczy. Ten pakiet zawiera wersję DocBook 4.0 SGML.

%prep
%setup -q -c
chmod 644 *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

install *.dtd *.mod *.dcl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

# install catalog (but filter out ISO entities)
grep -v 'ISO ' docbook.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/catalog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q /etc/sgml/sgml-docbook-%{ver}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%postun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/sgml/docbook/sgml-dtd-4.0
