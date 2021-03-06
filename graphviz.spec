#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : graphviz
Version  : 2.44.1
Release  : 42
URL      : https://gitlab.com/graphviz/graphviz/-/archive/2.44.1/graphviz-2.44.1.tar.gz
Source0  : https://gitlab.com/graphviz/graphviz/-/archive/2.44.1/graphviz-2.44.1.tar.gz
Summary  : Library for parsing graphs in xdot format
Group    : Development/Tools
License  : BSD-2-Clause CPL-1.0 EPL-1.0 MIT
Requires: graphviz-bin = %{version}-%{release}
Requires: graphviz-config = %{version}-%{release}
Requires: graphviz-data = %{version}-%{release}
Requires: graphviz-lib = %{version}-%{release}
Requires: graphviz-license = %{version}-%{release}
Requires: graphviz-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-golang
BuildRequires : buildreq-qmake
BuildRequires : expat-dev
BuildRequires : flex
BuildRequires : freeglut-dev
BuildRequires : ghostscript
BuildRequires : ghostscript-dev
BuildRequires : groff
BuildRequires : gtk+-dev
BuildRequires : libXt-dev
BuildRequires : libgd-dev
BuildRequires : librsvg-dev
BuildRequires : libwebp-dev
BuildRequires : llvm
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xrender)
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
Patch1: 0001-Move-config-path-to-var-lib-graphviz.patch

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
%setup -q -n graphviz-2.44.1
cd %{_builddir}/graphviz-2.44.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609898084
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1609898084
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/graphviz
cp %{_builddir}/graphviz-2.44.1/COPYING %{buildroot}/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d
cp %{_builddir}/graphviz-2.44.1/LICENSE %{buildroot}/usr/share/package-licenses/graphviz/0435b8c8e59b4e3bcc367276e5e8db44debb1bf7
cp %{_builddir}/graphviz-2.44.1/contrib/java-dot/license.txt %{buildroot}/usr/share/package-licenses/graphviz/ff8f5786c5bfd83621338353fd37ca8148d45874
cp %{_builddir}/graphviz-2.44.1/debian/copyright %{buildroot}/usr/share/package-licenses/graphviz/0bece0f3e31e61c3b5afe821fec476190f0b3417
cp %{_builddir}/graphviz-2.44.1/epl-v10.html %{buildroot}/usr/share/package-licenses/graphviz/35666c54f2406125707e63edab12f2914d85ca76
cp %{_builddir}/graphviz-2.44.1/epl-v10.txt %{buildroot}/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d
cp %{_builddir}/graphviz-2.44.1/lib/rbtree/LICENSE %{buildroot}/usr/share/package-licenses/graphviz/e5398178f20a2036de0eca59ed5d9668121fa15e
cp %{_builddir}/graphviz-2.44.1/macosx/build/English.lproj/License.rtf %{buildroot}/usr/share/package-licenses/graphviz/288dbb0f336ec60c12e9ce96b3405da9a7e15c6d
cp %{_builddir}/graphviz-2.44.1/plugin.demo/xgtk/COPYING %{buildroot}/usr/share/package-licenses/graphviz/f8c92c8978081caefdbfae2311a0947ca82a1315
cp %{_builddir}/graphviz-2.44.1/plugin.demo/xgtk/epl-v10.html %{buildroot}/usr/share/package-licenses/graphviz/35666c54f2406125707e63edab12f2914d85ca76
cp %{_builddir}/graphviz-2.44.1/plugin.demo/xgtk/epl-v10.txt %{buildroot}/usr/share/package-licenses/graphviz/3348e5430ba4fb49fa8eb6e9caf4f06266639d0d
%make_install
## install_append content
install -m 0755 -D graphviz.conf %{buildroot}/usr/lib/tmpfiles.d/graphviz.conf
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/graphviz/tcl/pkgIndex.tcl
/usr/lib64/tcl8.6/graphviz/pkgIndex.tcl

