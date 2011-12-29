# revision 23267
# category Package
# catalog-ctan /biblio/bibtex/contrib/persian-bib
# catalog-date 2011-07-10 22:10:07 +0200
# catalog-license lppl
# catalog-version 0.6
Name:		texlive-persian-bib
Version:	0.6
Release:	1
Summary:	Persian translations of classic BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/persian-bib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-bib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-bib.doc.tar.xz
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
%{_texmfdistdir}/bibtex/bst/persian-bib/acm-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/asa-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/chicago-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/ieeetr-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/plain-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/plainnat-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/unsrt-fa.bst
%{_texmfdistdir}/bibtex/csf/persian-bib/cp1256fa.csf
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/MyReferences.bib
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/Persian-bib-userguide.pdf
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/Persian-bib-userguide.tex
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/README
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/bibtex-example.pdf
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/bibtex-example.tex
%doc %{_texmfdistdir}/doc/xelatex/persian-bib/gen_pdf.pl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
