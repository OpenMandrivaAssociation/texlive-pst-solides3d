# revision 33375
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-solides3d
# catalog-date 2014-03-28 18:05:25 +0100
# catalog-license lppl1.3
# catalog-version 4.245
Name:		texlive-pst-solides3d
Version:	4.245
Release:	2
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
Features include: create primitive solids; create solids by
including a list of its vertices and faces; faces of solids and
surfaces can be colored by choosing from a very large palette
of colors; draw parametric surfaces in algebraic and reverse
polish notation; create explicit and parameterized algebraic
functions drawn in 2 or 3 dimensions; project text onto a plane
and onto the faces of a solid; support for including external
database files.

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

%doc %{_texmfdistdir}/doc/generic/pst-solides3d/README
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/pst-solides3d-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Changes
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Letter.ist
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Makefile
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Pyramid-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Pyramid-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Pyramid-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/Pyramid-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/chapter-1-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/chapter-2-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubeHexagone-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubeHexagone-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubeHexagone-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubeHexagone-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubecolor-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubecolor-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubecolor-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/cubecolor-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/faces_nefer.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/faces_nefer_levres.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/faces_nefer_sourcils.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/faces_nefer_yeux.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/fusee62-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/fusee62-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/fusee62-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/fusee62-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/geodedual44-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/geodedual44-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/geodedual44-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/geodedual44-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/horoptere-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/horoptere-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/horoptere-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/horoptere-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/kepler.eps
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-acknowledgements-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-affinage-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-anneaux-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-annoterschema-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-axes3D-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-chanfrein-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-codejps-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-colorierfacettes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-commandestrace-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-couleurs-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-courbeR3-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-cylindres-cones-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-datfile-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-definirfonction-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-definirplanquelconque-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-definitionmaillage-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-eclairageponctuel-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-enleverfacettes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-extensions-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-face-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-fusion-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-fusionjps-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-geode-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-grille-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-image2d-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-keywords-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-ligne3D-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-lignedeniveau-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-modes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-new-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-nommersolide-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-numeroterfacettes-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-opacity-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-parametres-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-plan-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-poems-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-point-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-pointagesommets-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-positionnerpointconnu-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-positionnersolide-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-prisme-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectionangledroit-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectioncercle-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectioncourbe-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectiondroite-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectionligne-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectionpoint-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectionpolygone-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectiontexte-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectionvecteur-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projectionvisibility-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-projpresentation-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-ruban-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-section-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-solidescreux-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-solidespredefinis-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-surfaces-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-surfacesparametrees-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-tracerpolygone-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-transform-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-transformpointconnu-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-tronque-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-tube-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/par-vecteur-en.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/paraboloid-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/paraboloid-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/paraboloid-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/paraboloid-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/parrot.eps
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/pst-solides3d-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/pst-solides3d-doc.ps
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/pst-solides3d-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/rocket.obj
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/slicePyramid-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/slicePyramid-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/slicePyramid-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/slicePyramid-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/sommets_nefer.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/sommets_nefer0.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tiger.eps
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1836-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1836-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1836-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1836-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860lemniscate-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860lemniscate-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860lemniscate-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860lemniscate-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860ovales-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860ovales-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860ovales-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860ovales-sommets.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860part-couleurs.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860part-faces.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860part-io.dat
%doc %{_texmfdistdir}/doc/generic/pst-solides3d/src/tore1860part-sommets.dat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
