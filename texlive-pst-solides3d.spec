%global tl_name pst-solides3d
%global tl_revision 79298

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.36
Release:	%{tl_revision}.1
Summary:	Draw perspective views of 3D solids
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-solides3d
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solides3d.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solides3d.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is designed to draw solids in 3d perspective. Features
include: create primitive solids; create solids by including a list of
its vertices and faces; faces of solids and surfaces can be colored by
choosing from a very large palette of colors; draw parametric surfaces
in algebraic and reverse polish notation; create explicit and
parameterized algebraic functions drawn in 2 or 3 dimensions; project
text onto a plane or onto the faces of a solid; support for including
external database files.

