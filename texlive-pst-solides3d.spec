Name:		texlive-pst-solides3d
Version:	61719
Release:	1
Summary:	Draw perspective views of 3D solids
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-solides3d
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solides3d.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-solides3d.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-solides3d
%{_texmfdistdir}/tex/generic/pst-solides3d
%{_texmfdistdir}/tex/latex/pst-solides3d

%doc %{_texmfdistdir}/doc/generic/pst-solides3d

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