%files bin
%defattr(-,root,root,-)
/usr/bin/acyclic
/usr/bin/bcomps
/usr/bin/ccomps
/usr/bin/circo
/usr/bin/cluster
/usr/bin/dijkstra
/usr/bin/dot
/usr/bin/dot2gxl
/usr/bin/dotty
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
/usr/bin/lneato
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
/usr/share/graphviz/doc/AUTHORS
/usr/share/graphviz/doc/CHANGELOG.md
/usr/share/graphviz/doc/COPYING
/usr/share/graphviz/doc/Dot.ref
/usr/share/graphviz/doc/NEWS
/usr/share/graphviz/doc/addingLayout.txt
/usr/share/graphviz/doc/cpl1.0.txt
/usr/share/graphviz/doc/fontfaq.txt
/usr/share/graphviz/doc/html/FAQ.html
/usr/share/graphviz/doc/html/build.html
/usr/share/graphviz/doc/html/char.html
/usr/share/graphviz/doc/html/gdtclft.entities.example.png
/usr/share/graphviz/doc/html/index.html
/usr/share/graphviz/doc/html/info/Mcircle.gif
/usr/share/graphviz/doc/html/info/Mdiamond.gif
/usr/share/graphviz/doc/html/info/Msquare.gif
/usr/share/graphviz/doc/html/info/a_box.gif
/usr/share/graphviz/doc/html/info/a_crow.gif
/usr/share/graphviz/doc/html/info/a_diamond.gif
/usr/share/graphviz/doc/html/info/a_dot.gif
/usr/share/graphviz/doc/html/info/a_ediamond.gif
/usr/share/graphviz/doc/html/info/a_empty.gif
/usr/share/graphviz/doc/html/info/a_forward.gif
/usr/share/graphviz/doc/html/info/a_halfopen.gif
/usr/share/graphviz/doc/html/info/a_inv.gif
/usr/share/graphviz/doc/html/info/a_invdot.gif
/usr/share/graphviz/doc/html/info/a_invempty.gif
/usr/share/graphviz/doc/html/info/a_invodot.gif
/usr/share/graphviz/doc/html/info/a_lteeoldiamond.gif
/usr/share/graphviz/doc/html/info/a_nohead.gif
/usr/share/graphviz/doc/html/info/a_none.gif
/usr/share/graphviz/doc/html/info/a_normal.gif
/usr/share/graphviz/doc/html/info/a_obox.gif
/usr/share/graphviz/doc/html/info/a_odiamond.gif
/usr/share/graphviz/doc/html/info/a_odot.gif
/usr/share/graphviz/doc/html/info/a_open.gif
/usr/share/graphviz/doc/html/info/a_tee.gif
/usr/share/graphviz/doc/html/info/aa_box.gif
/usr/share/graphviz/doc/html/info/aa_crow.gif
/usr/share/graphviz/doc/html/info/aa_diamond.gif
/usr/share/graphviz/doc/html/info/aa_dot.gif
/usr/share/graphviz/doc/html/info/aa_inv.gif
/usr/share/graphviz/doc/html/info/aa_lbox.gif
/usr/share/graphviz/doc/html/info/aa_lcrow.gif
/usr/share/graphviz/doc/html/info/aa_ldiamond.gif
/usr/share/graphviz/doc/html/info/aa_linv.gif
/usr/share/graphviz/doc/html/info/aa_lnormal.gif
/usr/share/graphviz/doc/html/info/aa_ltee.gif
/usr/share/graphviz/doc/html/info/aa_lvee.gif
/usr/share/graphviz/doc/html/info/aa_none.gif
/usr/share/graphviz/doc/html/info/aa_normal.gif
/usr/share/graphviz/doc/html/info/aa_obox.gif
/usr/share/graphviz/doc/html/info/aa_odiamond.gif
/usr/share/graphviz/doc/html/info/aa_odot.gif
/usr/share/graphviz/doc/html/info/aa_oinv.gif
/usr/share/graphviz/doc/html/info/aa_olbox.gif
/usr/share/graphviz/doc/html/info/aa_oldiamond.gif
/usr/share/graphviz/doc/html/info/aa_olinv.gif
/usr/share/graphviz/doc/html/info/aa_olnormal.gif
/usr/share/graphviz/doc/html/info/aa_onormal.gif
/usr/share/graphviz/doc/html/info/aa_orbox.gif
/usr/share/graphviz/doc/html/info/aa_ordiamond.gif
/usr/share/graphviz/doc/html/info/aa_orinv.gif
/usr/share/graphviz/doc/html/info/aa_ornormal.gif
/usr/share/graphviz/doc/html/info/aa_rbox.gif
/usr/share/graphviz/doc/html/info/aa_rcrow.gif
/usr/share/graphviz/doc/html/info/aa_rdiamond.gif
/usr/share/graphviz/doc/html/info/aa_rinv.gif
/usr/share/graphviz/doc/html/info/aa_rnormal.gif
/usr/share/graphviz/doc/html/info/aa_rtee.gif
/usr/share/graphviz/doc/html/info/aa_rvee.gif
/usr/share/graphviz/doc/html/info/aa_tee.gif
/usr/share/graphviz/doc/html/info/aa_vee.gif
/usr/share/graphviz/doc/html/info/arrows.html
/usr/share/graphviz/doc/html/info/attrs.html
/usr/share/graphviz/doc/html/info/back.gif
/usr/share/graphviz/doc/html/info/both.gif
/usr/share/graphviz/doc/html/info/box.gif
/usr/share/graphviz/doc/html/info/box3d.gif
/usr/share/graphviz/doc/html/info/c_bold.png
/usr/share/graphviz/doc/html/info/c_dashed.png
/usr/share/graphviz/doc/html/info/c_dotted.png
/usr/share/graphviz/doc/html/info/c_filled.png
/usr/share/graphviz/doc/html/info/c_rounded.png
/usr/share/graphviz/doc/html/info/c_solid.png
/usr/share/graphviz/doc/html/info/c_striped.png
/usr/share/graphviz/doc/html/info/circle.gif
/usr/share/graphviz/doc/html/info/colorlist.gif
/usr/share/graphviz/doc/html/info/colors.html
/usr/share/graphviz/doc/html/info/command.html
/usr/share/graphviz/doc/html/info/component.gif
/usr/share/graphviz/doc/html/info/constraint.gif
/usr/share/graphviz/doc/html/info/cylinder.gif
/usr/share/graphviz/doc/html/info/diamond.gif
/usr/share/graphviz/doc/html/info/doublecircle.gif
/usr/share/graphviz/doc/html/info/doubleoctagon.gif
/usr/share/graphviz/doc/html/info/e_bold.png
/usr/share/graphviz/doc/html/info/e_dashed.png
/usr/share/graphviz/doc/html/info/e_dotted.png
/usr/share/graphviz/doc/html/info/e_solid.png
/usr/share/graphviz/doc/html/info/egg.gif
/usr/share/graphviz/doc/html/info/ellipse.gif
/usr/share/graphviz/doc/html/info/fill.gif
/usr/share/graphviz/doc/html/info/folder.gif
/usr/share/graphviz/doc/html/info/forward.gif
/usr/share/graphviz/doc/html/info/g_lin0.png
/usr/share/graphviz/doc/html/info/g_lin180.png
/usr/share/graphviz/doc/html/info/g_lin270.png
/usr/share/graphviz/doc/html/info/g_lin360.png
/usr/share/graphviz/doc/html/info/g_lin45.png
/usr/share/graphviz/doc/html/info/g_lin90.png
/usr/share/graphviz/doc/html/info/g_rad0.png
/usr/share/graphviz/doc/html/info/g_rad180.png
/usr/share/graphviz/doc/html/info/g_rad270.png
/usr/share/graphviz/doc/html/info/g_rad360.png
/usr/share/graphviz/doc/html/info/g_rad45.png
/usr/share/graphviz/doc/html/info/g_rad90.png
/usr/share/graphviz/doc/html/info/hexagon.gif
/usr/share/graphviz/doc/html/info/house.gif
/usr/share/graphviz/doc/html/info/html1.gif
/usr/share/graphviz/doc/html/info/html2.gif
/usr/share/graphviz/doc/html/info/html2.gv
/usr/share/graphviz/doc/html/info/html3.gif
/usr/share/graphviz/doc/html/info/html3.gv
/usr/share/graphviz/doc/html/info/html4.gif
/usr/share/graphviz/doc/html/info/html4.gv
/usr/share/graphviz/doc/html/info/index.html
/usr/share/graphviz/doc/html/info/invhouse.gif
/usr/share/graphviz/doc/html/info/invtrapezium.gif
/usr/share/graphviz/doc/html/info/invtriangle.gif
/usr/share/graphviz/doc/html/info/lang.html
/usr/share/graphviz/doc/html/info/mrecord.gif
/usr/share/graphviz/doc/html/info/n_bold.png
/usr/share/graphviz/doc/html/info/n_dashed.png
/usr/share/graphviz/doc/html/info/n_diagonals.png
/usr/share/graphviz/doc/html/info/n_dotted.png
/usr/share/graphviz/doc/html/info/n_filled.png
/usr/share/graphviz/doc/html/info/n_rounded.png
/usr/share/graphviz/doc/html/info/n_solid.png
/usr/share/graphviz/doc/html/info/n_striped.png
/usr/share/graphviz/doc/html/info/n_wedged.png
/usr/share/graphviz/doc/html/info/nohead.gif
/usr/share/graphviz/doc/html/info/none.gif
/usr/share/graphviz/doc/html/info/none_back.png
/usr/share/graphviz/doc/html/info/none_both.png
/usr/share/graphviz/doc/html/info/none_forward.png
/usr/share/graphviz/doc/html/info/none_none.png
/usr/share/graphviz/doc/html/info/normal_back.png
/usr/share/graphviz/doc/html/info/normal_both.png
/usr/share/graphviz/doc/html/info/normal_forward.png
/usr/share/graphviz/doc/html/info/normal_none.png
/usr/share/graphviz/doc/html/info/note.gif
/usr/share/graphviz/doc/html/info/octagon.gif
/usr/share/graphviz/doc/html/info/output.html
/usr/share/graphviz/doc/html/info/oval.gif
/usr/share/graphviz/doc/html/info/parallelogram.gif
/usr/share/graphviz/doc/html/info/pentagon.gif
/usr/share/graphviz/doc/html/info/plain.gif
/usr/share/graphviz/doc/html/info/plaintext.gif
/usr/share/graphviz/doc/html/info/plugins.png
/usr/share/graphviz/doc/html/info/point.gif
/usr/share/graphviz/doc/html/info/polygon.gif
/usr/share/graphviz/doc/html/info/record.gif
/usr/share/graphviz/doc/html/info/record2.gif
/usr/share/graphviz/doc/html/info/rect.gif
/usr/share/graphviz/doc/html/info/rectangle.gif
/usr/share/graphviz/doc/html/info/round.gif
/usr/share/graphviz/doc/html/info/sdlshapes.png
/usr/share/graphviz/doc/html/info/septagon.gif
/usr/share/graphviz/doc/html/info/shapes.html
/usr/share/graphviz/doc/html/info/spline_curved.png
/usr/share/graphviz/doc/html/info/spline_line.png
/usr/share/graphviz/doc/html/info/spline_none.png
/usr/share/graphviz/doc/html/info/spline_ortho.png
/usr/share/graphviz/doc/html/info/spline_polyline.png
/usr/share/graphviz/doc/html/info/spline_spline.png
/usr/share/graphviz/doc/html/info/square.gif
/usr/share/graphviz/doc/html/info/tab.gif
/usr/share/graphviz/doc/html/info/trapezium.gif
/usr/share/graphviz/doc/html/info/triangle.gif
/usr/share/graphviz/doc/html/info/tripleoctagon.gif
/usr/share/graphviz/doc/html/info/underline.gif
/usr/share/graphviz/doc/html/internal_todo.html
/usr/share/graphviz/doc/html/pspdf.png
/usr/share/graphviz/doc/html/schema/arguments.xml
/usr/share/graphviz/doc/html/schema/attributes.xml
/usr/share/graphviz/doc/html/schema/attributes.xslt
/usr/share/graphviz/doc/html/tcldot.html
/usr/share/graphviz/doc/html/todo.html
/usr/share/graphviz/doc/html/winbuild.html
/usr/share/graphviz/doc/latex_suggestions.txt
/usr/share/graphviz/doc/pdf/Agraph.pdf
/usr/share/graphviz/doc/pdf/acyclic.1.pdf
/usr/share/graphviz/doc/pdf/bcomps.1.pdf
/usr/share/graphviz/doc/pdf/ccomps.1.pdf
/usr/share/graphviz/doc/pdf/cdt.3.pdf
/usr/share/graphviz/doc/pdf/cgraph.3.pdf
/usr/share/graphviz/doc/pdf/circo.1.pdf
/usr/share/graphviz/doc/pdf/cluster.1.pdf
/usr/share/graphviz/doc/pdf/diffimg.1.pdf
/usr/share/graphviz/doc/pdf/dijkstra.1.pdf
/usr/share/graphviz/doc/pdf/dot.1.pdf
/usr/share/graphviz/doc/pdf/dot2gxl.1.pdf
/usr/share/graphviz/doc/pdf/dotguide.pdf
/usr/share/graphviz/doc/pdf/dotty.1.pdf
/usr/share/graphviz/doc/pdf/dottyguide.pdf
/usr/share/graphviz/doc/pdf/edgepaint.1.pdf
/usr/share/graphviz/doc/pdf/expr.3.pdf
/usr/share/graphviz/doc/pdf/fdp.1.pdf
/usr/share/graphviz/doc/pdf/gc.1.pdf
/usr/share/graphviz/doc/pdf/gdtclft.3tcl.pdf
/usr/share/graphviz/doc/pdf/gml2gv.1.pdf
/usr/share/graphviz/doc/pdf/graphml2gv.1.pdf
/usr/share/graphviz/doc/pdf/gv2gml.1.pdf
/usr/share/graphviz/doc/pdf/gv2gxl.1.pdf
/usr/share/graphviz/doc/pdf/gvc.3.pdf
/usr/share/graphviz/doc/pdf/gvcolor.1.pdf
/usr/share/graphviz/doc/pdf/gvedit.1.pdf
/usr/share/graphviz/doc/pdf/gvgen.1.pdf
/usr/share/graphviz/doc/pdf/gvmap.1.pdf
/usr/share/graphviz/doc/pdf/gvmap.sh.1.pdf
/usr/share/graphviz/doc/pdf/gvpack.1.pdf
/usr/share/graphviz/doc/pdf/gvpr.1.pdf
/usr/share/graphviz/doc/pdf/gvpr.3.pdf
/usr/share/graphviz/doc/pdf/gxl2dot.1.pdf
/usr/share/graphviz/doc/pdf/gxl2gv.1.pdf
/usr/share/graphviz/doc/pdf/lefty.1.pdf
/usr/share/graphviz/doc/pdf/leftyguide.pdf
/usr/share/graphviz/doc/pdf/libguide.pdf
/usr/share/graphviz/doc/pdf/lneato.1.pdf
/usr/share/graphviz/doc/pdf/mingle.1.pdf
/usr/share/graphviz/doc/pdf/mm2gv.1.pdf
/usr/share/graphviz/doc/pdf/neato.1.pdf
/usr/share/graphviz/doc/pdf/neatoguide.pdf
/usr/share/graphviz/doc/pdf/nop.1.pdf
/usr/share/graphviz/doc/pdf/osage.1.pdf
/usr/share/graphviz/doc/pdf/pack.3.pdf
/usr/share/graphviz/doc/pdf/patchwork.1.pdf
/usr/share/graphviz/doc/pdf/pathplan.3.pdf
/usr/share/graphviz/doc/pdf/prune.1.pdf
/usr/share/graphviz/doc/pdf/sccmap.1.pdf
/usr/share/graphviz/doc/pdf/sfdp.1.pdf
/usr/share/graphviz/doc/pdf/smyrna.pdf
/usr/share/graphviz/doc/pdf/tcldot.3tcl.pdf
/usr/share/graphviz/doc/pdf/tred.1.pdf
/usr/share/graphviz/doc/pdf/twopi.1.pdf
/usr/share/graphviz/doc/pdf/unflatten.1.pdf
/usr/share/graphviz/doc/pdf/vimdot.1.pdf
/usr/share/graphviz/doc/pdf/xdot.3.pdf
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
/usr/share/graphviz/gvedit/attrs.txt
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
/usr/share/graphviz/lefty/box.lefty
/usr/share/graphviz/lefty/def.lefty
/usr/share/graphviz/lefty/dotty.lefty
/usr/share/graphviz/lefty/dotty_draw.lefty
/usr/share/graphviz/lefty/dotty_edit.lefty
/usr/share/graphviz/lefty/dotty_layout.lefty
/usr/share/graphviz/lefty/dotty_ui.lefty
/usr/share/graphviz/lefty/fractal.lefty
/usr/share/graphviz/lefty/fractal2.lefty
/usr/share/graphviz/lefty/lefty.psp
/usr/share/graphviz/lefty/slides.lefty
/usr/share/graphviz/lefty/tree.lefty

