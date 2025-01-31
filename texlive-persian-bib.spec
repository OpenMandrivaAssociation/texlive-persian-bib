Name:		texlive-persian-bib
Version:	37297
Release:	2
Summary:	Persian translations of classic BibTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/persian-bib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-bib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-bib.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Currently 7 files: acm-fa.bst, asa-fa.bst, chicago-fa.bst,
ieeetr-fa.bst, plain-fa.bst, plainnat-fa.bst and unsrt-fa.bst
are modified for Persian documents prepared with XePersian
(which the present package depends on). The Persian .bst files
can simultaneously handle both Latin and Persian references. A
file cp1256fa.csf is provided for correct sorting of Persian
references and three fields LANGUAGE, TRANSLATOR and AUTHORFA
are defined.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/persian-bib
%{_texmfdistdir}/bibtex/csf/persian-bib
%doc %{_texmfdistdir}/doc/xelatex/persian-bib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
