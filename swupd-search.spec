#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-search
Version  : 5
Release  : 4
URL      : http://localhost/cgit/projects/swupd-local-search/snapshot/swupd-local-search-5.tar.xz
Source0  : http://localhost/cgit/projects/swupd-local-search/snapshot/swupd-local-search-5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: swupd-search-bin = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the swupd-search package.
Group: Binaries

%description bin
bin components for the swupd-search package.


%prep
%setup -q -n swupd-local-search-5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550447990
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1550447990
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd-search