%files dev
%defattr(-,root,root,-)
/usr/include/graphviz/arith.h
/usr/include/graphviz/cdt.h
/usr/include/graphviz/cgraph.h
/usr/include/graphviz/color.h
/usr/include/graphviz/geom.h
/usr/include/graphviz/graphviz_version.h
/usr/include/graphviz/gv.cpp
/usr/include/graphviz/gv.i
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
/usr/lib64/liblab_gamut.so
/usr/lib64/libpathplan.so
/usr/lib64/libxdot.so
/usr/lib64/pkgconfig/libcdt.pc
/usr/lib64/pkgconfig/libcgraph.pc
/usr/lib64/pkgconfig/libgvc.pc
/usr/lib64/pkgconfig/libgvpr.pc
/usr/lib64/pkgconfig/liblab_gamut.pc
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

%files extras
%defattr(-,root,root,-)
/usr/bin/diffimg
/usr/bin/dot_builtins
/usr/bin/gvedit
/usr/lib64/graphviz/libgvplugin_gd.so
/usr/lib64/graphviz/libgvplugin_gd.so.6
/usr/lib64/graphviz/libgvplugin_gd.so.6.0.0
/usr/lib64/graphviz/libgvplugin_gdk.so
/usr/lib64/graphviz/libgvplugin_gdk.so.6
/usr/lib64/graphviz/libgvplugin_gdk.so.6.0.0
/usr/lib64/graphviz/libgvplugin_gs.so
/usr/lib64/graphviz/libgvplugin_gs.so.6
/usr/lib64/graphviz/libgvplugin_gs.so.6.0.0
/usr/lib64/graphviz/libgvplugin_gtk.so
/usr/lib64/graphviz/libgvplugin_gtk.so.6
/usr/lib64/graphviz/libgvplugin_gtk.so.6.0.0
/usr/lib64/graphviz/libgvplugin_pango.so
/usr/lib64/graphviz/libgvplugin_pango.so.6
/usr/lib64/graphviz/libgvplugin_pango.so.6.0.0
/usr/lib64/graphviz/libgvplugin_rsvg.so
/usr/lib64/graphviz/libgvplugin_rsvg.so.6
/usr/lib64/graphviz/libgvplugin_rsvg.so.6.0.0
/usr/lib64/graphviz/libgvplugin_xlib.so
/usr/lib64/graphviz/libgvplugin_xlib.so.6
/usr/lib64/graphviz/libgvplugin_xlib.so.6.0.0
/usr/lib64/graphviz/tcl/libgdtclft.so
/usr/lib64/graphviz/tcl/libgdtclft.so.0
/usr/lib64/graphviz/tcl/libgdtclft.so.0.0.0
/usr/lib64/graphviz/tcl/libtcldot.so
/usr/lib64/graphviz/tcl/libtcldot.so.0
/usr/lib64/graphviz/tcl/libtcldot.so.0.0.0
/usr/lib64/graphviz/tcl/libtcldot_builtin.so
/usr/lib64/graphviz/tcl/libtcldot_builtin.so.0
/usr/lib64/graphviz/tcl/libtcldot_builtin.so.0.0.0
/usr/lib64/graphviz/tcl/libtclplan.so
/usr/lib64/graphviz/tcl/libtclplan.so.0
/usr/lib64/graphviz/tcl/libtclplan.so.0.0.0
/usr/lib64/tcl8.6/graphviz/libgdtclft.so
/usr/lib64/tcl8.6/graphviz/libgdtclft.so.0
/usr/lib64/tcl8.6/graphviz/libgdtclft.so.0.0.0
/usr/lib64/tcl8.6/graphviz/libtcldot.so
/usr/lib64/tcl8.6/graphviz/libtcldot.so.0
/usr/lib64/tcl8.6/graphviz/libtcldot.so.0.0.0
/usr/lib64/tcl8.6/graphviz/libtcldot_builtin.so
/usr/lib64/tcl8.6/graphviz/libtcldot_builtin.so.0
/usr/lib64/tcl8.6/graphviz/libtcldot_builtin.so.0.0.0
/usr/lib64/tcl8.6/graphviz/libtclplan.so
/usr/lib64/tcl8.6/graphviz/libtclplan.so.0
/usr/lib64/tcl8.6/graphviz/libtclplan.so.0.0.0

