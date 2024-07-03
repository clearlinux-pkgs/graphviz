#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : graphviz
Version  : 11.0.0
Release  : 83
URL      : https://gitlab.com/graphviz/graphviz/-/archive/11.0.0/graphviz-11.0.0.tar.gz
Source0  : https://gitlab.com/graphviz/graphviz/-/archive/11.0.0/graphviz-11.0.0.tar.gz
Summary  : Container DataType library
Group    : Development/Tools
License  : BSD-2-Clause CPL-1.0 EPL-1.0 MIT
BuildRequires : bison
BuildRequires : bison-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : expat-dev
BuildRequires : flex
BuildRequires : freeglut-dev
BuildRequires : freetype-dev
BuildRequires : ghostscript
BuildRequires : ghostscript-dev
BuildRequires : groff
BuildRequires : gtk+-dev
BuildRequires : libXt-dev
BuildRequires : libgd-dev
BuildRequires : librsvg-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-2.0)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gdlib)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xrender)
BuildRequires : poppler-dev
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Move-config-path-to-var-lib-graphviz.patch
Patch2: 0002-Don-t-try-and-figure-out-libdir-from-maps.patch
Patch3: 0003-Enable-stateless-config.patch

%description
Graphviz - Graph Drawing Programs from AT&T Research and Lucent Bell Labs
See doc/build.html for prerequisites and detailed build notes.

%prep
%setup -q -n graphviz-11.0.0
cd %{_builddir}/graphviz-11.0.0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a graphviz-11.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719964477
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719964477
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/graphviz
cp %{_builddir}/graphviz-%{version}/COPYING %{buildroot}/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d || :
cp %{_builddir}/graphviz-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/graphviz/0435b8c8e59b4e3bcc367276e5e8db44debb1bf7 || :
cp %{_builddir}/graphviz-%{version}/contrib/java-dot/license.txt %{buildroot}/usr/share/package-licenses/graphviz/ff8f5786c5bfd83621338353fd37ca8148d45874 || :
cp %{_builddir}/graphviz-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/graphviz/0bece0f3e31e61c3b5afe821fec476190f0b3417 || :
cp %{_builddir}/graphviz-%{version}/epl-v10.html %{buildroot}/usr/share/package-licenses/graphviz/35666c54f2406125707e63edab12f2914d85ca76 || :
cp %{_builddir}/graphviz-%{version}/epl-v10.txt %{buildroot}/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d || :
cp %{_builddir}/graphviz-%{version}/lib/rbtree/LICENSE %{buildroot}/usr/share/package-licenses/graphviz/e5398178f20a2036de0eca59ed5d9668121fa15e || :
cp %{_builddir}/graphviz-%{version}/macosx/build/English.lproj/License.rtf %{buildroot}/usr/share/package-licenses/graphviz/288dbb0f336ec60c12e9ce96b3405da9a7e15c6d || :
cp %{_builddir}/graphviz-%{version}/plugin.demo/xgtk/COPYING %{buildroot}/usr/share/package-licenses/graphviz/f8c92c8978081caefdbfae2311a0947ca82a1315 || :
cp %{_builddir}/graphviz-%{version}/plugin.demo/xgtk/epl-v10.html %{buildroot}/usr/share/package-licenses/graphviz/35666c54f2406125707e63edab12f2914d85ca76 || :
cp %{_builddir}/graphviz-%{version}/plugin.demo/xgtk/epl-v10.txt %{buildroot}/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
install -m 0755 -D graphviz.conf %{buildroot}/usr/lib/tmpfiles.d/graphviz.conf

# Create default config file
mkdir -p %{buildroot}/usr/share/graphviz/
GV_CONFIG_PATH=%{buildroot}/usr/share/graphviz LD_LIBRARY_PATH=%{buildroot}/usr/lib64 %{buildroot}/usr/bin/dot -cv
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
