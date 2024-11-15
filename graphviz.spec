#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v21
# autospec commit: e822d6e48dc0
#
Name     : graphviz
Version  : 12.2.0
Release  : 89
URL      : https://gitlab.com/graphviz/graphviz/-/archive/12.2.0/graphviz-12.2.0.tar.gz
Source0  : https://gitlab.com/graphviz/graphviz/-/archive/12.2.0/graphviz-12.2.0.tar.gz
Summary  : Container DataType library
Group    : Development/Tools
License  : BSD-2-Clause CPL-1.0 EPL-1.0 MIT
Requires: graphviz-bin = %{version}-%{release}
Requires: graphviz-config = %{version}-%{release}
Requires: graphviz-data = %{version}-%{release}
Requires: graphviz-lib = %{version}-%{release}
Requires: graphviz-license = %{version}-%{release}
Requires: graphviz-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-qmake
BuildRequires : expat-dev
BuildRequires : file
BuildRequires : flex
BuildRequires : freeglut-dev
BuildRequires : ghostscript
BuildRequires : ghostscript-dev
BuildRequires : groff
BuildRequires : gtk+-dev
BuildRequires : libXt-dev
BuildRequires : libgd-dev
BuildRequires : librsvg-dev
BuildRequires : llvm
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gdlib)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(guile-3.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(xrender)
BuildRequires : poppler-dev
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Move-config-path-to-var-lib-graphviz.patch
Patch2: 0002-Don-t-try-and-figure-out-libdir-from-maps.patch
Patch3: 0003-Enable-stateless-config.patch
Patch4: 0004-Set-proper-dir-for-LD_LIBRARY_PATH.patch

%description
Graphviz - Graph Drawing Programs from AT&T Research and Lucent Bell Labs
See doc/build.html for prerequisites and detailed build notes.

%package bin
Summary: bin components for the graphviz package.
Group: Binaries
Requires: graphviz-data = %{version}-%{release}
Requires: graphviz-config = %{version}-%{release}
Requires: graphviz-license = %{version}-%{release}

%description bin
bin components for the graphviz package.


%package config
Summary: config components for the graphviz package.
Group: Default

%description config
config components for the graphviz package.


%package data
Summary: data components for the graphviz package.
Group: Data

%description data
data components for the graphviz package.


%package dev
Summary: dev components for the graphviz package.
Group: Development
Requires: graphviz-lib = %{version}-%{release}
Requires: graphviz-bin = %{version}-%{release}
Requires: graphviz-data = %{version}-%{release}
Provides: graphviz-devel = %{version}-%{release}
Requires: graphviz = %{version}-%{release}

%description dev
dev components for the graphviz package.


%package doc
Summary: doc components for the graphviz package.
Group: Documentation
Requires: graphviz-man = %{version}-%{release}

%description doc
doc components for the graphviz package.


%package extras
Summary: extras components for the graphviz package.
Group: Default

%description extras
extras components for the graphviz package.


%package lib
Summary: lib components for the graphviz package.
Group: Libraries
Requires: graphviz-data = %{version}-%{release}
Requires: graphviz-license = %{version}-%{release}

%description lib
lib components for the graphviz package.


%package license
Summary: license components for the graphviz package.
Group: Default

%description license
license components for the graphviz package.


%package man
Summary: man components for the graphviz package.
Group: Default

%description man
man components for the graphviz package.


%prep
%setup -q -n graphviz-12.2.0
cd %{_builddir}/graphviz-12.2.0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
pushd ..
cp -a graphviz-12.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731102630
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
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1731102630
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
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
install -m 0755 -D graphviz.conf %{buildroot}/usr/lib/tmpfiles.d/graphviz.conf

# Create default config file
mkdir -p %{buildroot}/usr/share/graphviz/
GV_CONFIG_PATH=%{buildroot}/usr/share/graphviz LD_LIBRARY_PATH=%{buildroot}/usr/lib64 %{buildroot}/usr/bin/dot -cv
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/graphviz/tcl/pkgIndex.tcl
/usr/lib64/tcl8.6/graphviz/pkgIndex.tcl

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/acyclic
/V3/usr/bin/bcomps
/V3/usr/bin/ccomps
/V3/usr/bin/cluster
/V3/usr/bin/dijkstra
/V3/usr/bin/dot
/V3/usr/bin/edgepaint
/V3/usr/bin/gc
/V3/usr/bin/gml2gv
/V3/usr/bin/graphml2gv
/V3/usr/bin/gv2gml
/V3/usr/bin/gvcolor
/V3/usr/bin/gvgen
/V3/usr/bin/gvmap
/V3/usr/bin/gvpack
/V3/usr/bin/gvpr
/V3/usr/bin/gxl2gv
/V3/usr/bin/mm2gv
/V3/usr/bin/nop
/V3/usr/bin/prune
/V3/usr/bin/sccmap
/V3/usr/bin/tred
/V3/usr/bin/unflatten
/usr/bin/acyclic
/usr/bin/bcomps
/usr/bin/ccomps
/usr/bin/circo
/usr/bin/cluster
/usr/bin/dijkstra
/usr/bin/dot
/usr/bin/dot2gxl
/usr/bin/edgepaint
/usr/bin/fdp
/usr/bin/gc
/usr/bin/gml2gv
/usr/bin/graphml2gv
/usr/bin/gv2gml
/usr/bin/gv2gxl
/usr/bin/gvcolor
/usr/bin/gvgen
/usr/bin/gvmap
/usr/bin/gvmap.sh
/usr/bin/gvpack
/usr/bin/gvpr
/usr/bin/gxl2dot
/usr/bin/gxl2gv
/usr/bin/mm2gv
/usr/bin/neato
/usr/bin/nop
/usr/bin/osage
/usr/bin/patchwork
/usr/bin/prune
/usr/bin/sccmap
/usr/bin/sfdp
/usr/bin/tred
/usr/bin/twopi
/usr/bin/unflatten
/usr/bin/vimdot

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/graphviz.conf

%files data
%defattr(-,root,root,-)
/usr/share/graphviz/config6
/usr/share/graphviz/demo/doted.tcl
/usr/share/graphviz/demo/doted.tcl.README
/usr/share/graphviz/demo/entities.html
/usr/share/graphviz/demo/entities.tcl
/usr/share/graphviz/demo/entities.tcl.README
/usr/share/graphviz/demo/gcat.tcl
/usr/share/graphviz/demo/gcat.tcl.README
/usr/share/graphviz/demo/modgraph.tcl
/usr/share/graphviz/demo/pathplan.tcl
/usr/share/graphviz/demo/pathplan.tcl.README
/usr/share/graphviz/demo/pathplan_data/boxes.dat
/usr/share/graphviz/demo/pathplan_data/dpd.dat
/usr/share/graphviz/demo/pathplan_data/funny.dat
/usr/share/graphviz/demo/pathplan_data/maze.dat
/usr/share/graphviz/demo/pathplan_data/nested.dat
/usr/share/graphviz/demo/pathplan_data/northo.dat
/usr/share/graphviz/demo/pathplan_data/obs.dat
/usr/share/graphviz/demo/pathplan_data/other.dat
/usr/share/graphviz/demo/pathplan_data/paths.dat
/usr/share/graphviz/demo/pathplan_data/rotor.dat
/usr/share/graphviz/demo/pathplan_data/u.dat
/usr/share/graphviz/demo/pathplan_data/unknown.dat
/usr/share/graphviz/graphs/directed/KW91.gv
/usr/share/graphviz/graphs/directed/Latin1.gv
/usr/share/graphviz/graphs/directed/NaN.gv
/usr/share/graphviz/graphs/directed/abstract.gv
/usr/share/graphviz/graphs/directed/alf.gv
/usr/share/graphviz/graphs/directed/arrows.gv
/usr/share/graphviz/graphs/directed/awilliams.gv
/usr/share/graphviz/graphs/directed/biological.gv
/usr/share/graphviz/graphs/directed/clust.gv
/usr/share/graphviz/graphs/directed/clust1.gv
/usr/share/graphviz/graphs/directed/clust2.gv
/usr/share/graphviz/graphs/directed/clust3.gv
/usr/share/graphviz/graphs/directed/clust4.gv
/usr/share/graphviz/graphs/directed/clust5.gv
/usr/share/graphviz/graphs/directed/crazy.gv
/usr/share/graphviz/graphs/directed/ctext.gv
/usr/share/graphviz/graphs/directed/dfa.gv
/usr/share/graphviz/graphs/directed/fig6.gv
/usr/share/graphviz/graphs/directed/fsm.gv
/usr/share/graphviz/graphs/directed/grammar.gv
/usr/share/graphviz/graphs/directed/hashtable.gv
/usr/share/graphviz/graphs/directed/honda-tokoro.gv
/usr/share/graphviz/graphs/directed/japanese.gv
/usr/share/graphviz/graphs/directed/jcctree.gv
/usr/share/graphviz/graphs/directed/jsort.gv
/usr/share/graphviz/graphs/directed/ldbxtried.gv
/usr/share/graphviz/graphs/directed/longflat.gv
/usr/share/graphviz/graphs/directed/mike.gv
/usr/share/graphviz/graphs/directed/nhg.gv
/usr/share/graphviz/graphs/directed/oldarrows.gv
/usr/share/graphviz/graphs/directed/pgram.gv
/usr/share/graphviz/graphs/directed/pm2way.gv
/usr/share/graphviz/graphs/directed/pmpipe.gv
/usr/share/graphviz/graphs/directed/polypoly.gv
/usr/share/graphviz/graphs/directed/proc3d.gv
/usr/share/graphviz/graphs/directed/psfonttest.gv
/usr/share/graphviz/graphs/directed/record2.gv
/usr/share/graphviz/graphs/directed/records.gv
/usr/share/graphviz/graphs/directed/rowe.gv
/usr/share/graphviz/graphs/directed/russian.gv
/usr/share/graphviz/graphs/directed/sdh.gv
/usr/share/graphviz/graphs/directed/shells.gv
/usr/share/graphviz/graphs/directed/states.gv
/usr/share/graphviz/graphs/directed/structs.gv
/usr/share/graphviz/graphs/directed/switch.gv
/usr/share/graphviz/graphs/directed/table.gv
/usr/share/graphviz/graphs/directed/train11.gv
/usr/share/graphviz/graphs/directed/trapeziumlr.gv
/usr/share/graphviz/graphs/directed/tree.gv
/usr/share/graphviz/graphs/directed/triedds.gv
/usr/share/graphviz/graphs/directed/try.gv
/usr/share/graphviz/graphs/directed/unix.gv
/usr/share/graphviz/graphs/directed/unix2.gv
/usr/share/graphviz/graphs/directed/viewfile.gv
/usr/share/graphviz/graphs/directed/world.gv
/usr/share/graphviz/graphs/undirected/ER.gv
/usr/share/graphviz/graphs/undirected/Heawood.gv
/usr/share/graphviz/graphs/undirected/Petersen.gv
/usr/share/graphviz/graphs/undirected/ngk10_4.gv
/usr/share/graphviz/graphs/undirected/process.gv
/usr/share/graphviz/gvpr/addedges
/usr/share/graphviz/gvpr/addranks
/usr/share/graphviz/gvpr/addrings
/usr/share/graphviz/gvpr/anon
/usr/share/graphviz/gvpr/attr
/usr/share/graphviz/gvpr/bb
/usr/share/graphviz/gvpr/bbox
/usr/share/graphviz/gvpr/binduce
/usr/share/graphviz/gvpr/bipart
/usr/share/graphviz/gvpr/chkclusters
/usr/share/graphviz/gvpr/chkedges
/usr/share/graphviz/gvpr/cliptree
/usr/share/graphviz/gvpr/col
/usr/share/graphviz/gvpr/collapse
/usr/share/graphviz/gvpr/color
/usr/share/graphviz/gvpr/cycle
/usr/share/graphviz/gvpr/dechain
/usr/share/graphviz/gvpr/deghist
/usr/share/graphviz/gvpr/deledges
/usr/share/graphviz/gvpr/delmulti
/usr/share/graphviz/gvpr/delnodes
/usr/share/graphviz/gvpr/depath
/usr/share/graphviz/gvpr/dijkstra
/usr/share/graphviz/gvpr/flatten
/usr/share/graphviz/gvpr/get-layers-list
/usr/share/graphviz/gvpr/group
/usr/share/graphviz/gvpr/histogram
/usr/share/graphviz/gvpr/indent
/usr/share/graphviz/gvpr/knbhd
/usr/share/graphviz/gvpr/maxdeg
/usr/share/graphviz/gvpr/path
/usr/share/graphviz/gvpr/rotate
/usr/share/graphviz/gvpr/scale
/usr/share/graphviz/gvpr/scalexy
/usr/share/graphviz/gvpr/span
/usr/share/graphviz/gvpr/topon
/usr/share/graphviz/gvpr/treetoclust

%files dev
%defattr(-,root,root,-)
/usr/include/graphviz/arith.h
/usr/include/graphviz/cdt.h
/usr/include/graphviz/cgraph.h
/usr/include/graphviz/color.h
/usr/include/graphviz/geom.h
/usr/include/graphviz/graphviz_version.h
/usr/include/graphviz/gvc.h
/usr/include/graphviz/gvcext.h
/usr/include/graphviz/gvcjob.h
/usr/include/graphviz/gvcommon.h
/usr/include/graphviz/gvconfig.h
/usr/include/graphviz/gvplugin.h
/usr/include/graphviz/gvplugin_device.h
/usr/include/graphviz/gvplugin_layout.h
/usr/include/graphviz/gvplugin_loadimage.h
/usr/include/graphviz/gvplugin_render.h
/usr/include/graphviz/gvplugin_textlayout.h
/usr/include/graphviz/gvpr.h
/usr/include/graphviz/pack.h
/usr/include/graphviz/pathgeom.h
/usr/include/graphviz/pathplan.h
/usr/include/graphviz/textspan.h
/usr/include/graphviz/types.h
/usr/include/graphviz/usershape.h
/usr/include/graphviz/xdot.h
/usr/lib64/libcdt.so
/usr/lib64/libcgraph.so
/usr/lib64/libgvc.so
/usr/lib64/libgvpr.so
/usr/lib64/libpathplan.so
/usr/lib64/libxdot.so
/usr/lib64/pkgconfig/libcdt.pc
/usr/lib64/pkgconfig/libcgraph.pc
/usr/lib64/pkgconfig/libgvc.pc
/usr/lib64/pkgconfig/libgvpr.pc
/usr/lib64/pkgconfig/libpathplan.pc
/usr/lib64/pkgconfig/libxdot.pc
/usr/share/man/man3/cdt.3
/usr/share/man/man3/cgraph.3
/usr/share/man/man3/expr.3
/usr/share/man/man3/gdtclft.3tcl
/usr/share/man/man3/gvc.3
/usr/share/man/man3/gvpr.3
/usr/share/man/man3/pack.3
/usr/share/man/man3/pathplan.3
/usr/share/man/man3/tcldot.3tcl
/usr/share/man/man3/xdot.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/graphviz/*

%files extras
%defattr(-,root,root,-)
/V3/usr/bin/diffimg
/V3/usr/bin/dot_builtins
/V3/usr/lib64/graphviz/libgvplugin_gd.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_gdk.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_gs.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_pango.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_xlib.so.6.0.0
/V3/usr/lib64/graphviz/tcl/libgdtclft.so
/V3/usr/lib64/graphviz/tcl/libtcldot.so
/V3/usr/lib64/graphviz/tcl/libtcldot_builtin.so
/V3/usr/lib64/graphviz/tcl/libtclplan.so
/V3/usr/lib64/tcl8.6/graphviz/libgdtclft.so
/V3/usr/lib64/tcl8.6/graphviz/libtcldot.so
/V3/usr/lib64/tcl8.6/graphviz/libtcldot_builtin.so
/V3/usr/lib64/tcl8.6/graphviz/libtclplan.so
/usr/bin/diffimg
/usr/bin/dot_builtins
/usr/lib64/graphviz/libgvplugin_gd.so
/usr/lib64/graphviz/libgvplugin_gd.so.6
/usr/lib64/graphviz/libgvplugin_gd.so.6.0.0
/usr/lib64/graphviz/libgvplugin_gdk.so
/usr/lib64/graphviz/libgvplugin_gdk.so.6
/usr/lib64/graphviz/libgvplugin_gdk.so.6.0.0
/usr/lib64/graphviz/libgvplugin_gs.so
/usr/lib64/graphviz/libgvplugin_gs.so.6
/usr/lib64/graphviz/libgvplugin_gs.so.6.0.0
/usr/lib64/graphviz/libgvplugin_pango.so
/usr/lib64/graphviz/libgvplugin_pango.so.6
/usr/lib64/graphviz/libgvplugin_pango.so.6.0.0
/usr/lib64/graphviz/libgvplugin_xlib.so
/usr/lib64/graphviz/libgvplugin_xlib.so.6
/usr/lib64/graphviz/libgvplugin_xlib.so.6.0.0
/usr/lib64/graphviz/tcl/libgdtclft.so
/usr/lib64/graphviz/tcl/libtcldot.so
/usr/lib64/graphviz/tcl/libtcldot_builtin.so
/usr/lib64/graphviz/tcl/libtclplan.so
/usr/lib64/tcl8.6/graphviz/libgdtclft.so
/usr/lib64/tcl8.6/graphviz/libtcldot.so
/usr/lib64/tcl8.6/graphviz/libtcldot_builtin.so
/usr/lib64/tcl8.6/graphviz/libtclplan.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/graphviz/libgvplugin_core.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_dot_layout.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_kitty.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_neato_layout.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_poppler.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_rsvg.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_vt.so.6.0.0
/V3/usr/lib64/graphviz/libgvplugin_webp.so.6.0.0
/V3/usr/lib64/libcdt.so.5.0.0
/V3/usr/lib64/libcgraph.so.6.0.0
/V3/usr/lib64/libgvc.so.6.0.0
/V3/usr/lib64/libgvpr.so.2.0.0
/V3/usr/lib64/libpathplan.so.4.0.0
/V3/usr/lib64/libxdot.so.4.0.0
/usr/lib64/graphviz/libgvplugin_core.so
/usr/lib64/graphviz/libgvplugin_core.so.6
/usr/lib64/graphviz/libgvplugin_core.so.6.0.0
/usr/lib64/graphviz/libgvplugin_dot_layout.so
/usr/lib64/graphviz/libgvplugin_dot_layout.so.6
/usr/lib64/graphviz/libgvplugin_dot_layout.so.6.0.0
/usr/lib64/graphviz/libgvplugin_kitty.so
/usr/lib64/graphviz/libgvplugin_kitty.so.6
/usr/lib64/graphviz/libgvplugin_kitty.so.6.0.0
/usr/lib64/graphviz/libgvplugin_neato_layout.so
/usr/lib64/graphviz/libgvplugin_neato_layout.so.6
/usr/lib64/graphviz/libgvplugin_neato_layout.so.6.0.0
/usr/lib64/graphviz/libgvplugin_poppler.so
/usr/lib64/graphviz/libgvplugin_poppler.so.6
/usr/lib64/graphviz/libgvplugin_poppler.so.6.0.0
/usr/lib64/graphviz/libgvplugin_rsvg.so
/usr/lib64/graphviz/libgvplugin_rsvg.so.6
/usr/lib64/graphviz/libgvplugin_rsvg.so.6.0.0
/usr/lib64/graphviz/libgvplugin_vt.so
/usr/lib64/graphviz/libgvplugin_vt.so.6
/usr/lib64/graphviz/libgvplugin_vt.so.6.0.0
/usr/lib64/graphviz/libgvplugin_webp.so
/usr/lib64/graphviz/libgvplugin_webp.so.6
/usr/lib64/graphviz/libgvplugin_webp.so.6.0.0
/usr/lib64/libcdt.so.5
/usr/lib64/libcdt.so.5.0.0
/usr/lib64/libcgraph.so.6
/usr/lib64/libcgraph.so.6.0.0
/usr/lib64/libgvc.so.6
/usr/lib64/libgvc.so.6.0.0
/usr/lib64/libgvpr.so.2
/usr/lib64/libgvpr.so.2.0.0
/usr/lib64/libpathplan.so.4
/usr/lib64/libpathplan.so.4.0.0
/usr/lib64/libxdot.so.4
/usr/lib64/libxdot.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/graphviz/0435b8c8e59b4e3bcc367276e5e8db44debb1bf7
/usr/share/package-licenses/graphviz/0bece0f3e31e61c3b5afe821fec476190f0b3417
/usr/share/package-licenses/graphviz/288dbb0f336ec60c12e9ce96b3405da9a7e15c6d
/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d
/usr/share/package-licenses/graphviz/35666c54f2406125707e63edab12f2914d85ca76
/usr/share/package-licenses/graphviz/e5398178f20a2036de0eca59ed5d9668121fa15e
/usr/share/package-licenses/graphviz/f8c92c8978081caefdbfae2311a0947ca82a1315
/usr/share/package-licenses/graphviz/ff8f5786c5bfd83621338353fd37ca8148d45874

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/acyclic.1
/usr/share/man/man1/bcomps.1
/usr/share/man/man1/ccomps.1
/usr/share/man/man1/circo.1
/usr/share/man/man1/cluster.1
/usr/share/man/man1/diffimg.1
/usr/share/man/man1/dijkstra.1
/usr/share/man/man1/dot.1
/usr/share/man/man1/dot2gxl.1
/usr/share/man/man1/edgepaint.1
/usr/share/man/man1/fdp.1
/usr/share/man/man1/gc.1
/usr/share/man/man1/gml2gv.1
/usr/share/man/man1/graphml2gv.1
/usr/share/man/man1/gv2gml.1
/usr/share/man/man1/gv2gxl.1
/usr/share/man/man1/gvcolor.1
/usr/share/man/man1/gvgen.1
/usr/share/man/man1/gvmap.1
/usr/share/man/man1/gvmap.sh.1
/usr/share/man/man1/gvpack.1
/usr/share/man/man1/gvpr.1
/usr/share/man/man1/gxl2dot.1
/usr/share/man/man1/gxl2gv.1
/usr/share/man/man1/mm2gv.1
/usr/share/man/man1/neato.1
/usr/share/man/man1/nop.1
/usr/share/man/man1/osage.1
/usr/share/man/man1/patchwork.1
/usr/share/man/man1/prune.1
/usr/share/man/man1/sccmap.1
/usr/share/man/man1/sfdp.1
/usr/share/man/man1/tred.1
/usr/share/man/man1/twopi.1
/usr/share/man/man1/unflatten.1
/usr/share/man/man1/vimdot.1
/usr/share/man/man7/graphviz.7