%files lib
%defattr(-,root,root,-)
/usr/lib64/graphviz/libgvplugin_core.so
/usr/lib64/graphviz/libgvplugin_core.so.6
/usr/lib64/graphviz/libgvplugin_core.so.6.0.0
/usr/lib64/graphviz/libgvplugin_dot_layout.so
/usr/lib64/graphviz/libgvplugin_dot_layout.so.6
/usr/lib64/graphviz/libgvplugin_dot_layout.so.6.0.0
/usr/lib64/graphviz/libgvplugin_neato_layout.so
/usr/lib64/graphviz/libgvplugin_neato_layout.so.6
/usr/lib64/graphviz/libgvplugin_neato_layout.so.6.0.0
/usr/lib64/graphviz/libgvplugin_visio.so
/usr/lib64/graphviz/libgvplugin_visio.so.6
/usr/lib64/graphviz/libgvplugin_visio.so.6.0.0
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
/usr/lib64/liblab_gamut.so.1
/usr/lib64/liblab_gamut.so.1.0.0
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
/usr/share/man/man1/dotty.1
/usr/share/man/man1/edgepaint.1
/usr/share/man/man1/fdp.1
/usr/share/man/man1/gc.1
/usr/share/man/man1/gml2gv.1
/usr/share/man/man1/graphml2gv.1
/usr/share/man/man1/gv2gml.1
/usr/share/man/man1/gv2gxl.1
/usr/share/man/man1/gvcolor.1
/usr/share/man/man1/gvedit.1
/usr/share/man/man1/gvgen.1
/usr/share/man/man1/gvmap.1
/usr/share/man/man1/gvmap.sh.1
/usr/share/man/man1/gvpack.1
/usr/share/man/man1/gvpr.1
/usr/share/man/man1/gxl2dot.1
/usr/share/man/man1/gxl2gv.1
/usr/share/man/man1/lefty.1
/usr/share/man/man1/lneato.1
/usr/share/man/man1/mingle.1
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
