# revision 24194
# category Package
# catalog-ctan /macros/latex/contrib/invoice
# catalog-date 2011-10-04 18:45:10 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-invoice
Version:	20111004
Release:	2
Summary:	Generate invoices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/invoice
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package may be used for generating invoices. The package
can deal with invisible expense items and deductions; output
may be presented in any of 10 different languages. The package
depends on the fp and calc packages for its calculations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/invoice/invoice.def
%{_texmfdistdir}/tex/latex/invoice/invoice.sty
%doc %{_texmfdistdir}/doc/latex/invoice/00README.tex
%doc %{_texmfdistdir}/doc/latex/invoice/copying
%doc %{_texmfdistdir}/doc/latex/invoice/history
%doc %{_texmfdistdir}/doc/latex/invoice/install
%doc %{_texmfdistdir}/doc/latex/invoice/invoice.pdf
%doc %{_texmfdistdir}/doc/latex/invoice/invoice.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111004-2
+ Revision: 752803
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111004-1
+ Revision: 718729
- texlive-invoice
- texlive-invoice
- texlive-invoice
- texlive-invoice

