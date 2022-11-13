Name:		texlive-invoice
Version:	48359
Release:	1
Summary:	Generate invoices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/invoice
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/invoice
%doc %{_texmfdistdir}/doc/latex/invoice

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
