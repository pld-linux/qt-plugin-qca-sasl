%define		rname qca-sasl
#
Summary:	Qt Cryptographic Architecture (QCA) SASL plugin
Summary(pl.UTF-8):	Wtyczka SASL dla Qt Cryptographic Architecture (QCA)
Name:		qt-plugin-%{rname}
Version:	1.0
Release:	5
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/qca/%{rname}-1.0.tar.bz2
# Source0-md5:	2e324cb45706f37a8d2b196f43428023
URL:		http://delta.affinix.com/qca/
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-devel >= 6:3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_libdir}/qt/plugins-mt/crypto

%description
A plugin to provide SASL capability to programs that utilize the Qt
Cryptographic Architecture (QCA).

%description -l pl.UTF-8
Wtyczka pozwalająca wykorzystać możliwości SASL w programach
korzystających z Qt Cryptographic Architecture (QCA).

%prep
%setup -qn %{rname}-%{version}

# This dir contains bad qcextra file, so prepare good one
sed -i \
	's,target.path=.*,target.path=%{_plugindir},' \
	qcextra

%build
export QTDIR=%{_prefix}
./configure

qmake %{rname}.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*.so
