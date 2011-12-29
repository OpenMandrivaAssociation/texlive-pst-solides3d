# revision 19959
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-solides3d
# catalog-date 2010-09-29 09:03:07 +0200
# catalog-license lppl1.3
# catalog-version 4.23
Name:		texlive-pst-solides3d
Version:	4.23
Release:	1
Summary:	Draw perspective views of 3D solids
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-solides3d
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solides3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solides3d.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed to draw solids in 3d perspective.
Features include: - create primitive solids; - create solids by
including a list of its vertices and faces; - faces of solids
and surfaces can be colored by choosing from a very large
palette of colors; - draw parametric surfaces in algebraic and
reverse polish notation; - create explicit and parameterized
algebraic functions drawn in 2 or 3 dimensions; - project text
onto a plane and onto the faces of a solid; - support for
including external database files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-solides3d/pst-solides3d.pro
%{_texmfdistdir}/tex/generic/pst-solides3d/pst-solides3d.tex
%{_texmfdistdir}/tex/latex/pst-solides3d/pst-solides3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/README
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/Changes
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/Makefile
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/Pyramid-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/Pyramid-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/Pyramid-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/Pyramid-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/README
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/chapter-1-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/chapter-2-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubeHexagone-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubeHexagone-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubeHexagone-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubeHexagone-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubecolor-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubecolor-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubecolor-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/cubecolor-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/faces_nefer.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/faces_nefer_levres.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/faces_nefer_sourcils.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/faces_nefer_yeux.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/fusee62-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/fusee62-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/fusee62-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/fusee62-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/geodedual44-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/geodedual44-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/geodedual44-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/geodedual44-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/horoptere-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/horoptere-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/horoptere-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/horoptere-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/kepler.eps
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-acknowledgements-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-affinage-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-anneaux-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-annoterschema-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-axes3D-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-chanfrein-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-codejps-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-colorierfacettes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-commandestrace-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-couleurs-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-courbeR3-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-cylindres-cones-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-datfile-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-definirfonction-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-definirplanquelconque-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-definitionmaillage-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-eclairageponctuel-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-enleverfacettes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-extensions-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-face-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-fusion-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-fusionjps-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-geode-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-grille-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-keywords-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-ligne3D-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-lignedeniveau-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-modes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-new-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-nommersolide-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-numeroterfacettes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-opacity-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-parametres-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-plan-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-poems-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-point-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-pointagesommets-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-positionnerpointconnu-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-positionnersolide-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-prisme-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectionangledroit-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectioncercle-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectioncourbe-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectiondroite-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectionligne-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectionpoint-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectionpolygone-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectiontexte-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectionvecteur-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projectionvisibility-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-projpresentation-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-ruban-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-section-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-solidescreux-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-solidespredefinis-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-surfaces-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-surfacesparametrees-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-tracerpolygone-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-transform-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-transformpointconnu-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-tronque-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-tube-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/par-vecteur-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/paraboloid-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/paraboloid-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/paraboloid-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/paraboloid-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/pst-solides3d-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/pst-solides3d-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/rocket.obj
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/slicePyramid-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/slicePyramid-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/slicePyramid-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/slicePyramid-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/sommets_nefer.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/sommets_nefer0.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tex-files-all.zip
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1836-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1836-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1836-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1836-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860lemniscate-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860lemniscate-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860lemniscate-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860lemniscate-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860ovales-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860ovales-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860ovales-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860ovales-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860part-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860part-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860part-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/doc-en/tore1860part-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/pst-solides3d-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
